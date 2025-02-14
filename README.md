# SQL Injection Vulnerability Demo

Simple containerized web application demonstrating an SQL injection vulnerability.

## How to Deploy
1. Install [Docker](https://www.docker.com/get-started/) and [Docker Compose](https://docs.docker.com/compose/install/).

2. Copy the `.env.example` file in `/src`, rename into `.env`, and set its own credentials.

```bash
cd /src
cp .env.example .env
```

3. Run & build
```bash
docker compose up -d --build
```
or simply execute
```bash
chmod +x setup.sh \
    ./setup.sh
```

4. Access the app at running on nginx port `:8051`, http://localhost:8051 or http://127.0.0.1:8051