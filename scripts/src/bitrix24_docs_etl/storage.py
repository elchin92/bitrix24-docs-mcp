"""Хранение выгруженных документов Bitrix24."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable
from urllib.parse import urlparse

from .fetch import FetchResult

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
META_DIR = RAW_DIR / "meta"


def ensure_dirs() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    META_DIR.mkdir(parents=True, exist_ok=True)


def persist_fetch_results(results: Iterable[FetchResult]) -> list[dict[str, object]]:
    """Сохраняет HTML и метаданные, возвращает информацию о файлах."""

    ensure_dirs()
    stored: list[dict[str, object]] = []
    for result in results:
        slug = _slug_from_url(result.url)
        html_path = RAW_DIR / f"{slug}.html"
        meta_path = META_DIR / f"{slug}.json"

        html_path.write_text(result.content, encoding="utf-8")
        meta = {
            "url": result.url,
            "title": result.title,
            "links": list(result.links),
            "status_code": result.status_code,
            "retrieved_at": datetime.now(timezone.utc).isoformat(),
            "html_path": str(html_path.relative_to(DATA_DIR)),
        }
        meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
        stored.append(meta)
    return stored


def _slug_from_url(url: str) -> str:
    parsed = urlparse(url)
    path = parsed.path.lstrip("/") or "index"
    safe_path = path.replace("/", "_")
    if parsed.query:
        query_hash = hashlib.sha256(parsed.query.encode("utf-8")).hexdigest()[:8]
        safe_path += f"_{query_hash}"
    host = parsed.netloc.replace(".", "_")
    return f"{host}_{safe_path}"
