# FastAPI Template

This project provides a robust and flexible template for building REST APIs with FastAPI, following a clean architecture inspired by Domain-Driven Design (DDD) principles. It includes a structured approach to organizing business logic, handling routing, and managing dependencies, along with pre-configured tools for development and testing.

-----

## Table of Contents

  - [Features](https://www.google.com/search?q=%23features)
  - [Architecture Overview](https://www.google.com/search?q=%23architecture-overview)
      - [Business Logic Structure](https://www.google.com/search?q=%23business-logic-structure)
      - [Routers](https://www.google.com/search?q=%23routers)
      - [Middlewares](https://www.google.com/search?q=%23middlewares)
      - [Utils](https://www.google.com/search?q=%23utils)
  - [Getting Started](https://www.google.com/search?q=%23getting-started)
      - [Prerequisites](https://www.google.com/search?q=%23prerequisites)
      - [Installation](https://www.google.com/search?q=%23installation)
      - [Environment Variables](https://www.google.com/search?q=%23environment-variables)
      - [Running the Application](https://www.google.com/search?q=%23running-the-application)
      - [Running Tests](https://www.google.com/search?q=%23running-tests)
  - [Project Structure](https://www.google.com/search?q=%23project-structure)
  - [Code Generation (Blueprints)](https://www.google.com/search?q=%23code-generation-blueprints)
  - [Pre-commit Hooks](https://www.google.com/search?q=%23pre-commit-hooks)
  - [Database](https://www.google.com/search?q=%23database)
  - [Authentication](https://www.google.com/search?q=%23authentication)
  - [Error Handling](https://www.google.com/search?q=%23error-handling)
  - [Contributing](https://www.google.com/search?q=%23contributing)
  - [License](https://www.google.com/search?q=%23license)

-----

## Features

  - **FastAPI**: High-performance, easy-to-use web framework.
  - **SQLModel**: Type-based ORM for SQL databases, built on SQLAlchemy and Pydantic.
  - **Poetry**: Dependency management and packaging.
  - **Docker Compose**: Easy setup for PostgreSQL database.
  - **Clean Architecture**: Clear separation of concerns (Controllers, Use Cases, Repositories).
  - **Dependency Injection**: Managed using FastAPI's `Depends` for clear dependency graphs.
  - **JWT Authentication**: Secure user authentication with access tokens.
  - **Pre-commit Hooks**: Automated code formatting (Black, Ruff), type checking (MyPy), and tests.
  - **Health Check Endpoint**: Basic API health status.
  - **GZip Middleware**: Compresses responses for faster delivery.
  - **CORS Middleware**: Configured for cross-origin resource sharing.
  - **Blueprint**: Templates for quick generation of new route modules.

-----

## Architecture Overview

This project adheres to a clean architecture, as documented in `docs/adrs/project_structure.md`, promoting maintainability, testability, and scalability.

### Business Logic Structure

The core business logic is organized into the following layers:

  - **Controller**: Handles incoming requests, validates input DTOs (Data Transfer Objects), and orchestrates the call to the appropriate Use Case. It acts as the entry point for API routes.
  - **UseCase**: Encapsulates the application's business rules and logic. Each Use Case performs a specific task and interacts with repositories to fetch or persist data. They are designed to be independent of external frameworks.
  - **Repository**: Manages communication with the database. Repositories provide an abstraction over data storage, allowing Use Cases to interact with data without knowing the underlying database implementation. They are defined by **Protocols** to facilitate unit testing and ensure loose coupling.

**Order of Consumption:**

`Controller -> UseCase -> Repository` (via UseCase)

Repositories are not consumed directly by Controllers; they are injected into Use Cases.

### Routers

The routing system is structured hierarchically:

1.  **General Router**: The main `APIRouter` that includes fundamental routes (e.g., health check) and version-specific routers. (`src/fast_api_template/core/infra/base_router.py`)
2.  **Version Router**: Routers for API versioning (e.g., `v1`, `v2`). This allows for managing API changes gracefully. (`src/fast_api_template/infra/v1_router.py`)
3.  **Module Router**: Routers specific to a particular module or domain (e.g., `UserRouter`, `AccountRouter`). These contain the individual API endpoints for that module. (`src/fast_api_template/modules/user/v1/infra/user_router_v1.py`)

### Middlewares

Middlewares are located in the `src/fast_api_template/modules/shared/middlewares` directory. They are designed to perform global tasks that affect all incoming requests or outgoing responses, such as:

  - **CORS (Cross-Origin Resource Sharing)**: Configured to allow requests from any origin.
  - **GZip Compression**: Automatically compresses responses for requests above a certain size, improving performance.
  - **Process Time Header**: Adds an `X-Process-Time` header to responses, indicating how long it took to process the request.

**Important Note**: Middlewares do not share information directly with controllers. Any shared information or dependencies should be passed via FastAPI's dependency injection system. This ensures that middlewares focus solely on global concerns, while authentication and authorization logic reside within the application's core or specific use cases, often utilizing dependency injection for user validation.

### Utils

Utility functions, which solve simple, recurring problems across multiple modules, are stored in the `src/fast_api_template/modules/shared/utils` directory. Examples include cryptographic functions (`crypto.py`) for hashing and JWT handling.

-----

## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

Before you begin, ensure you have the following installed:

  - **Python 3.10+**: The project is built with Python 3.10.
  - **Poetry**: A Python dependency management and packaging tool. If you don't have it, install it with:
    ```bash
    pip install poetry
    ```
  - **Docker and Docker Compose**: Required for running the PostgreSQL database.

### Installation

1.  **Clone the repository:**

    ```bash
    git clone <your-repository-url>
    cd fast-api-template
    ```

2.  **Install project dependencies using Poetry:**

    ```bash
    poetry install
    ```

    This command will create a virtual environment and install all the dependencies listed in `pyproject.toml`.

3.  **Install pre-commit hooks:**

    ```bash
    poetry run pre-commit install
    ```

    This sets up hooks that will run automatically before each commit, ensuring code quality and consistency.

4.  **Start the database container:**

    ```bash
    docker-compose up -d db
    ```

    This will start a PostgreSQL database container in the background, as defined in `docker-compose.yml`. The database will be accessible on port `5432`.

### Environment Variables

The project uses `pydantic-settings` to manage environment variables. You need to create a `.env` file in the root of your project.

**Example `.env` file:**

```dotenv
POSTGRES_URL="postgresql+asyncpg://admin:admin@localhost:5432/template"
SALT="your_strong_salt_string"
PEPPER="your_strong_pepper_string"
SECRET="your_jwt_secret_key"
JWT_TTL=3600 # JWT Time-To-Live in seconds (e.g., 1 hour)
```

**Important:**

  - Replace `your_strong_salt_string`, `your_strong_pepper_string`, and `your_jwt_secret_key` with actual strong, randomly generated values. You can generate these using tools or Python's `secrets` module.
  - The `POSTGRES_URL` should match your database configuration. If using the provided `docker-compose.yml`, the URL `postgresql+asyncpg://admin:admin@localhost:5432/template` is correct.

### Running the Application

To start the FastAPI development server:

```bash
poetry run dev
```

This command will run `uvicorn` with `src/fast_api_template.core.main:app`, listening on `http://127.0.0.1:8000` and enabling auto-reload for development.

You can then access the API documentation (Swagger UI) at `http://127.0.0.1:8000/docs`.

### Running Tests

To execute the project's tests:

```bash
poetry run pytest
```

The `pytest.ini` file configures `asyncio_mode=auto` for seamless testing of asynchronous code.

-----

## Project Structure

The project follows a modular structure, with each major component or domain residing in its own module:

```
.
├── blueprints/                  # Templates for generating new modules/routes
├── docs/                        # Project documentation (ADRs, etc.)
│   └── adrs/
├── scripts/                     # Utility scripts (e.g., dev server runner)
├── src/
│   └── fast_api_template/
│       ├── core/                # Core application components
│       │   ├── infra/           # Infrastructure (database, routers, env)
│       │   ├── middlewares/     # Global FastAPI middlewares
│       │   └── main.py          # FastAPI application entry point
│       ├── infra/               # Versioning routers (e.g., v1_router)
│       ├── modules/             # Main application modules/domains
│       │   ├── health_check/    # Example module: API health check
│       │   │   ├── infra/
│       │   │   └── use_cases/
│       │   │       └── health_check/
│       │   ├── shared/          # Shared components across modules
│       │   │   ├── base_dto.py
│       │   │   ├── base_model.py
│       │   │   ├── base_use_case.py
│       │   │   ├── dependency_injections/ # Common dependency injections
│       │   │   ├── middlewares/       # Shared middlewares
│       │   │   └── utils/             # Utility functions (e.g., crypto)
│       │   └── user/              # Example module: User management
│       │       ├── repository/
│       │       │   └── schemas/
│       │       ├── v1/              # Versioned API for User module
│       │       │   └── features/    # Features/sub-domains within the module
│       │       │       ├── create_user/
│       │       │       ├── delete_me/
│       │       │       ├── get_me/
│       │       │       └── login/
│       │       └── user.py        # User ORM model
├── .env.example                 # Example environment variables file
├── .pre-commit-config.yaml      # Pre-commit hook configurations
├── docker-compose.yml           # Docker Compose setup for services
├── pyproject.toml               # Poetry project configuration and dependencies
├── pytest.ini                   # Pytest configuration
└── README.md                    # Project README
```

-----

## Code Generation (Blueprints)

The `blueprints/route/` directory contains templates that can be used to quickly scaffold new routes/features within your modules. These templates include:

  - `{{file_name}}_controller.py.template`
  - `{{file_name}}_dto.py.template`
  - `{{file_name}}_injection.py.template`
  - `{{file_name}}_use_case.py.template`

These templates are designed to follow the established architecture (Controller, DTO, Injection, UseCase). You would typically use a custom script or a tool like `blprint` (which is a dependency of this project) to generate new modules from these templates, replacing the `{{variable}}` placeholders with your desired names (e.g., `{{name__snake_case}}`, `{{name__camel_case}}`).

**Example of `blprint` usage (assuming `blprint` is installed and configured):**

To create a new `product` module feature within `v1`:

```bash
blueprint create route ./src/fast_api_template/modules/product/v1/features/
```

(Note: You might need to adjust the `blueprint` command based on its exact configuration for this project.)

-----

## Pre-commit Hooks

This project uses `pre-commit` to maintain code quality and consistency. The `.pre-commit-config.yaml` file defines the following hooks:

  - **Black**: An uncompromising Python code formatter.
  - **MyPy**: A static type checker for Python. It checks for type consistency across your codebase.
  - **Ruff**: An extremely fast Python linter, written in Rust.
  - **`end-of-file-fixer`**: Ensures files end with a newline.
  - **`trailing-whitespace`**: Removes superfluous whitespace at the end of lines.
  - **`check-merge-conflict`**: Checks for files that contain merge conflict strings.
  - **`pytest-check`**: Runs all tests before each commit, preventing commits that break existing functionality.

These hooks run automatically when you commit your changes, helping to catch issues early in the development cycle.

-----

## Database

The project uses **SQLModel** as its ORM, providing a type-hinted way to interact with SQL databases. The `docker-compose.yml` file sets up a PostgreSQL database.

  - **`db` service**: Runs a `postgres:15` image.
  - **Environment Variables**: Configured with `POSTGRES_USER`, `POSTGRES_PASSWORD`, and `POSTGRES_DB` set to `admin`, `admin`, and `template` respectively. **Remember to change these credentials in production environments.**
  - **Port Mapping**: The database is exposed on port `5432` of your host machine.
  - **Volume**: A named volume `pgdata` is used to persist database data, so your data won't be lost when the container is stopped or removed.

The `create_db_and_tables()` function in `src/fast_api_template/core/infra/database.py` is called during the application's `lifespan` event to automatically create all defined SQLModel tables if they don't already exist.

-----

## Authentication

The project includes a basic JWT-based authentication system:

  - **`require_user_injection.py`**: Provides `GetCurrentUser` as a FastAPI dependency. This dependency decrypts a JWT token from the `Authorization` header, validates its expiration, and retrieves the corresponding `User` from the database. If the token is invalid or expired, it raises an `HTTPException`.
  - **`login_controller.py`**: Handles user login, authenticating credentials and issuing a JWT token.
  - **`crypto.py`**: Contains utility functions for hashing passwords (`hash_string`) and encrypting/decrypting JWT payloads (`encrypt_payload`, `decrypt_jwt`).
  - **`User` model**: Defines the user schema with email and hashed password.

-----

## Error Handling

The project currently has a `TODO` to improve error handling, specifically for login and user creation errors. While some basic `HTTPException` are raised (e.g., for duplicate emails or invalid tokens), a more comprehensive global error handling strategy could be implemented (e.g., custom exception handlers for specific error types or a centralized error response format).

-----

## Contributing

Contributions are welcome\! If you'd like to contribute, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes.
4.  Ensure all tests pass and pre-commit hooks run successfully.
5.  Write clear and concise commit messages.
6.  Open a pull request.

-----

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

-----
