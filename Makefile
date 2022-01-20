help:
	@echo "docker-compose commands:"
	@echo "    make lint:       Run pre-commit hooks"
	@echo "    make rm: 		Removes all docker containers running"
	@echo "    make up: 		Up all services - Starts all services"
	@echo "    make bash: 		Bash into application container"
	@echo "    make ps:			list containers/services"
	@echo "	   make restart:    restart (removes all services and restart them -- without rebuilding)"
	@echo "	   make build:		build (usually, requires to build when changes happen to the Dockerfile or docker-compose.yml)"
	@echo "    make bash: 		open bash console in the app service"
	@echo "    make test: 		run application unit tests"


lint:
	docker-compose run --rm app pre-commit run --all-files

rm:
	docker-compose down && docker-compose rm -f

up:
	docker-compose up -d

ps:
	docker-compose ps

restart:
	make rm && make up

build:
	docker-compose build

bash:
	docker-compose run --rm app bash

test:
	docker-compose run --rm app pytest


