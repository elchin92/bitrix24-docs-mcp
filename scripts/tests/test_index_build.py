import json
from pathlib import Path

import bitrix24_docs_etl.storage as storage
from bitrix24_docs_etl.index import build_simple_index


def write_processed(slug: str, title: str, content: str) -> None:
    storage.PROCESSED_MARKDOWN_DIR.mkdir(parents=True, exist_ok=True)
    storage.PROCESSED_META_DIR.mkdir(parents=True, exist_ok=True)
    markdown_path = storage.PROCESSED_MARKDOWN_DIR / f"{slug}.md"
    meta_path = storage.PROCESSED_META_DIR / f"{slug}.json"
    markdown_path.write_text(content, encoding="utf-8")
    meta_payload = {
        "url": f"https://apidocs.bitrix24.ru/{slug}",
        "title": title,
        "slug": slug,
        "links": [],
        "retrieved_at": "2025-01-01T00:00:00Z",
        "markdown_path": str(markdown_path.relative_to(storage.DATA_DIR)),
        "html_path": "raw/index.html",
        "text_preview": content[:100],
    }
    meta_path.write_text(json.dumps(meta_payload, ensure_ascii=False), encoding="utf-8")


def test_build_simple_index_generates_expected_entries(tmp_path):
    write_processed("crm_lead", "CRM Lead", "Lead documentation body")
    write_processed("crm_deal", "CRM Deal", "Deal documentation body")

    stats = build_simple_index()
    index_path = stats.output_path

    assert index_path.exists()
    index_data = json.loads(index_path.read_text(encoding="utf-8"))

    assert len(index_data) == 2
    assert {entry["slug"] for entry in index_data} == {"crm_lead", "crm_deal"}
    for entry in index_data:
        assert entry["markdown_path"].startswith("processed/markdown/"), "Markdown path should be relative"
