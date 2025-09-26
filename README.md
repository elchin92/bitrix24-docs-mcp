# Bitrix24 Documentation MCP Server (WIP)

Проект предоставляет MCP-сервер, который в реальном времени обращается к документации Bitrix24 REST API в публичном репозитории [`bitrix24/b24restdocs`](https://github.com/bitrix24/b24restdocs). Цель — повторить подход [Microsoft Learn MCP Server](https://github.com/MicrosoftDocs/mcp), но для Bitrix24, чтобы любой разработчик мог подключить актуальные материалы к своим ИИ-агентам и IDE.

> **Статус:** TypeScript-сервер работает поверх GitHub API (инструменты `bitrix_docs_search` и `bitrix_docs_fetch`), добавлены базовые автотесты и пример конфигурации Codex. В каталоге `scripts/` хранится опциональный ETL для локального кэша и индексации.

## Ключевые возможности

- Поиск по документации Bitrix24 через GitHub Code Search без предварительного скачивания всего сайта.
- Получение полного Markdown-файла по slug или GitHub URL.
- Поддержка двух транспортов: STDIO (для локальных инструментов) и Streamable HTTP (для будущего публичного размещения).
- Персонализируемый источник (`BITRIX24_GITHUB_REPO`) и поддержка GitHub токена (`BITRIX24_GITHUB_TOKEN`) для обхода лимитов.
- Python-утилиты для офлайн-режима и построения пользовательских индексов.

## Материалы по MCP

Каталог `doc/` служит внутренним справочником и не предназначен для конечных пользователей. Перед публичным релизом он будет вынесен/очищен.

- `doc/Documentation.md` — обзор протокола.
- `doc/Specification.md` — формальные требования (JSON-RPC, инструменты, ресурсы).
- `doc/Schema_Reference.md` — схемы типов.
- `doc/Community.md` — best practices.

## Структура репозитория

```
.
├── doc/                # временные справочные материалы MCP
├── server/             # исходники MCP-сервера (TypeScript)
├── scripts/            # Python-утилиты ETL и индексатор
├── docker/             # docker-контексты и entrypoint
└── README.md
```

## Запуск MCP-сервера

```bash
cd server
npm install
npm run build
BITRIX24_GITHUB_REPO="bitrix24/b24restdocs" \
BITRIX24_GITHUB_TOKEN="ghp_..." \  # опционально, но уменьшает риск rate limit
npm run start
```

Переменные окружения:

- `BITRIX24_GITHUB_REPO` — репозиторий, откуда читается документация (по умолчанию `bitrix24/b24restdocs`).
- `BITRIX24_GITHUB_TOKEN` — персональный токен GitHub (scope `public_repo`), повышает лимит запросов с 60 до 5 000 в час.
- `BITRIX24_MCP_TRANSPORT` — `stdio` (по умолчанию) или `http`.
- `BITRIX24_MCP_HTTP_PORT`, `BITRIX24_MCP_HTTP_PATH` — настройки HTTP-транспорта.

Пример вызова инструмента через MCP Inspector:

```json
{
  "name": "bitrix_docs_search",
  "arguments": { "query": "CRM сделки", "limit": 3 }
}
```

Ответ содержит заголовок, путь в репозитории, GitHub URL и сниппет. Полный текст доступен через `bitrix_docs_fetch`.

## Конфигурация Codex CLI (`~/.codex/config.toml`)

```toml
[mcp_servers.bitrix24_docs_local]
command = "node"
args = ["/srv/mcp/bitrix24/server/dist/index.js"]

[mcp_servers.bitrix24_docs_local.env]
BITRIX24_MCP_TRANSPORT = "stdio"
BITRIX24_GITHUB_REPO = "bitrix24/b24restdocs"
# BITRIX24_GITHUB_TOKEN = "ghp_xxxxx"  # задайте, чтобы избежать rate limit GitHub
```

После перезапуска Codex можно запрашивать документы напрямую, например:

```json
{
  "name": "bitrix_docs_fetch",
  "arguments": {
    "url": "https://github.com/bitrix24/b24restdocs/blob/master/api-reference/crm/deal/index.md"
  }
}
```

Сервер вернёт заголовок, ссылку и весь Markdown-документ.

## Офлайн ETL (по желанию)

Каталог `scripts/` содержит утилиты для случаев, когда нужен локальный кэш или собственный индекс:

```bash
cd scripts
python3 -m venv .venv
source .venv/bin/activate
pip install -e .[dev]

# Проверить доступность источников
bitrix24-docs check --json

# Быстрый импорт Markdown из GitHub (без поиска)
bitrix24-docs import-github --repo https://github.com/bitrix24/b24restdocs --branch master

# Сконструировать простой индекс по локальному кэшу
bitrix24-docs index
```

Все артефакты записываются в `scripts/data/` (каталог исключён из git).

## Тестирование

- **Node.js**
  ```bash
  cd server
  npm install
  npm run build
  npm run test -- --run
  ```
- **Python**
  ```bash
  cd scripts
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -e .[dev]
  PYTHONPATH=src pytest
  ```

CI (см. `.github/workflows/ci.yml`) запускает оба набора тестов при push и PR.

## Планы и TODO

- Кэширование ответов GitHub и обработка rate limit без ошибок.
- Интеграционные тесты MCP с моками GitHub API.
- Документация на английском и примеры для VS Code/Claude.
- Расширенный HTTP-режим: авторизация, rate limiting, логирование.
- Удаление временной папки `doc/` в публичной версии.

## Как участвовать

- Создавайте issues и PR с предложениями улучшений.
- Соблюдайте рекомендации `doc/Community.md` при общении.
- Обсуждайте значимые архитектурные изменения в GitHub Discussions.

Лицензия будет определена перед первым релизом (в package.json указана MIT как базовый вариант).
