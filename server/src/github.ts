import { Buffer } from 'node:buffer';

export interface GithubSearchResult {
  title: string;
  path: string;
  htmlUrl: string;
  snippet: string;
  score: number;
}

export interface GithubDocument {
  title: string;
  path: string;
  htmlUrl: string;
  content: string;
}

const DEFAULT_REPO = process.env.BITRIX24_GITHUB_REPO ?? 'bitrix24/b24restdocs';
const GITHUB_API_BASE = 'https://api.github.com';

function getHeaders(): HeadersInit {
  const headers: HeadersInit = {
    Accept: 'application/vnd.github+json',
    'User-Agent': 'bitrix24-mcp-server',
  };
  const token = process.env.BITRIX24_GITHUB_TOKEN;
  if (token) {
    headers.Authorization = `Bearer ${token}`;
  }
  return headers;
}

async function githubFetch(url: string): Promise<Response> {
  const response = await fetch(url, {
    headers: getHeaders(),
  });
  if (response.status === 403) {
    const details = await response.text();
    throw new Error(
      `GitHub API rate limit exceeded or access forbidden. Response: ${details}`,
    );
  }
  if (!response.ok) {
    const details = await response.text();
    throw new Error(`GitHub API error ${response.status}: ${details}`);
  }
  return response;
}

function buildSearchUrl(query: string, repo: string, perPage: number): string {
  const searchQuery = `${query} repo:${repo}`;
  const params = new URLSearchParams({ q: searchQuery, per_page: String(perPage) });
  return `${GITHUB_API_BASE}/search/code?${params.toString()}`;
}

function makeSnippet(content: string, query: string, limit = 200): string {
  const normalizedContent = content.replace(/\s+/g, ' ').trim();
  const tokens = query.toLowerCase().split(/\s+/).filter(Boolean);
  let index = -1;
  for (const token of tokens) {
    const candidate = normalizedContent.toLowerCase().indexOf(token);
    if (candidate >= 0) {
      index = candidate;
      break;
    }
  }
  if (index === -1) {
    return normalizedContent.slice(0, limit);
  }
  const start = Math.max(0, index - limit / 2);
  const end = Math.min(normalizedContent.length, start + limit);
  return normalizedContent.slice(start, end).trim();
}

export async function searchGithubDocs(
  query: string,
  limit = 5,
  repo: string = DEFAULT_REPO,
): Promise<GithubSearchResult[]> {
  const perPage = Math.min(Math.max(limit, 1), 20);
  const response = await githubFetch(buildSearchUrl(query, repo, perPage));
  const data = (await response.json()) as {
    items?: Array<{
      path: string;
      html_url: string;
      score: number;
      url: string;
      name: string;
    }>;
  };
  const items = data.items ?? [];
  const results: GithubSearchResult[] = [];
  for (const item of items.slice(0, limit)) {
    const file = await fetchGithubFile(item.path, repo);
    results.push({
      title: file.title,
      path: item.path,
      htmlUrl: file.htmlUrl,
      snippet: makeSnippet(file.content, query),
      score: item.score ?? 0,
    });
  }
  return results;
}

function normalizeIdentifier(identifier: string): { path: string; repo: string } {
  const repo = DEFAULT_REPO;
  if (identifier.startsWith('http')) {
    const githubPrefix = 'https://github.com/';
    const rawPrefix = 'https://raw.githubusercontent.com/';
    if (identifier.startsWith(rawPrefix)) {
      const parts = identifier.slice(rawPrefix.length).split('/');
      const repoName = `${parts[0]}/${parts[1]}`;
      const path = parts.slice(3).join('/');
      return { path, repo: repoName };
    }
    if (identifier.startsWith(githubPrefix)) {
      const rest = identifier.slice(githubPrefix.length);
      const parts = rest.split('/');
      if (parts.length > 4 && parts[2] === 'blob') {
        const repoName = `${parts[0]}/${parts[1]}`;
        const path = parts.slice(4).join('/');
        return { path, repo: repoName };
      }
    }
  }
  return { path: identifier.replace(/^\//, ''), repo };
}

export async function fetchGithubFile(
  path: string,
  repo: string = DEFAULT_REPO,
): Promise<GithubDocument> {
  const url = `${GITHUB_API_BASE}/repos/${repo}/contents/${path}`;
  const response = await githubFetch(url);
  const data = (await response.json()) as {
    content?: string;
    encoding?: string;
    html_url: string;
    path: string;
  };
  if (!data.content || data.encoding !== 'base64') {
    throw new Error(`Не удалось получить содержимое файла ${path}`);
  }
  const markdown = Buffer.from(data.content, 'base64').toString('utf8');
  const title = extractTitle(markdown, path);
  return {
    title,
    path: data.path,
    htmlUrl: data.html_url,
    content: markdown,
  };
}

export async function fetchGithubDocument(identifier: string): Promise<GithubDocument> {
  const { path, repo } = normalizeIdentifier(identifier);
  return fetchGithubFile(path, repo);
}

function extractTitle(markdown: string, fallback: string): string {
  for (const line of markdown.split('\n')) {
    if (line.startsWith('#')) {
      const title = line.replace(/^#+\s*/, '').trim();
      if (title) {
        return title;
      }
    }
  }
  return fallback;
}
