import process from 'node:process';
import { randomUUID } from 'node:crypto';

import cors from 'cors';
import express from 'express';

import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { StreamableHTTPServerTransport } from '@modelcontextprotocol/sdk/server/streamableHttp.js';
import { z } from 'zod';

import {
  fetchGithubDocument,
  searchGithubDocs,
} from './github.js';

const DEFAULT_HTTP_PORT = 8000;
const DEFAULT_HTTP_PATH = '/mcp';

async function createServer(): Promise<void> {
  const transportMode = process.env.BITRIX24_MCP_TRANSPORT ?? 'stdio';

  if (transportMode === 'http') {
    await startHttpServer();
  } else {
    await startStdioServer();
  }
}

export function createMcpServer(): McpServer {
  const repo = process.env.BITRIX24_GITHUB_REPO ?? 'bitrix24/b24restdocs';

  const mcpServer = new McpServer(
    {
      name: 'bitrix24-docs-mcp',
      version: '0.2.0',
    },
    {
      instructions:
        `Инструменты обращаются к актуальной документации Bitrix24 через GitHub-репозиторий ${repo}. Используйте bitrix_docs_search для поиска и bitrix_docs_fetch для получения полного текста.`,
    },
  );

  const searchInput = z.object({
    query: z
      .string()
      .min(2, 'Строка запроса должна содержать минимум 2 символа'),
    limit: z
      .number()
      .int()
      .min(1)
      .max(20)
      .default(5)
      .describe('Максимальное количество результатов'),
  });

  mcpServer.registerTool(
    'bitrix_docs_search',
    {
      title: 'Поиск по документации Bitrix24',
      description:
        'Выполняет поиск по GitHub-репозиторию документации Bitrix24 и возвращает релевантные страницы.',
      inputSchema: searchInput.shape,
    },
    async ({ query, limit }) => {
      try {
        const results = await searchGithubDocs(query, limit ?? 5, repo);
        if (results.length === 0) {
          return {
            content: [
              {
                type: 'text' as const,
                text: `По запросу "${query}" ничего не найдено. Попробуйте уточнить формулировку.`,
              },
            ],
          };
        }

        const formatted = results
          .map((result, index) => {
            return `${index + 1}. ${result.title}\nURL: ${result.htmlUrl}\nПуть: ${result.path}\nСниппет: ${result.snippet}\n`;
          })
          .join('\n');

        return {
          content: [
            {
              type: 'text' as const,
              text: formatted,
            },
          ],
        };
      } catch (error) {
        return {
          isError: true,
          content: [
            {
              type: 'text' as const,
              text: error instanceof Error ? error.message : String(error),
            },
          ],
        };
      }
    },
  );

  const fetchInput = z.object({
    slug: z
      .string()
      .min(1)
      .optional()
      .describe('Путь внутри репозитория (например, api-reference/catalog/index.md)'),
    url: z
      .string()
      .url()
      .optional()
      .describe('Полный URL GitHub к документу'),
  });

  mcpServer.registerTool(
    'bitrix_docs_fetch',
    {
      title: 'Получение полного документа Bitrix24',
      description:
        'Загружает Markdown-документ из репозитория документации Bitrix24 по указанному пути или ссылке.',
      inputSchema: fetchInput.shape,
    },
    async ({ slug, url }) => {
      const identifier = slug ?? url;
      if (!identifier) {
        return {
          isError: true,
          content: [
            {
              type: 'text' as const,
              text: 'Нужно указать slug или url документа.',
            },
          ],
        };
      }

      try {
        const doc = await fetchGithubDocument(identifier);
        const header = `# ${doc.title}\nИсточник: ${doc.htmlUrl}\nПуть: ${doc.path}\n`;
        return {
          content: [
            {
              type: 'text' as const,
              text: `${header}\n${doc.content}`,
            },
          ],
        };
      } catch (error) {
        return {
          isError: true,
          content: [
            {
              type: 'text' as const,
              text: error instanceof Error ? error.message : String(error),
            },
          ],
        };
      }
    },
  );

  return mcpServer;
}

async function startStdioServer(): Promise<void> {
  const mcpServer = createMcpServer();
  const transport = new StdioServerTransport();
  await mcpServer.connect(transport);
  // eslint-disable-next-line no-console
  console.log('Bitrix24 MCP сервер (stdio) запущен. Источник: GitHub.');
}

async function startHttpServer(): Promise<void> {
  const app = express();
  app.use(express.json({ limit: '10mb' }));
  app.use(cors());

  const pathPrefix = process.env.BITRIX24_MCP_HTTP_PATH ?? DEFAULT_HTTP_PATH;
  const port = Number.parseInt(
    process.env.BITRIX24_MCP_HTTP_PORT ?? String(DEFAULT_HTTP_PORT),
    10,
  );

  app.post(pathPrefix, async (req, res) => {
    const server = createMcpServer();
    const transport = new StreamableHTTPServerTransport({
      sessionIdGenerator: () => randomUUID(),
    });

    try {
      await server.connect(transport);
      await transport.handleRequest(req, res, req.body);
    } catch (error) {
      console.error('Ошибка обработки HTTP-запроса MCP:', error);
      if (!res.headersSent) {
        res.status(500).json({
          jsonrpc: '2.0',
          error: {
            code: -32603,
            message: 'Internal server error',
          },
          id: null,
        });
      }
    } finally {
      res.on('close', () => {
        void transport.close();
        void server.close();
      });
    }
  });

  app.all(pathPrefix, (_req, res) => {
    res.status(405).json({
      jsonrpc: '2.0',
      error: {
        code: -32000,
        message: 'Method not allowed',
      },
      id: null,
    });
  });

  app.listen(port, () => {
    console.log(
      `Bitrix24 MCP сервер (HTTP) запущен на порту ${port}, путь ${pathPrefix}. Источник: GitHub репозиторий документации.`,
    );
  });
}

if (process.env.NODE_ENV !== 'test') {
  createServer().catch((error) => {
    console.error('Критическая ошибка сервера:', error);
    process.exit(1);
  });
}
