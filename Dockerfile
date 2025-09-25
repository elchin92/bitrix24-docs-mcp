# Container for Bitrix24 Documentation MCP Server
FROM node:20-bullseye

# Install Python tooling for ETL scripts
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Pre-copy manifests to leverage Docker layer caching
COPY server/package.json server/package-lock.json ./server/
COPY scripts/pyproject.toml ./scripts/
COPY scripts/src ./scripts/src

# Install Python dependencies (exposes `bitrix24-docs` CLI)
RUN pip3 install --no-cache-dir ./scripts

# Install Node dependencies for the MCP server
RUN cd server && npm ci

# Copy repository contents
COPY . .

# Ensure entrypoint is executable
RUN chmod +x docker/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/app/docker/entrypoint.sh"]
