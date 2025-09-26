import importlib

import pytest

import bitrix24_docs_etl.storage as storage
import bitrix24_docs_etl.index as index_module


@pytest.fixture(autouse=True)
def isolated_data_dir(tmp_path, monkeypatch):
    importlib.reload(storage)
    base = tmp_path
    monkeypatch.setattr("bitrix24_docs_etl.storage.DATA_DIR", base)
    monkeypatch.setattr("bitrix24_docs_etl.storage.RAW_DIR", base / "raw")
    monkeypatch.setattr("bitrix24_docs_etl.storage.RAW_META_DIR", base / "raw" / "meta")
    monkeypatch.setattr("bitrix24_docs_etl.storage.PROCESSED_DIR", base / "processed")
    monkeypatch.setattr("bitrix24_docs_etl.storage.PROCESSED_MARKDOWN_DIR", base / "processed" / "markdown")
    monkeypatch.setattr("bitrix24_docs_etl.storage.PROCESSED_META_DIR", base / "processed" / "meta")
    monkeypatch.setattr("bitrix24_docs_etl.storage.INDEX_DIR", base / "index")

    monkeypatch.setattr("bitrix24_docs_etl.index.DATA_DIR", base)
    monkeypatch.setattr("bitrix24_docs_etl.index.INDEX_DIR", base / "index")

    (base / "raw" / "meta").mkdir(parents=True, exist_ok=True)
    (base / "processed" / "markdown").mkdir(parents=True, exist_ok=True)
    (base / "processed" / "meta").mkdir(parents=True, exist_ok=True)
    (base / "index").mkdir(parents=True, exist_ok=True)

    yield
