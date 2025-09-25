"""CLI для управления процессом ETL документации Bitrix24."""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Optional

import click
from rich.console import Console
from rich.table import Table

from . import fetch

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


def main() -> None:
    cli()


if __name__ == "__main__":  # pragma: no cover
    main()
