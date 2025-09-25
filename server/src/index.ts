import fs from 'node:fs/promises';
import path from 'node:path';
import process from 'node:process';
import { fileURLToPath } from 'node:url';
import { randomUUID } from 'node:crypto';

import express from 'express';
import cors from 'cors';

import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { StreamableHTTPServerTransport } from '@modelcontextprotocol/sdk/server/streamableHttp.js';
import { z } from 'zod';
import type { ZodRawShape } from 'zod';

interface IndexEntry {
  slug: string;
  url: string;
  title?: string;
  text_preview?: string;
  markdown_path: string;
  retrieved_at?: string;
}

interface SearchMatch {
  entry: IndexEntry;
  score: number;
  snippet: string;
}

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const DEFAULT_INDEX_PATH = path.resolve(
  __dirname,
  '..',
  '..',
  'data',
  'index',
  'simple_index.json',
);

class BitrixDocsIndex {
  private entries: IndexEntry[];
  private bySlug: Map<string, IndexEntry>;
  private dataDir: string;

  private constructor(entries: IndexEntry[], dataDir: string) {
    this.entries = entries;
    this.bySlug = new Map(entries.map((entry) => [entry.slug, entry]));
    this.dataDir = dataDir;
  }

  static async load(indexPath: string): Promise<BitrixDocsIndex> {
    const raw = await fs.readFile(indexPath, 'utf-8');
    const entries = JSON.parse(raw) as IndexEntry[];
    const dataDir = path.resolve(path.dirname(indexPath), '..');
    return new BitrixDocsIndex(entries, dataDir);
  }

  search(query: string, limit = 5): SearchMatch[] {
    const normalized = query.toLowerCase().trim();
    if (!normalized) {
      return [];
    }
    const tokens = normalized.split(/\s+/).filter(Boolean);

    const matches: SearchMatch[] = [];
    for (const entry of this.entries) {
      const haystackTitle = (entry.title ?? '').toLowerCase();
      const haystackPreview = (entry.text_preview ?? '').toLowerCase();

      let score = 0;
      let snippet = '';

      for (const token of tokens) {
        if (haystackTitle.includes(token)) {
          score += 3;
        }
        if (haystackPreview.includes(token)) {
          score += 1;
        }
      }

      if (score > 0) {
        snippet = this.buildSnippet(entry, tokens);
        matches.push({ entry, score, snippet });
      }
    }

    return matches
      .sort((a, b) => b.score - a.score)
      .slice(0, limit ?? 5);
  }

  async getMarkdown(entry: IndexEntry): Promise<string> {
    const markdownPath = path.resolve(this.dataDir, entry.markdown_path);
    return await fs.readFile(markdownPath, 'utf-8');
  }

  getEntries(): IndexEntry[] {
    return [...this.entries];
  }

  getBySlugOrUrl(identifier: string): IndexEntry | undefined {
    const trimmed = identifier.trim();
    if (!trimmed) {
      return undefined;
    }

    const bySlug = this.bySlug.get(trimmed);
    if (bySlug) {
      return bySlug;
    }

    return this.entries.find((item) => item.url === trimmed);
  }

  private buildSnippet(entry: IndexEntry, tokens: string[]): string {
    const source = entry.text_preview ?? '';
    if (!source) {
      return '';
    }
    const lower = source.toLowerCase();
    for (const token of tokens) {
      const idx = lower.indexOf(token);
      if (idx >= 0) {
        const start = Math.max(0, idx - 60);
        const end = Math.min(source.length, idx + token.length + 60);
        const excerpt = source.slice(start, end).trim();
        return excerpt.replace(/\s+/g, ' ');
      }
    }
    return source.slice(0, 160).replace(/\s+/g, ' ');
  }
}

function formatDocument(entry: IndexEntry, body: string): string {
  const headerLines = [
    `# ${entry.title ?? entry.slug}`,
    `Источник: ${entry.url}`,
    `Получено: ${entry.retrieved_at ?? 'неизвестно'}`,
    '',
  ];
  return [...headerLines, body].join('\n');
}

async function createServer(): Promise<void> {
  const indexPath = process.env.BITRIX24_MCP_INDEX_PATH
    ? path.resolve(process.env.BITRIX24_MCP_INDEX_PATH)
    : DEFAULT_INDEX_PATH;

  let docsIndex: BitrixDocsIndex;
  try {
    docsIndex = await BitrixDocsIndex.load(indexPath);
  } catch (error) {
    console.error(`Не удалось загрузить индекс по пути ${indexPath}:`, error);
    process.exit(1);
    return;
  }

  const transportMode = process.env.BITRIX24_MCP_TRANSPORT ?? 'stdio';

  if (transportMode === 'http') {
    await startHttpServer(docsIndex, indexPath);
  } else {
    await startStdioServer(docsIndex, indexPath);
  }
}

export function createMcpServer(docsIndex: Pick<
  BitrixDocsIndex,
  'getEntries' | 'search' | 'getMarkdown' | 'getBySlugOrUrl'
>): McpServer {
  const mcpServer = new McpServer(
    {
      name: 'bitrix24-docs-mcp',
      version: '0.1.0',
    },
    {
      instructions:
        'Используйте инструменты `bitrix_docs_search` и `bitrix_docs_fetch` для работы с документацией Bitrix24. Документы также доступны как ресурсы с URI `bitrix24-docs://docs/<slug>`.',
      capabilities: {
        resources: {},
        tools: {},
      },
    },
  );

  const searchInputShape = {
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
  } satisfies ZodRawShape;

  mcpServer.registerTool(
    'bitrix_docs_search',
    {
      title: 'Поиск по документации Bitrix24',
      description:
        'Выполняет поиск по локальному индексу документации Bitrix24 и возвращает топ-результаты.',
      inputSchema: searchInputShape,
    },
    async ({ query, limit }) => {
      const results = docsIndex.search(query, limit ?? 5);
      if (results.length === 0) {
        return {
          content: [
            {
              type: 'text' as const,
              text: `По запросу "${query}" ничего не найдено. Попробуйте переформулировать запрос.`,
            },
          ],
        };
      }

      const formatted = results
        .map((result, index) => {
          const { entry, snippet, score } = result;
          return `${index + 1}. ${entry.title ?? 'Без названия'}\nURL: ${entry.url}\nСлаг: ${entry.slug}\nСниппет: ${snippet}\nСчёт: ${score}`;
        })
        .join('\n\n');

      return {
        content: [
          {
            type: 'text' as const,
            text: formatted,
          },
        ],
      };
    },
  );

  const fetchInputShape = {
    slug: z
      .string()
      .min(1)
      .optional()
      .describe('Слаг документа (из результатов поиска)'),
    url: z
      .string()
      .url()
      .optional()
      .describe('Полный URL документации Bitrix24'),
  } satisfies ZodRawShape;

  mcpServer.registerTool(
    'bitrix_docs_fetch',
    {
      title: 'Получение полного документа Bitrix24',
      description:
        'Возвращает Markdown-версию документа Bitrix24 по слагу или URL. Требует предварительного обхода документации.',
      inputSchema: fetchInputShape,
    },
    async ({ slug, url }) => {
      const identifier = slug ?? url ?? '';
      if (!identifier) {
        return {
          content: [
            {
              type: 'text' as const,
              text: 'Нужно указать slug или url для получения документа.',
            },
          ],
        };
      }
      const entry = docsIndex.getBySlugOrUrl(identifier);
      if (!entry) {
        return {
          content: [
            {
              type: 'text' as const,
              text: `Документ с идентификатором "${identifier}" не найден в индексе. Выполните crawl/normalize/index перед запуском сервера.`,
            },
          ],
        };
      }

      try {
        const markdown = await docsIndex.getMarkdown(entry);
        return {
          content: [
            {
              type: 'text' as const,
              text: formatDocument(entry, markdown),
            },
          ],
        };
      } catch (error) {
        return {
          content: [
            {
              type: 'text' as const,
              text: `Не удалось прочитать файл для "${entry.slug}": ${error instanceof Error ? error.message : String(error)}`,
            },
          ],
        };
      }
    },
  );

  const resourceEntries = docsIndex.getEntries();
  for (const entry of resourceEntries) {
    const resourceUri = `bitrix24-docs://docs/${entry.slug}`;
    const resourceName = `bitrix24-doc-${entry.slug}`;

    mcpServer.resource(
      resourceName,
      resourceUri,
      {
        title: entry.title ?? entry.slug,
        description: `Документация Bitrix24. Исходный URL: ${entry.url}`,
        mimeType: 'text/markdown',
      },
      async () => {
        try {
          const markdown = await docsIndex.getMarkdown(entry);
          return {
            contents: [
              {
                uri: resourceUri,
                mimeType: 'text/markdown',
                text: formatDocument(entry, markdown),
              },
            ],
          };
        } catch (error) {
          const message = error instanceof Error ? error.message : String(error);
          return {
            contents: [
              {
                uri: resourceUri,
                mimeType: 'text/plain',
                text: `Ошибка чтения ресурса: ${message}`,
              },
            ],
          };
        }
      },
    );
  }

  return mcpServer;
}

async function startStdioServer(docsIndex: BitrixDocsIndex, indexPath: string): Promise<void> {
  const mcpServer = createMcpServer(docsIndex);
  const transport = new StdioServerTransport();
  await mcpServer.connect(transport);
  // eslint-disable-next-line no-console
  console.log(
    `Bitrix24 MCP сервер (stdio) запущен. Индекс: ${indexPath}. Экспортировано ресурсов: ${docsIndex.getEntries().length}`,
  );
}

async function startHttpServer(docsIndex: BitrixDocsIndex, indexPath: string): Promise<void> {
  const app = express();
  app.use(express.json({ limit: '10mb' }));
  app.use(cors());

  const pathPrefix = process.env.BITRIX24_MCP_HTTP_PATH ?? '/mcp';
  const port = Number.parseInt(process.env.BITRIX24_MCP_HTTP_PORT ?? '8000', 10);

  app.post(pathPrefix, async (req, res) => {
    const server = createMcpServer(docsIndex);
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

  app.all(pathPrefix, (req, res) => {
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
      `Bitrix24 MCP сервер (HTTP) запущен на порту ${port}, путь ${pathPrefix}. Индекс: ${indexPath}. Ресурсов: ${docsIndex.getEntries().length}`,
    );
  });
}

if (process.env.NODE_ENV !== 'test') {
  createServer().catch((error) => {
    console.error('Критическая ошибка сервера:', error);
    process.exit(1);
  });
}
