"""Нормализация HTML-документов в Markdown и JSON."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator

from bs4 import BeautifulSoup
from markdownify import markdownify

from .storage import (
    load_raw_documents,
    persist_processed_document,
    processed_document_exists,
    ProcessedDocumentMeta,
)


@dataclass(slots=True)
class NormalizationStats:
    total: int
    processed: int
    skipped: int


def normalize_all(limit: int | None = None, force: bool = False) -> NormalizationStats:
    processed = 0
    skipped = 0

    for index, raw in enumerate(load_raw_documents()):
        if limit is not None and index >= limit:
            break
        if not force and processed_document_exists(raw.slug):
            skipped += 1
            continue
        markdown_content, text_content = _convert_html(raw.html)
        meta = ProcessedDocumentMeta(
            url=raw.url,
            title=raw.title,
            slug=raw.slug,
            markdown=markdown_content,
            text=text_content,
            html_path=raw.html_path,
            retrieved_at=raw.retrieved_at,
            links=raw.links,
        )
        persist_processed_document(meta, force=force)
        processed += 1
    total = processed + skipped
    return NormalizationStats(total=total, processed=processed, skipped=skipped)


def _convert_html(html: str) -> tuple[str, str]:
    soup = BeautifulSoup(html, "lxml")
    for tag in soup(["script", "style", "noscript", "nav", "footer", "header"]):
        tag.decompose()
    target = soup.find("main") or soup.body or soup
    markdown_text = markdownify(str(target), heading_style="ATX")
    text_content = target.get_text(" ", strip=True)
    return markdown_text.strip(), text_content
