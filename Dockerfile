FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN pip install poetry

COPY poetry.lock .
COPY pyproject.toml .
RUN poetry install

COPY . ./

