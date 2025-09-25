"""Хранение выгруженных документов Bitrix24."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Iterator
from urllib.parse import urlparse

from .fetch import FetchResult

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
RAW_META_DIR = RAW_DIR / "meta"
PROCESSED_DIR = DATA_DIR / "processed"
PROCESSED_MARKDOWN_DIR = PROCESSED_DIR / "markdown"
PROCESSED_META_DIR = PROCESSED_DIR / "meta"
INDEX_DIR = DATA_DIR / "index"


@dataclass(slots=True)
class RawDocument:
    slug: str
    url: str
    title: str | None
    html: str
    links: list[str]
    status_code: int
    retrieved_at: str
    html_path: Path
    meta_path: Path


@dataclass(slots=True)
class ProcessedDocumentMeta:
    url: str
    title: str | None
    slug: str
    markdown: str
    text: str
    html_path: Path
    retrieved_at: str
    links: list[str]


@dataclass(slots=True)
class ProcessedDocument:
    slug: str
    url: str
    title: str | None
    markdown_path: Path
    html_path: Path
    text_preview: str
    retrieved_at: str
    links: list[str]


def ensure_dirs() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    RAW_META_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_MARKDOWN_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_META_DIR.mkdir(parents=True, exist_ok=True)
    INDEX_DIR.mkdir(parents=True, exist_ok=True)


def persist_fetch_results(results: Iterable[FetchResult]) -> list[dict[str, object]]:
    """Сохраняет HTML и метаданные, возвращает информацию о файлах."""

    ensure_dirs()
    stored: list[dict[str, object]] = []
    for result in results:
        slug = _slug_from_url(result.url)
        html_path = RAW_DIR / f"{slug}.html"
        meta_path = RAW_META_DIR / f"{slug}.json"

        html_path.write_text(result.content, encoding="utf-8")
        meta = {
            "url": result.url,
            "title": result.title,
            "links": list(result.links),
            "status_code": result.status_code,
            "retrieved_at": datetime.now(timezone.utc).isoformat(),
            "html_path": str(html_path.relative_to(DATA_DIR)),
            "slug": slug,
        }
        meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
        stored.append(meta)
    return stored


def load_raw_documents() -> Iterator[RawDocument]:
    ensure_dirs()
    for meta_file in sorted(RAW_META_DIR.glob("*.json")):
        data = json.loads(meta_file.read_text(encoding="utf-8"))
        html_path = DATA_DIR / data["html_path"]
        if not html_path.exists():
            continue
        html_content = html_path.read_text(encoding="utf-8")
        slug = data.get("slug") or _slug_from_url(data["url"])
        yield RawDocument(
            slug=slug,
            url=data["url"],
            title=data.get("title"),
            html=html_content,
            links=list(data.get("links", [])),
            status_code=int(data.get("status_code", 0)),
            retrieved_at=str(data.get("retrieved_at", "")),
            html_path=html_path,
            meta_path=meta_file,
        )


def processed_document_exists(slug: str) -> bool:
    markdown_path = PROCESSED_MARKDOWN_DIR / f"{slug}.md"
    meta_path = PROCESSED_META_DIR / f"{slug}.json"
    return markdown_path.exists() and meta_path.exists()


def persist_processed_document(meta: ProcessedDocumentMeta, force: bool = False) -> None:
    ensure_dirs()
    markdown_path = PROCESSED_MARKDOWN_DIR / f"{meta.slug}.md"
    meta_path = PROCESSED_META_DIR / f"{meta.slug}.json"
    if not force and markdown_path.exists() and meta_path.exists():
        return
    markdown_path.write_text(meta.markdown, encoding="utf-8")
    meta_payload = {
        "url": meta.url,
        "title": meta.title,
        "slug": meta.slug,
        "links": meta.links,
        "retrieved_at": meta.retrieved_at,
        "markdown_path": str(markdown_path.relative_to(DATA_DIR)),
        "html_path": str(meta.html_path.relative_to(DATA_DIR)),
        "text_preview": meta.text[:400],
    }
    meta_path.write_text(json.dumps(meta_payload, ensure_ascii=False, indent=2), encoding="utf-8")


def load_processed_documents() -> Iterator[ProcessedDocument]:
    ensure_dirs()
    for meta_file in sorted(PROCESSED_META_DIR.glob("*.json")):
        data = json.loads(meta_file.read_text(encoding="utf-8"))
        markdown_path = DATA_DIR / data["markdown_path"]
        html_path = DATA_DIR / data["html_path"]
        if not markdown_path.exists():
            continue
        yield ProcessedDocument(
            slug=data["slug"],
            url=data["url"],
            title=data.get("title"),
            markdown_path=markdown_path,
            html_path=html_path,
            text_preview=data.get("text_preview", ""),
            retrieved_at=data.get("retrieved_at", ""),
            links=list(data.get("links", [])),
        )


def _slug_from_url(url: str) -> str:
    parsed = urlparse(url)
    path = parsed.path.lstrip("/") or "index"
    safe_path = path.replace("/", "_")
    if parsed.query:
        query_hash = hashlib.sha256(parsed.query.encode("utf-8")).hexdigest()[:8]
        safe_path += f"_{query_hash}"
    host = parsed.netloc.replace(".", "_")
    return f"{host}_{safe_path}"
