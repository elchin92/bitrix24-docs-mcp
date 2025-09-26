# Парсинг и индексация (опционально)

Каталог `scripts/` хранит Python-утилиты для сценариев, когда хочется локально закэшировать документацию Bitrix24 или построить собственный индекс (например, для офлайн-режима). Основной MCP-сервер теперь работает напрямую с GitHub (`bitrix24/b24restdocs`), поэтому запускать ETL не обязательно.

## Возможности CLI `bitrix24-docs`

- `check` — проверяет доступность `https://apidocs.bitrix24.ru/`, скачивает `robots.txt`.
- `crawl` — обходит сайт Bitrix24 и сохраняет HTML (используется по необходимости).
- `normalize` — переводит HTML в Markdown и JSON.
- `index` — строит простой JSON-индекс для локального поиска.
- `pipeline` — объединяет этапы `crawl → normalize → index`.
- `import-github` — быстро подтягивает готовые Markdown-файлы прямо из GitHub-репозитория документации (`bitrix24/b24restdocs` по умолчанию).

## Установка окружения

```bash
cd scripts
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .[dev]
```

## Примеры команд

```bash
# Проверка источника и сохранение robots.txt
bitrix24-docs check --json --save robots.txt

# Импорт Markdown из GitHub без обхода сайта
bitrix24-docs import-github --branch master

# Построение индекса по локальному кэшу
bitrix24-docs index
```

Все файлы складываются в `scripts/data/` и не попадают в git (см. `.gitignore`).

## Тестирование

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
PYTHONPATH=src pytest
```

Тесты используют временные каталоги, поэтому данные в `scripts/data/` не затрагиваются.
