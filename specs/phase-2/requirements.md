# Phase 2 — Testing & Linting: Requirements

Source: [docs/roadmap.md](../../docs/roadmap.md) item 2, [docs/tech-stack.md](../../docs/tech-stack.md).
Depends on Phase 1 being complete ([../phase-1/validation.md](../phase-1/validation.md) passing).

## R1 — pytest for unit and API tests
- `tests/` directory at repo root, containing at least:
  - `tests/unit/` — unit-level tests (no live server required).
  - `tests/api/` — tests using the `requests` library against a running instance of the app.
- At least one unit test asserting the `/` view function returns the expected body string.
- At least one API test: start the app (via pytest fixture, e.g. `flask.testing` test client, or subprocess + `requests`), assert `GET /` returns status `200` and body `<h1>Hello World</h1>`.
- `pytest` is a dependency declared in `pyproject.toml` under a `dev`/`test` dependency group.
- Running `pytest tests/unit` and `pytest tests/api` each exit `0` with all tests passing.

## R2 — Playwright for browser tests
- `tests/browser/` directory containing at least one Playwright test.
- Test opens `http://localhost:5000/` in a real browser context and asserts the rendered page contains an `<h1>` element with text `Hello World`.
- `playwright` (Python) declared as a dev dependency; browsers installed via `uv run playwright install` (documented, not necessarily automated in CI for this phase).

## R3 — flake8 and black for Python linting
- `flake8` and `black` declared as dev dependencies.
- A `setup.cfg` or `.flake8` config sets line length consistent with `black` (e.g. 88) to avoid conflicting rules.
- `flake8 app tests` exits `0` (no lint errors) against the current codebase.
- `black --check app tests` exits `0` (no formatting diffs) against the current codebase.

## R4 — eslint for JavaScript linting
- `.eslintrc` (or `eslint.config.js`) at repo root or in the frontend asset directory.
- Applies even though Phase 2 has no JS yet — config must exist and be runnable (`eslint .` exits `0` on an empty/placeholder JS tree), so later phases have linting in place from the start.

## R5 — Makefile targets
- `lint` — runs `flake8`, `black --check`, and `eslint`, in that order; fails (non-zero exit) if any fail.
- `test` — runs `pytest tests/unit`.
- `api-test` — runs `pytest tests/api` (implies the app must be running or the target must start/stop it).
- `browser-test` — runs the Playwright suite (implies the app must be running or the target must start/stop it).
- All four targets declared `.PHONY`.

## R6 — README updated
- Adds a "Lint" section documenting `make lint`.
- Adds a "Test" section documenting `make test`, `make api-test`, `make browser-test`, including any one-time setup (e.g. `uv run playwright install`).

## Out of scope for Phase 2
- CI/CD pipeline wiring (not requested by roadmap).
- Test coverage thresholds — "a few tests," not exhaustive coverage.
