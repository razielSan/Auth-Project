<div align="center">

# ⚡ Authenticate Project

An educational backend application built with FastAPI, demonstrating user authentication, authorization, and user management.

### 🧱 Technology Stack

[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.51+-blue.svg)](https://www.sqlalchemy.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14+-blue.svg)](https://www.postgresql.org/)
[![SQLite](https://img.shields.io/badge/SQLite-enabled-green.svg)](https://www.sqlite.org/)
[![Redis](https://img.shields.io/badge/Redis-5.0.14+-blue.svg)](https://redis.io/)
[![Alembic](https://img.shields.io/badge/Alembic-1.14.1-blue.svg)](https://alembic.sqlalchemy.org/en/latest/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0+-blue.svg)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
![JavaScript](https://img.shields.io/badge/JavaScript-enabled-green.svg)
[![Tests](https://img.shields.io/badge/tests-pytest-success.svg)](https://docs.pytest.org/en/stable/)
![AsyncIO](https://img.shields.io/badge/Async-First-green.svg)
![Architecture](https://img.shields.io/badge/architecture-layered-green.svg)
![JWT](https://img.shields.io/badge/JWT-enabled-green.svg)


**Project goals:**

📚 Learning resource for backend development<br>
🏗️ Example of layered architecture<br>
🔐 Reference implementation of authentication and authorization<br>

</div>


## 🎨  Overview


Authenticate Project demonstrates the implementation of common
backend features using FastAPI and modern Python technologies.

The project focuses on application architecture, asynchronous
programming, database integration, authentication, authorization,
and automated testing.



## 👨‍💻 Features

### Authentication and Security

- User registration and authentication
- JWT access and refresh tokens
- Access and refresh token validation
- Password hashing with Argon2
- Role-based access control

### Management

- User management
- Admin functionality

### Infrastructure

- SQLite and PostgreSQL support
- Asynchronous database operations
- Redis-based rate limiting
- Database migrations with Alembic

### Testing

- Automated testing with pytest



## 📁 Architecture


```text
src/
├── app/
│   └── my_project/
│       ├── backend/
│       │   ├── application/     # Application use cases.
│       │   ├── cli/              # Database initialization and preparation scripts.
│       │   ├── core/             # Application initialization and composition.
│       │   ├── presentation/     # HTTP routes, handlers.
│       │   └── ...
│       │
│       └── frontend/
│
├── core/                         # Shared project components and utilities.
├── domain/                       # Domain models, interfaces, and business rules.
├── dto/                           # Data Transfer Objects.
├── infrastructure/               # Database and external service implementations.
├── settings/                      # Application configuration.
├── test_data/                     # Test data and database utilities.
└── ...
```


## 🚀 Installation

### 1️⃣ Clone repository

```bash
git clone <repository-url>
cd <repository-directory>
```


### 2️⃣ Install dependencies

First. install Poetry

```bash
pip install poetry
poetry install
```

**For development**

Install all dependencies, including development tools(pytest, mypy, ruff, etc.)

```bash
poetry install
```

**For production**

Install only the main dependencies required to run, the application

```bash
poetry install --without dev
```


### 3️⃣ Configuration

Create the following files in the project root:

- .env
- .env.test

Use the example files as templates:

- [The content of the .env file](.env.example)
- [The content of the .env.test file](.env.test.example)

Update the configuration values according to your environment.

### 4️⃣  Database preparation

Run the commands corresponding to your database.

| SQLite | PostgreSQL |
| :--- | :--- |
| `poetry run sqlite-prepare` | `Create the database and PostgreSQL user` |
| `poetry run alembic upgrade head` | `poetry run alembic upgrade head` |
| `poetry run create-roles` | `poetry run create-roles` |
| `poetry run create-admin` | `poetry run create-admin` |


### ▶️ Running the application

Start redis

```bash
poetry run redis-server
```
Start app

```bash
poetry run app
```


## Testing

The project uses pytest and pytest-asyncio.

For detailed instructions on running tests, configuring
test databases, and adding new database backends,
see [TESTING.md](TESTING.md).


###  🗄 Database Support

| Database           | Status        |
| ------------------ | ------------- |
| SQLite             | ✅ Supported  |
| PostgreSQL         | ✅ Supported  |

### 📬 Contact

Telegram: @razielasus

⭐ Support Project

If this repository helped you:

Star the repo ⭐
Fork it 🍴
Share it 🚀