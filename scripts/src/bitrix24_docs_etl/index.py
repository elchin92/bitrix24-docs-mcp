"""Построение упрощённого поискового индекса."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from .storage import DATA_DIR, INDEX_DIR, load_processed_documents

INDEX_FILE = INDEX_DIR / "simple_index.json"


@dataclass(slots=True)
class IndexStats:
    documents: int
    output_path: Path


def build_simple_index(limit: int | None = None) -> IndexStats:
    docs: list[dict[str, object]] = []
    for idx, doc in enumerate(load_processed_documents()):
        if limit is not None and idx >= limit:
            break
        docs.append(
            {
                "slug": doc.slug,
                "url": doc.url,
                "title": doc.title,
                "text_preview": doc.text_preview,
                "markdown_path": str(doc.markdown_path.relative_to(DATA_DIR)),
                "retrieved_at": doc.retrieved_at,
            }
        )
    INDEX_FILE.parent.mkdir(parents=True, exist_ok=True)
    INDEX_FILE.write_text(json.dumps(docs, ensure_ascii=False, indent=2), encoding="utf-8")
    return IndexStats(documents=len(docs), output_path=INDEX_FILE)
