#!/usr/bin/env bash
set -euo pipefail

cd /app

# allow skipping pipeline if data already mounted
if [[ "${BITRIX24_SKIP_PIPELINE:-false}" != "true" ]]; then
  echo "[entrypoint] Running Bitrix24 documentation pipeline..."
  PIPELINE_ARGS=(
    --max-pages "${BITRIX24_PIPELINE_MAX_PAGES:-200}"
    --max-depth "${BITRIX24_PIPELINE_MAX_DEPTH:-3}"
  )
  if [[ "${BITRIX24_PIPELINE_SKIP_NORMALIZE:-false}" == "true" ]]; then
    PIPELINE_ARGS+=(--skip-normalize)
  fi
  if [[ "${BITRIX24_PIPELINE_SKIP_INDEX:-false}" == "true" ]]; then
    PIPELINE_ARGS+=(--skip-index)
  fi
  if [[ "${BITRIX24_PIPELINE_SKIP_CRAWL:-false}" == "true" ]]; then
    PIPELINE_ARGS+=(--skip-crawl)
  fi
  if [[ -n "${BITRIX24_PIPELINE_NORMALIZE_LIMIT:-}" ]]; then
    PIPELINE_ARGS+=(--normalize-limit "${BITRIX24_PIPELINE_NORMALIZE_LIMIT}")
  fi
  bitrix24-docs pipeline "${PIPELINE_ARGS[@]}"
else
  echo "[entrypoint] Skipping pipeline as requested (BITRIX24_SKIP_PIPELINE=true)"
fi

INDEX_PATH=${BITRIX24_MCP_INDEX_PATH:-/app/data/index/simple_index.json}

if [[ ! -f "$INDEX_PATH" ]]; then
  echo "[entrypoint] Индекс не найден по пути $INDEX_PATH"
  echo "[entrypoint] Завершение работы. Проверьте параметры pipeline или смонтируйте готовый индекс."
  exit 1
fi

cd /app/server

if [[ "${BITRIX24_SKIP_BUILD:-false}" != "true" ]]; then
  echo "[entrypoint] Building TypeScript server..."
  npm run build >/dev/null 2>&1 || npm run build
else
  echo "[entrypoint] Пропуск сборки (BITRIX24_SKIP_BUILD=true)"
fi

echo "[entrypoint] Запуск MCP сервера..."
BITRIX24_MCP_INDEX_PATH="$INDEX_PATH" node dist/index.js
