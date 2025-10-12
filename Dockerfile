FROM python:3.12-slim


ENV POETRY_VERSION=1.8.2
ENV POETRY_HOME="/opt/poetry"

ENV POETRY_VIRTUALENVS_CREATE=false
ENV PATH="$POETRY_HOME/bin:$PATH"

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends libjpeg-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock* /app/

RUN poetry install --no-interaction --no-ansi --no-root --no-dev

COPY . /app/

EXPOSE 8041

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8041"]