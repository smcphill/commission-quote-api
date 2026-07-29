# Phase 2 — Testing & Linting: Requirements

Source: [docs/roadmap.md](../../docs/roadmap.md) item 2, [docs/tech-stack.md](../../docs/tech-stack.md).
Depends on Phase 1 being complete ([../phase-1/validation.md](../phase-1/validation.md) passing).

## R1 — pytest for unit and API tests
- `tests/` directory at repo root, containing at least:
  - `tests/unit/` — unit-level tests (no live server required).
  - `tests/api/` — tests using the `requests` library against a running instance of the app.
- At least one unit test asserting the `/` view function's response contains `<h1>Hello World</h1>` (the view renders a full HTML template via `render_template`/`url_for`, so the body is not that string alone).
- At least one API test: start the app (via pytest fixture, e.g. `flask.testing` test client, or subprocess + `requests`), assert `GET /` returns status `200` and a body containing `<h1>Hello World</h1>`.
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
- `eslint.config.js` at repo root (flat config — the `npx`-installed ESLint version requires this format over legacy `.eslintrc`).
- Scoped to `app/static/js/**/*.js`, the app's static JS directory (`app/main.py`'s `index` view renders `app/templates/index.html`, which references `app/static/js/app.js` via `url_for('static', filename=...)`).
- `eslint .` exits `0` against the current codebase.

## R5 — Makefile targets
- `lint` — runs `flake8`, `black --check`, and `eslint`, in that order; fails (non-zero exit) if any fail.
- `test` — runs `pytest tests/unit`.
- `api-test` — runs `pytest tests/api` (implies the app must be running or the target must start/stop it).
- `browser-test` — runs the Playwright suite (implies the app must be running or the target must start/stop it).
- All four targets declared `.PHONY`.

## R6 — README updated
- Adds a "Prerequisites" section documenting how to install everything needed to run lint/test locally: `uv` itself, Node.js/npm (for `npx eslint`), and any OS-level packages Playwright's browser install needs.
- Adds a "Lint" section documenting `make lint`.
- Adds a "Test" section documenting `make test`, `make api-test`, `make browser-test`, including any one-time setup (e.g. `uv run playwright install`).

## Out of scope for Phase 2
- CI/CD pipeline wiring (not requested by roadmap).
- Test coverage thresholds — "a few tests," not exhaustive coverage.
