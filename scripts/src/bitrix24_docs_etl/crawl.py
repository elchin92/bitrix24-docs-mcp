"""Обход документации Bitrix24 для составления списка страниц."""

from __future__ import annotations

import asyncio
import logging
from collections import deque
from dataclasses import dataclass
from typing import Iterable, Optional

from .fetch import BASE_URL, BitrixDocumentationFetcher, FetchResult

LOGGER = logging.getLogger(__name__)


@dataclass(slots=True)
class PageSummary:
    url: str
    title: Optional[str]
    links: tuple[str, ...]


@dataclass(slots=True)
class CrawlResult:
    pages: dict[str, PageSummary]
    raw_pages: dict[str, FetchResult]

    def to_manifest(self) -> list[dict[str, object]]:
        return [
            {
                "url": page.url,
                "title": page.title,
                "links": list(page.links),
            }
            for page in self.pages.values()
        ]

    def iter_fetch_results(self) -> Iterable[FetchResult]:
        return self.raw_pages.values()


class BitrixCrawler:
    """Простой очередной обход страниц Bitrix24."""

    def __init__(
        self,
        base_url: str = BASE_URL,
        max_pages: int = 200,
        max_depth: int = 3,
        delay: float = 0.0,
    ) -> None:
        self.base_url = base_url
        self.max_pages = max_pages
        self.max_depth = max_depth
        self.delay = delay

    async def crawl(self, start_paths: Iterable[str | None]) -> CrawlResult:
        fetcher = BitrixDocumentationFetcher(self.base_url)
        visited: set[str] = set()
        pages: dict[str, PageSummary] = {}
        raw_pages: dict[str, FetchResult] = {}
        queue: deque[tuple[str | None, int]] = deque((path, 0) for path in start_paths)

        try:
            while queue and len(visited) < self.max_pages:
                path, depth = queue.popleft()
                key = self._normalize_key(path)
                if key in visited:
                    continue
                try:
                    result = await fetcher.fetch(path)
                except Exception:  # noqa: BLE001
                    LOGGER.exception("Не удалось загрузить %s", path or self.base_url)
                    visited.add(key)
                    continue

                visited.add(key)
                pages[result.url] = PageSummary(result.url, result.title, result.links)
                raw_pages[result.url] = result
                LOGGER.debug("Страница %s: найдено ссылок %d", result.url, len(result.links))

                if depth < self.max_depth:
                    for link in result.links:
                        if link.startswith(self.base_url):
                            queue.append((link, depth + 1))
                if self.delay:
                    await asyncio.sleep(self.delay)
        finally:
            await fetcher.aclose()

        return CrawlResult(pages, raw_pages)

    def _normalize_key(self, path: str | None) -> str:
        if path is None:
            return self.base_url
        if isinstance(path, str) and path.startswith("http"):
            return path
        return f"{self.base_url.rstrip('/')}/{path.lstrip('/')}"


async def collect_default(max_pages: int = 200) -> CrawlResult:
    crawler = BitrixCrawler(max_pages=max_pages)
    return await crawler.crawl([None])
