# Сервер MCP (в разработке)

Здесь будет реализован локальный MCP-сервер на TypeScript для работы с документацией Bitrix24. Планируемая структура:

- `src/` — исходный код сервера на SDK MCP для TypeScript.
- `package.json`/`tsconfig.json` — метаданные проекта и зависимости.
- `tests/` — автотесты на корректность обработки запросов MCP (пока не созданы).
- `dist/` — результирующие JavaScript-файлы после сборки (`npm run build`).

Транспорт на первом этапе — `stdio` (для локального прототипа). На следующих итерациях добавим поддержку `http` для публичного размещения. При реализации следует строго следовать спецификации MCP (`doc/Specification.md`).

Сервер экспортирует документацию как MCP-ресурсы (`bitrix24-docs://docs/<slug>`), чтобы клиенты могли использовать стандартные операции `resources/list` и `resources/read`.

## Установка зависимостей

```bash
cd server
npm install
```

### Основные скрипты

- `npm run build` — компиляция TypeScript в `dist/`.
- `npm run dev` — запуск сервера в режиме hot-reload (использует `tsx`).
- `npm run start` — запуск собранной версии (`dist/index.js`).
- `npm run lint` / `npm run format` — статический анализ и проверка форматирования.
- `npm run test -- --run` — unit-тесты (Vitest).

## Зависимость от данных

Сервер читает индекс документации (`data/index/simple_index.json` по умолчанию). Перед запуском необходимо сформировать данные через Python-утилиты:

```bash
bitrix24-docs crawl --save
bitrix24-docs normalize
bitrix24-docs index
```

Путь к индексу можно переопределить переменной окружения `BITRIX24_MCP_INDEX_PATH`.

## Режимы запуска

- `BITRIX24_MCP_TRANSPORT=stdio` — запуск по умолчанию, взаимодействие через stdin/stdout.
- `BITRIX24_MCP_TRANSPORT=http` — сервер будет слушать HTTP-запросы (по умолчанию порт `8000`, путь `/mcp`). Дополнительно можно настроить `BITRIX24_MCP_HTTP_PORT` и `BITRIX24_MCP_HTTP_PATH`.

Пример запуска HTTP-режима:

```bash
BITRIX24_MCP_TRANSPORT=http \
BITRIX24_MCP_HTTP_PORT=8080 \
BITRIX24_MCP_INDEX_PATH=../data/index/simple_index.json \
npm run start
```
