import { describe, expect, it, vi } from 'vitest';
import type { Mock } from 'vitest';

vi.mock('./github.js', () => ({
  searchGithubDocs: vi.fn(),
  fetchGithubDocument: vi.fn(),
}));

import { createMcpServer } from './index.js';
import { searchGithubDocs, fetchGithubDocument } from './github.js';

describe('createMcpServer tools', () => {
  it('calls searchGithubDocs and formats the response', async () => {
    (searchGithubDocs as unknown as Mock).mockResolvedValue([
      {
        title: 'Документ 1',
        path: 'api/doc1.md',
        htmlUrl: 'https://github.com/path/doc1',
        snippet: 'Сниппет 1',
        score: 10,
      },
    ]);

    const server = createMcpServer();
    const tool = (server as any)._registeredTools?.bitrix_docs_search;
    expect(tool).toBeDefined();

    const result = await tool.callback({ query: 'catalog', limit: 1 }, {});

    expect(searchGithubDocs).toHaveBeenCalledWith('catalog', 1, expect.any(String));
    expect(result.content[0].text).toContain('Документ 1');
    expect(result.content[0].text).toContain('https://github.com/path/doc1');
  });

  it('fetches document content via fetchGithubDocument', async () => {
    (fetchGithubDocument as unknown as Mock).mockResolvedValue({
      title: 'Документ',
      path: 'api/doc.md',
      htmlUrl: 'https://github.com/path/doc',
      content: '# Заголовок\nТекст',
    });

    const server = createMcpServer();
    const tool = (server as any)._registeredTools?.bitrix_docs_fetch;
    expect(tool).toBeDefined();

    const result = await tool.callback({ slug: 'api/doc.md' }, {});

    expect(fetchGithubDocument).toHaveBeenCalledWith('api/doc.md');
    expect(result.content[0].text).toContain('# Заголовок');
    expect(result.content[0].text).toContain('https://github.com/path/doc');
  });
});
