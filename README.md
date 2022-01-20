Exchange app
============

- *Exchange Rate API*: [localhost:8000/api/rates/]
- *Docs*: [localhost:8000/docs/]
- *Admin*: [localhost:8000/admin/]
- *ReDoc*: [localhost:8000/redoc/]

# Developer Guide

The development environment can be managed either locally via pipenv or using docker and docker-compose.

## Prerequisite

- [Docker](https://docs.docker.com/install/)
- [docker-compose](https://docs.docker.com/compose/install/)  

## Makefile reference


```bash
# build (usually, requires to build when changes happen to the Dockerfile or docker-compose.yml)
$ make build

# start all services and dependencies
$ make up

# down and remove all services
$ make rm

# restart (removes all services and restart them -- without rebuilding)
$ make restart

# list services running/active services
$ make ps

# open bash console in the app service
$ make bash

# Run pre-commit to project base and apply formatting.
$ make lint

# run unit testing
$ make test

```
