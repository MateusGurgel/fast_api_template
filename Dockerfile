FROM python:3.10-slim AS builder

ENV POETRY_VERSION=2.1.3 \
    POETRY_HOME="/opt/poetry" \
    PATH="/opt/poetry/bin:$PATH" \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl build-essential \
 && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s "$POETRY_HOME/bin/poetry" /usr/local/bin/poetry

WORKDIR /app

COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.in-project true && \
    poetry install --no-interaction --no-root

COPY src ./src

FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH" \
    PYTHONPATH="/app/src"

WORKDIR /app

COPY --from=builder /app /app

EXPOSE 8000

CMD ["gunicorn", "fast_api_template.core.main:app", "-c", "src/fast_api_template/infra/gunicorn.py", "--bind", "0.0.0.0:8000", "--worker-class", "uvicorn.workers.UvicornWorker", "--workers", "5"]
