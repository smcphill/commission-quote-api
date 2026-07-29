# Phase 1 — Foundation: Requirements

Source: [docs/roadmap.md](../../docs/roadmap.md) item 1, [docs/tech-stack.md](../../docs/tech-stack.md).

## R1 — Python project managed by UV
- Repo root contains `pyproject.toml` and `uv.lock`, managed via `uv`.
- Python version pinned exactly to `3.12.13` (latest 3.12 patch release as of 2026-07-29) via a `.python-version` file at repo root, and `requires-python = "==3.12.13"` in `pyproject.toml`.
- `uv python pin 3.12.13` used to generate `.python-version`; `uv sync` downloads/uses that exact interpreter if not already installed.
- `uv sync` (fresh clone, no prior `.venv`) completes with exit code 0, creates `.venv/`, and `uv run python --version` reports `Python 3.12.13`.

## R2 — Flask app with a Hello World route
- Flask app lives at `app/main.py`, exposing a `Flask` instance named `app`.
- `GET /` returns HTTP status `200`.
- Response `Content-Type` is `text/html; charset=utf-8`.
- Response body is exactly `<h1>Hello World</h1>` (no surrounding whitespace/newlines beyond what Flask's default renderer adds is acceptable, but the `<h1>` tag content must match verbatim).
- App listens on port `5000` (Flask default) when run directly or via `flask run`.

## R3 — Makefile with `make install` and `make run`
- Root `Makefile` defines `install` and `run` targets.
- `make install` runs `uv sync`, installing project dependencies into `.venv/`.
- `make run` starts the Flask app locally (via `uv run flask run` or equivalent) and serves `GET /` on `http://localhost:5000/`.

## R4 — README updated
- [README.md](../../README.md) includes an "Install" section documenting `uv sync` (or equivalent) as the setup step.
- Includes a "Run" section documenting `make run`.
- Includes the expected result of visiting `http://localhost:5000/` after running.

## Out of scope for Phase 1
- Any route other than `GET /`.
- Tests, linting (covered in Phase 2).
- API key handling, `/api/quote` (covered in Phase 3+).
- Containerization (descoped; may return as a later phase).
