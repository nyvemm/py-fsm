FROM python:3.10

COPY poetry.lock pyproject.toml /app/

WORKDIR /app

ENV PATH="/app/venv/bin:$PATH"

RUN python -m venv venv
RUN venv/bin/pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY . /app

