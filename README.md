# commission-quote-api
Coding chalenge for Bendigo Bank

## Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/) — manages the Python version and dependencies.
- [Node.js](https://nodejs.org/) (includes `npm`/`npx`) — used to run ESLint via `npx eslint`.
- Playwright's browser binaries — installed with a one-time `uv run playwright install chromium` (see Test section below). On Linux this may also prompt for OS packages; follow Playwright's on-screen instructions if so.

## Install

```
make install
```

## Run

```
make run
```

The app will be available at http://localhost:5000/.

## Lint

```
make lint
```

Runs `flake8`, `black --check`, and `eslint` against `app/` and `tests/`.

## Test

One-time setup, to install the Playwright browser used by the browser tests:

```
uv run playwright install chromium
```

Then:

```
make test           # unit tests
make api-test       # API tests against a running instance of the app
make browser-test   # browser tests against a running instance of the app
```
