# Simple Notes API

A lightweight, asynchronous REST API built with **FastAPI**, **SQLAlchemy** (Async), and **PostgreSQL** for managing simple notes. 

This project was built to master the fundamental FastAPI workflow: project initialization with `uv`, environment configuration, database setup, and basic CRUD operations.

---

## Features

- **Asynchronous Database Access:** Powered by `asyncpg` and SQLAlchemy's `ext.asyncio`.
- **Environment Management:** Uses `.env` files and `python-dotenv` for secure database credentials.
- **Automatic Schema Creation:** Managed via FastAPI lifespan context managers.
- **RESTful Endpoints:** Full support for creating, reading, listing, and deleting notes.

---

## Tech Stack

- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy 2.0 (Async)
- **Package Manager:** `uv`
- **Server:** Uvicorn

---

## Prerequisites

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) package manager installed
- PostgreSQL installed and running locally

---

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone <https://github.com/SonsoriIssah/Simple-Notes-API>
   cd <your-repo-folder>
   ```

2. **Initialize and install dependencies with `uv`:**
   ```bash
   uv sync
   ```
   *(Or install directly from `requirements.txt`: `uv pip install -r requirements.txt` or `pip install -r requirements.txt`)*

3. **Configure Environment Variables:**
   Create a `.env` file in the root directory and add your database URL:
   ```env
   DATABASE_URL="postgresql+asyncpg://postgres:postgres@localhost:5432/notesdb"
   ```

4. **Create the Database:**
   Ensure PostgreSQL is running and create the `notesdb` database:
   ```bash
   psql -U postgres -c "CREATE DATABASE notesdb;"
   ```

---

## Running the Application

Start the development server using `uv run`:

```bash
uv run uvicorn main:app --reload
```

The server will start at `http://127.0.0.1:8000`.

---

## Interactive API Documentation

FastAPI automatically generates interactive Swagger documentation:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/notes` | Retrieve all notes |
| `GET` | `/notes/{id}` | Retrieve a specific note by ID |
| `POST` | `/notes` | Create a new note |
| `DELETE` | `/notes/{id}` | Delete a note by ID |
