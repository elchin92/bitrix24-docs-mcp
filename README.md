# Bitrix24 Documentation MCP Server (WIP)

Проект нацелен на создание удалённого MCP-сервера, который по запросу ИИ-клиентов возвращает свежую документацию по Bitrix24 REST API. Репозиторий будет публичным, чтобы разработчики могли легко подключать сервер к своим агентам и IDE, аналогично тому, как работает [Microsoft Learn MCP Server](https://github.com/MicrosoftDocs/mcp).

> **Статус:** подготовлен локальный ETL-пайплайн (Python) и прототип MCP-сервера (TypeScript), следующий этап — тесты и подготовка публичного размещения.

## Цели

- Собирать и нормализовать публичную документацию с `https://apidocs.bitrix24.ru/`.
- Предоставлять MCP-инструмент для семантического/полнотекстового поиска по документации.
- Давать возможность запрашивать полный текст документа по URL.
- Подготовить публичный HTTP-endpoint, пригодный для использования в Copilot/Claude/VS Code (на следующем этапе после локального прототипа).

## Документы по MCP

Каталог `doc/` хранит вспомогательные материалы по MCP, которые используются во время разработки и не предназначены для конечных пользователей репозитория. Он будет очищен или вынесен в отдельный архив перед публичным релизом.

- `doc/Documentation.md` — базовые понятия и архитектура MCP.
- `doc/Specification.md` — формальные требования и протокол.
- `doc/Schema_Reference.md` — описание доступных типов и схем.
- `doc/Community.md` — рекомендации по коммуникациям и взаимодействию сообщества.

## Структура репозитория

```
.
├── doc/                # Официальная документация MCP (для справки)
├── server/             # Исходный код MCP-сервера (TypeScript)
├── scripts/            # Утилиты для парсинга и индексации (Python)
├── data/               # Сырые и обработанные данные документации (в .gitignore)
└── README.md           # Текущий файл
```

Каталоги `server/`, `scripts/` и `data/` будут заполнены в последующих шагах.

## План работ

1. **Парсер документации** — реализовано: Python-CLI загружает HTML и сохраняет метаданные.
2. **Индекс поиска** — реализовано: сборка базового JSON-индекса; исследуем переход на полнотекстовый/векторный.
3. **MCP-сервер** — реализовано: локальный сервер на TypeScript с инструментами `bitrix_docs_search`, `bitrix_docs_fetch` и экспортом документов в виде MCP-ресурсов.
4. **Тестирование** — в работе: планируется покрыть скрипты и сервер автотестами, проверить через MCP Inspector.
5. **Публичный endpoint** — запланировано: хостинг, авторизация, безопасность, документация для пользователей.

## Быстрый старт

### 1. Подготовка Python-окружения

```bash
cd scripts
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .[dev]
```

### 2. Формирование индекса документации

```bash
bitrix24-docs check               # убедиться, что источник доступен
bitrix24-docs crawl --save        # сохранить HTML в data/raw
bitrix24-docs normalize           # конвертировать в Markdown
bitrix24-docs index               # создать data/index/simple_index.json
```

> Каталог `data/` не коммитится в git. При необходимости можно очистить его вручную.

### 3. Сборка и запуск MCP-сервера

```bash
cd ../server
npm install
npm run build
npm run start  # использует STDIO транспорт
```

По умолчанию сервер ищет индекс по пути `../data/index/simple_index.json`. Используйте переменную `BITRIX24_MCP_INDEX_PATH`, чтобы указать альтернативный файл.

#### Режимы транспорта

- `BITRIX24_MCP_TRANSPORT=stdio` — режим по умолчанию, взаимодействие через стандартные потоки.
- `BITRIX24_MCP_TRANSPORT=http` — поднимает HTTP-эндпоинт со [Streamable HTTP](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#streamable-http`). Дополнительные переменные:
  - `BITRIX24_MCP_HTTP_PORT` (по умолчанию `8000`).
  - `BITRIX24_MCP_HTTP_PATH` (по умолчанию `/mcp`).

Пример запуска HTTP-сервера:

```bash
BITRIX24_MCP_TRANSPORT=http \
BITRIX24_MCP_HTTP_PORT=8080 \
BITRIX24_MCP_INDEX_PATH=../data/index/simple_index.json \
npm run start
```

### 4. Подключение к MCP Inspector/IDE

Пример конфигурации для MCP Inspector или VS Code:

```json
{
  "bitrix24-docs": {
    "command": "node",
    "args": ["/path/to/repo/server/dist/index.js"],
    "transport": "stdio"
  }
}
```

Рекомендуется задать системный промпт, напоминающий модели использовать инструменты `bitrix_docs_search` и `bitrix_docs_fetch` при работе с Bitrix24.

### 5. Работа с ресурсами

Сервер автоматически публикует документы как ресурсы с URI вида `bitrix24-docs://docs/<slug>`. Их можно просматривать через `resources/list` и `resources/read`, что соответствует рекомендациям из `doc/Specification.md` по экспонированию контента в виде ресурсов.

### 6. Docker

```bash
docker build -t bitrix24-mcp .
docker run --rm \
  -p 8000:8000 \
  -e BITRIX24_MCP_TRANSPORT=http \
  bitrix24-mcp
```

Контейнер при запуске прогоняет ETL-пайплайн (`bitrix24-docs pipeline`), формирует индекс в `/app/data/index/` и поднимает HTTP-эндпоинт на порту `8000`. Для повторного запуска с уже подготовленными данными можно смонтировать volume или установить `BITRIX24_SKIP_PIPELINE=true`.
Дополнительные переменные окружения:

- `BITRIX24_PIPELINE_MAX_PAGES`, `BITRIX24_PIPELINE_MAX_DEPTH` — управление глубиной обхода.
- `BITRIX24_SKIP_BUILD=true` — пропустить сборку TypeScript (если `dist/` смонтирован заранее).

## Тестирование

- Python ETL:

  ```bash
  cd scripts
  python -m venv .venv
  source .venv/bin/activate
  pip install -e .[dev]
  PYTHONPATH=src pytest
  ```

- MCP сервер (Node.js):

  ```bash
  cd server
  npm install
  npm run build
  npm run test -- --run
  ```

CI-конвейер (`.github/workflows/ci.yml`) прогоняет оба набора тестов при каждом push/PR.

## Следующие шаги

- расширить покрытие автотестами для ETL и MCP (базовые тесты и CI уже подключены);
- проработать требования безопасности (хранение ключей, rate limiting, логирование);
- доработать HTTP-режим (аутентификация, rate limiting) и подготовить документацию на английском для широкой аудитории;
- вынести вспомогательную папку `doc/` из релизной версии репозитория.

## Как участвовать

- Предлагайте идеи и улучшения через issues/PR.
- Следуйте рекомендациям из `doc/Community.md`.
- При необходимости создавайте обсуждения (GitHub Discussions) для архитектурных решений.

## Лицензия

Лицензия будет определена после подготовки первой рабочей версии сервера.
