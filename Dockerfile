FROM python:3.7-alpine3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apk update \
  # psycopg2 dependencies
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  # Pillow dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
  # CFFI dependencies
  && apk add libffi-dev py-cffi \
  # Translations dependencies
  && apk add gettext \
  && apk add curl openssh bash  \
  # https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
  && apk add postgresql-client \
  && apk add git \
  && pip install --upgrade pip \
  && pip install pipenv

COPY Pipfile Pipfile.lock .pre-commit-config.yaml ./
RUN pipenv install --system --deploy --dev \
    && git init . \
    && pre-commit install-hooks

RUN pipenv install --system --deploy --dev

ADD . ./

RUN rm /bin/sh && ln -s /bin/bash /bin/sh




