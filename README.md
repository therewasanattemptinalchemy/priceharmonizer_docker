# Price Harmonizer

A Django app to ingest product price data, clean it, and sync it using Dockerized services. Includes:

- SQL triggers for logging
- Django signals for validation
- REST API for access
- CI/CD via GitHub Actions
- Fully automated via Makefile

## Setup

```bash
make build
make up
make migrate
make load-fixtures
make setup-db
make test