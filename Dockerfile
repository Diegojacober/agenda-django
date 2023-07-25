FROM python:alpine

ARG YOUR_ENV

ENV YOUR_ENV=${YOUR_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.0.0

WORKDIR /var/www

RUN pip install "poetry==1.2.0"
 
COPY ./pyproject.toml /var/www/pyproject.toml
 
 COPY ./ /var/www

RUN poetry config virtualenvs.create false \
  && poetry install


WORKDIR /var/www
