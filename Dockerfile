# pull official base image
FROM python:3.11.2-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt update \
  && apt -y install netcat gcc \
  && apt clean \

RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false

# install python dependencies
COPY ["./poetry.lock", "./pyproject.toml", "./"]
RUN poetry install

COPY backend_fastapi/ ./
