"""Каркас загрузчика документации Bitrix24.

На первом этапе реализованы:
- Проверка доступности источника и robots.txt.
- Функции для загрузки HTML-страницы с таймаутами и базовой валидацией.

Дальнейшее развитие: обход линков, очистка, сохранение в data/processed.
"""

from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass
from typing import Optional
from urllib.parse import urljoin, urlparse

import httpx
from bs4 import BeautifulSoup

LOGGER = logging.getLogger(__name__)

BASE_URL = "https://apidocs.bitrix24.ru/"
ROBOTS_PATH = "robots.txt"
USER_AGENT = "Bitrix24-Docs-MCP/0.1 (+https://github.com/bitrix24/bitrix24-docs-mcp)"


@dataclass(slots=True)
class FetchResult:
    """Результат загрузки страницы."""

    url: str
    status_code: int
    content: str
    title: Optional[str] = None


class BitrixDocumentationFetcher:
    """Простой асинхронный загрузчик страниц Bitrix24."""

    def __init__(self, base_url: str = BASE_URL, timeout: float = 10.0) -> None:
        self.base_url = base_url.rstrip("/") + "/"
        self._client = httpx.AsyncClient(timeout=timeout, headers={
            "User-Agent": USER_AGENT
        })

    async def aclose(self) -> None:
        await self._client.aclose()

    async def fetch(self, path: str | None = None) -> FetchResult:
        url = self.base_url if path is None else urljoin(self.base_url, path)
        response = await self._client.get(url)
        response.raise_for_status()
        text = response.text
        title = _extract_title(text)
        return FetchResult(url=url, status_code=response.status_code, content=text, title=title)

    async def check_reachability(self) -> bool:
        try:
            result = await self.fetch()
            LOGGER.debug("Fetched %s with status %s", result.url, result.status_code)
            return True
        except (httpx.HTTPError, asyncio.TimeoutError) as exc:
            LOGGER.error("Ошибка при обращении к %s: %s", self.base_url, exc)
            return False

    async def fetch_robots(self) -> FetchResult:
        return await self.fetch(ROBOTS_PATH)


def _extract_title(html_text: str) -> Optional[str]:
    soup = BeautifulSoup(html_text, "lxml")
    if soup.title and soup.title.string:
        return soup.title.string.strip()
    h1 = soup.find("h1")
    if h1 and h1.text:
        return h1.text.strip()
    return None


def ensure_same_host(url: str, base: str = BASE_URL) -> bool:
    """Проверяет, что URL принадлежит домену Bitrix24 docs."""

    parsed = urlparse(url)
    base_parsed = urlparse(base)
    return parsed.netloc == base_parsed.netloc


async def check_source() -> dict[str, object]:
    """Асинхронная проверка доступности и соблюдения robots."""

    fetcher = BitrixDocumentationFetcher()
    try:
        is_reachable = await fetcher.check_reachability()
        robots = await fetcher.fetch_robots()
        return {
            "reachable": is_reachable,
            "robots_status": robots.status_code,
            "robots_sample": robots.content[:500],
            "title": robots.title,
        }
    finally:
        await fetcher.aclose()


def check_source_sync() -> dict[str, object]:
    """Синхронная обёртка для check_source()."""

    return asyncio.run(check_source())
