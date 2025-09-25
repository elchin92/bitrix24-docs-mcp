# Парсинг и индексация

Каталог для утилит на Python, которые скачивают, очищают и индексируют документацию Bitrix24.

Предполагаемые компоненты:
- `fetch_docs.py` — загрузка HTML-страниц Bitrix24 (с учётом robots.txt и лимитов).
- `normalize.py` — очистка разметки, конвертация в Markdown/JSON.
- `build_index.py` — построение полнотекстового или векторного индекса.

Результаты работы скриптов должны сохраняться в каталоге `data/`. При реализации важно документировать параметры и формат выходных файлов. Зависимости будут описаны в `pyproject.toml`.

## Установка окружения

```bash
cd scripts
python -m venv .venv
source .venv/bin/activate  # или .venv\Scripts\activate в Windows
pip install -e .[dev]
```

После установки можно запускать CLI-команды, которые будут добавлены в модуль `bitrix24_docs_etl`.

## Проверка доступности источника

```bash
bitrix24-docs check --log INFO
```

Команда выводит статус соединения с `https://apidocs.bitrix24.ru/` и проверяет `robots.txt`. Флаг `--json` возвращает результат в JSON, `--save` сохраняет robots.txt в файл.

## Обход и выгрузка страниц

```bash
bitrix24-docs crawl --max-pages 50 --max-depth 2 --save --manifest ../data/raw/manifest.json
```

Параметры:
- `--max-pages` — ограничение на количество страниц.
- `--max-depth` — глубина обхода ссылок (0 — только стартовая страница).
- `--save` — сохраняет HTML и метаданные в `data/raw/`.
- `--manifest` — путь для JSON с описанием сохранённых страниц.
- `--json` — выводит список найденных страниц без сохранения файлов.

## Нормализация HTML → Markdown

```bash
bitrix24-docs normalize --limit 20
```

Команда читает HTML из `data/raw/` и создаёт Markdown-версии в `data/processed/markdown/` вместе с метаданными в `data/processed/meta/`. Флаг `--force` пересоздаёт уже существующие записи.

## Построение базового индекса

```bash
bitrix24-docs index
```

Создаёт файл `data/index/simple_index.json` со сводной информацией по нормализованным документам. Параметр `--limit` ограничивает количество записей, попадающих в индекс.

## Запуск полного пайплайна

```bash
bitrix24-docs pipeline --max-pages 150 --max-depth 3
```

Команда последовательно выполняет `crawl`, `normalize` и `index`. Опциональные флаги `--skip-*` позволяют выключать этапы, `--normalize-force` пересоздаёт Markdown, `--index-limit` ограничивает итоговый список. Manifest по умолчанию сохраняется в `data/raw/manifest.json`.
