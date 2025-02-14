# SQL Injection Vulnerability Demo

Simple containerized flask web application demonstrating an SQL injection vulnerability.

## How to Deploy
1. Install [Docker](https://www.docker.com/get-started/) and [Docker Compose](https://docs.docker.com/compose/install/).

2. Copy the `.env.example` file in [src/.env.example](src/.env.example), rename into `.env`, and set its own credentials.

```bash
cd src/
cp .env.example .env
```

3. Set DB Query at [src/query.sql.example](src/query.sql.example)

```bash
cd src/
cp query.sql.example query.sql
```

4. Run & build
```bash
docker compose up -d --build
```

or simply execute

```bash
chmod +x setup.sh \
    ./setup.sh
```

5. Access the app at running on nginx port `:8051`, http://localhost:8051 or http://127.0.0.1:8051