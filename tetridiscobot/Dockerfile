FROM python:3.11

WORKDIR /app/discord

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock /app/discord/
RUN poetry install --only main

COPY . /app/discord
ENTRYPOINT [ "python", "main.py" ]