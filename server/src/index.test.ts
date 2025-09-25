import { describe, expect, it } from 'vitest';

import { createMcpServer } from './index.js';

describe('createMcpServer', () => {
  const sampleDocs = [
    {
      slug: 'crm_lead',
      url: 'https://apidocs.bitrix24.ru/crm_lead',
      title: 'CRM Lead',
      markdown_path: 'processed/markdown/crm_lead.md',
      retrieved_at: '2025-01-01T00:00:00Z',
      text_preview: 'lead preview',
    },
    {
      slug: 'crm_deal',
      url: 'https://apidocs.bitrix24.ru/crm_deal',
      title: 'CRM Deal',
      markdown_path: 'processed/markdown/crm_deal.md',
      retrieved_at: '2025-01-01T00:00:00Z',
      text_preview: 'deal preview',
    },
  ];

  const stubIndex = {
    getEntries: () => sampleDocs,
    search: () => [],
    getMarkdown: async () => '# mock',
    getBySlugOrUrl: () => sampleDocs[0],
  } as const;

  it('registers resources for each document entry', () => {
    const server = createMcpServer(stubIndex);
    const registeredResources = Object.keys((server as any)._registeredResources ?? {});

    expect(registeredResources).toContain('bitrix24-docs://docs/crm_lead');
    expect(registeredResources).toContain('bitrix24-docs://docs/crm_deal');
  });
});
