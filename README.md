
[![codecov](https://codecov.io/gh/tiagoCMatias/FastApiTemplate/graph/badge.svg?token=XBJEKRU2QA)](https://codecov.io/gh/tiagoCMatias/FastApiTemplate)

# FastAPI + SQLAlchemy + Alembic

## Overview

This project is a template for a FastAPI project that uses SQLAlchemy for database management and Alembic for database migrations.

## Installation

To install the project, use the following command:

```bash
pip install -r requirements.txt
```

## FastAPI

### Running the Server

To run the server, use the following command:

```bash
uvicorn main:app --reload
```

## Alembic

### Running Migrations

To run migrations, use the following command:

```bash
alembic upgrade head
```

### Generating Migrations

To generate a new migration, use the following command:

```bash
alembic revision --autogenerate -m "migration message"
```

### Downgrading Migrations

To downgrade a migration, use the following command:

```bash
alembic downgrade -1
```

## Testing

To run tests, use the following command:

```bash
pytest
```