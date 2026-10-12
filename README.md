# Task & Handover Tracker

A small REST API for tracking shift tasks, built with FastAPI. Developed over two
Agile sprints with a CI pipeline (GitHub Actions), automated tests and basic monitoring.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs for the interactive API (Swagger UI).

## Endpoints

| Method | Path | Description |
|---|---|---|
| POST | `/tasks` | Create a task (`title`, optional `description`, `priority`) |
| GET | `/tasks` | List tasks. Filters: `?completed=true`, `?priority=high` |
| PATCH | `/tasks/{id}/complete` | Mark a task complete |
| GET | `/health` | Health check for monitoring |

## Run tests

```bash
pytest --cov=app --cov-report=term-missing
ruff check .
```

## Project docs

See the `docs/` folder for the backlog, sprint plans, reviews and retrospectives.
