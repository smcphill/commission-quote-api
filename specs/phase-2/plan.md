# Phase 2 — Testing & Linting: Plan

Implements [requirements.md](requirements.md). Verified by [validation.md](validation.md).

## File layout to add

```
.
├── .flake8
├── pyproject.toml          # updated: dev deps + black/pytest config
├── .eslintrc.json
├── Makefile                # updated: lint, test, api-test, browser-test
├── README.md                # updated
└── tests/
    ├── unit/
    │   └── test_app.py
    ├── api/
    │   └── test_hello_world_api.py
    └── browser/
        └── test_hello_world_browser.py
```

## Steps

1. **Add dev dependencies** (R1, R2, R3)
   - `uv add --dev pytest requests playwright flake8 black`
   - `uv run playwright install chromium` (document as manual one-time step; not required for `make lint`/`make test`).

2. **Unit test** (R1)
   - `tests/unit/test_app.py`: import `app` from `app.main`, use Flask's built-in test client (`app.test_client()`), assert status 200 and body on `GET /`.
   - This does not require a running server — fast, no network.

3. **API test** (R1)
   - `tests/api/test_hello_world_api.py`: use `requests.get("http://localhost:5000/")` against a live instance.
   - Fixture assumption: the `api-test` Makefile target is responsible for starting the app before pytest and stopping it after — the test itself just assumes `localhost:5000` is reachable.

4. **Browser test** (R2)
   - `tests/browser/test_hello_world_browser.py`: use `playwright.sync_api`, launch chromium, `page.goto("http://localhost:5000/")`, assert `page.locator("h1").inner_text() == "Hello World"`.
   - Same "app already running" assumption as API tests, owned by `browser-test` target.

5. **Linting config** (R3, R4)
   - `.flake8`: `max-line-length = 88`, exclude `.venv`.
   - `black` config via `[tool.black]` in `pyproject.toml`, `line-length = 88`.
   - `.eslintrc.json`: minimal recommended ruleset (`eslint:recommended`), `env.browser = true`. Create a placeholder `static/js/.gitkeep` or similar if no JS exists yet, so `eslint .` has a defined (empty) target rather than erroring on "no files found" — alternatively scope `eslint` to a `static/` glob that's allowed to match zero files.

6. **Makefile targets** (R5)
   ```makefile
   .PHONY: run lint test api-test browser-test

   lint:
   	uv run flake8 app tests
   	uv run black --check app tests
   	npx eslint .

   test:
   	uv run pytest tests/unit

   api-test:
   	$(MAKE) run &
   	sleep 2
   	uv run pytest tests/api; kill %1

   browser-test:
   	$(MAKE) run &
   	sleep 2
   	uv run pytest tests/browser; kill %1
   ```
   - The `start in background, sleep, test, kill` pattern is a pragmatic choice for a 4-hour scope — acceptable here, but note it's a known flaky pattern (fixed sleep) if this were to be hardened later.

7. **README** — update last, once targets are confirmed working (R6).
   - Add a "Prerequisites" section (before Lint/Test) covering: installing `uv`, installing Node.js/npm (needed for `npx eslint`), and the `uv run playwright install` step with any OS packages it may prompt for.

## Sequencing note
Write the unit test first (fastest feedback, no server), confirm `make test` and `make lint` are green, then add API/browser tests which require the start/stop server choreography.
