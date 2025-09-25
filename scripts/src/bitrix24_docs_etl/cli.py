"""CLI для управления процессом ETL документации Bitrix24."""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Optional

import asyncio
import click
from rich.console import Console
from rich.table import Table

from . import fetch
from .crawl import BitrixCrawler
from .index import build_simple_index
from .normalize import normalize_all
from .storage import persist_fetch_results

console = Console()
logger = logging.getLogger(__name__)


@click.group()
@click.option("--log", "log_level", default="INFO", help="Уровень логирования (DEBUG/INFO/WARNING)")
def cli(log_level: str) -> None:
    """Инструменты для загрузки и проверки документации Bitrix24."""

    logging.basicConfig(level=log_level.upper(), format="[%(levelname)s] %(message)s")


@cli.command("check")
@click.option("--json", "output_json", is_flag=True, help="Вывести результат в JSON")
@click.option("--save", type=click.Path(dir_okay=False, path_type=Path), help="Сохранить robots.txt в файл")
def check_command(output_json: bool, save: Optional[Path]) -> None:
    """Проверяет доступность основного раздела и robots.txt."""

    result = fetch.check_source_sync()
    if output_json:
        console.print_json(data=result)
    else:
        table = Table(title="Проверка источника Bitrix24")
        table.add_column("Метрика")
        table.add_column("Значение")
        table.add_row("reachable", str(result["reachable"]))
        table.add_row("robots_status", str(result["robots_status"]))
        table.add_row("title", str(result.get("title")))
        console.print(table)
    if save:
        content = result.get("robots_sample", "")
        save.write_text(content)
        console.print(f"[green]robots.txt сохранён в {save}")


@cli.command("crawl")
@click.option("--max-pages", default=100, show_default=True, help="Максимум страниц")
@click.option("--max-depth", default=2, show_default=True, help="Максимальная глубина обхода")
@click.option("--json", "output_json", is_flag=True, help="Выводить результат в JSON")
@click.option("--save", is_flag=True, help="Сохранить HTML и метаданные в data/raw")
@click.option("--manifest", type=click.Path(dir_okay=False, path_type=Path), help="Путь для сохранения manifest.json")
def crawl_command(max_pages: int, max_depth: int, output_json: bool, save: bool, manifest: Optional[Path]) -> None:
    """Собирает список страниц Bitrix24 с главной."""

    crawler = BitrixCrawler(max_pages=max_pages, max_depth=max_depth)
    result = asyncio.run(crawler.crawl([None]))
    stored_meta = []
    if save:
        stored_meta = persist_fetch_results(result.iter_fetch_results())
        console.print(f"[green]Сохранено страниц: {len(stored_meta)}")
        if manifest:
            manifest.parent.mkdir(parents=True, exist_ok=True)
            manifest.write_text(json.dumps(stored_meta, ensure_ascii=False, indent=2), encoding="utf-8")
        console.print(f"[green]Manifest записан в {manifest}")
    if output_json:
        console.print_json(data=result.to_manifest())
    else:
        table = Table(title="Найденные страницы", show_lines=False)
        table.add_column("#")
        table.add_column("URL")
        table.add_column("Заголовок")
        for idx, page in enumerate(result.pages.values(), start=1):
            table.add_row(str(idx), page.url, page.title or "—")
        console.print(table)
        console.print(f"[green]Всего страниц: {len(result.pages)}")


@cli.command("normalize")
@click.option("--limit", type=int, help="Ограничить количество документов")
@click.option("--force", is_flag=True, help="Пересоздать уже нормализованные файлы")
def normalize_command(limit: int | None, force: bool) -> None:
    """Конвертирует HTML из data/raw в Markdown и JSON."""

    stats = normalize_all(limit=limit, force=force)
    table = Table(title="Нормализация документации")
    table.add_column("Метрика")
    table.add_column("Значение")
    table.add_row("Всего рассмотрено", str(stats.total))
    table.add_row("Создано/обновлено", str(stats.processed))
    table.add_row("Пропущено", str(stats.skipped))
    console.print(table)


@cli.command("index")
@click.option("--limit", type=int, help="Ограничить количество документов в индексе")
def index_command(limit: int | None) -> None:
    """Строит простой JSON-индекс на основе нормализованных документов."""

    stats = build_simple_index(limit=limit)
    console.print(f"[green]Создан индекс с {stats.documents} документами: {stats.output_path}")


def main() -> None:
    cli()


if __name__ == "__main__":  # pragma: no cover
    main()
