DOCKER_COMPOSE=docker-compose
MANAGE=python manage.py

.PHONY: build up migrate setup-db load-fixtures test clean

build:
	$(DOCKER_COMPOSE) build

up:
	$(DOCKER_COMPOSE) up -d

migrate:
	$(DOCKER_COMPOSE) exec web $(MANAGE) migrate

load-fixtures:
	$(DOCKER_COMPOSE) exec web $(MANAGE) loaddata products_fixture.json

setup-db:
	$(DOCKER_COMPOSE) exec db psql -U user -d price_db -f /docker-entrypoint-initdb.d/init_triggers.sql

test:
	$(DOCKER_COMPOSE) exec web $(MANAGE) test

clean:
	$(DOCKER_COMPOSE) down -v
