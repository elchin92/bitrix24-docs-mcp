"""Import documentation directly from the official Bitrix24 REST repo."""

from __future__ import annotations

import json
import subprocess
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

from .storage import (
    ProcessedDocumentMeta,
    persist_processed_document,
    PROCESSED_MARKDOWN_DIR,
    DATA_DIR,
)

GITHUB_REPO_DEFAULT = "https://github.com/bitrix24/b24restdocs"


@dataclass(slots=True)
class ImportStats:
    imported: int
    repo_url: str
    branch: str


def import_github_docs(
    repo_url: str = GITHUB_REPO_DEFAULT,
    branch: str = "main",
    include_paths: Iterable[str] | None = None,
) -> ImportStats:
    include_paths = tuple(include_paths or ("api-reference", "tutorials"))
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_path = Path(tmpdir)
        _clone_repo(repo_url, branch, repo_path)
        imported = _ingest_markdown(repo_path, repo_url, branch, include_paths)
    return ImportStats(imported=imported, repo_url=repo_url, branch=branch)


def _clone_repo(repo_url: str, branch: str, destination: Path) -> None:
    subprocess.run(
        [
            "git",
            "clone",
            "--depth",
            "1",
            "--branch",
            branch,
            repo_url,
            str(destination),
        ],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def _ingest_markdown(
    repo_path: Path,
    repo_url: str,
    branch: str,
    include_paths: Iterable[str],
) -> int:
    timestamp = datetime.now(timezone.utc).isoformat()
    imported = 0
    for include in include_paths:
        target_dir = repo_path / include
        if not target_dir.exists():
            continue
        for md_file in target_dir.rglob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            relative = md_file.relative_to(repo_path)
            slug = _slug_from_path(relative)
            markdown_path = PROCESSED_MARKDOWN_DIR / f"{slug}.md"
            markdown_path.parent.mkdir(parents=True, exist_ok=True)
            markdown_path.write_text(content, encoding="utf-8")
            text_preview = _make_preview(content)
            meta = ProcessedDocumentMeta(
                url=f"{repo_url.rstrip('/')}/blob/{branch}/{relative.as_posix()}",
                title=_extract_title(content, slug),
                slug=slug,
                markdown=content,
                text=text_preview,
                html_path=markdown_path,
                retrieved_at=timestamp,
                links=[],
            )
            persist_processed_document(meta, force=True)
            imported += 1
    return imported


def _slug_from_path(path: Path) -> str:
    return path.with_suffix("").as_posix().replace("/", "_").replace(".", "_")


def _make_preview(markdown: str, limit: int = 400) -> str:
    stripped = markdown.replace("#", " ")
    stripped = stripped.replace("*", " ")
    stripped = " ".join(stripped.split())
    return stripped[:limit]


def _extract_title(markdown: str, fallback: str) -> str:
    for line in markdown.splitlines():
        if line.startswith("#"):
            return line.lstrip("# ").strip() or fallback
    return fallback
