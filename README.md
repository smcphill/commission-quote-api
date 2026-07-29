# commission-quote-api
Coding chalenge for Bendigo Bank

## Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/) — manages the Python version and dependencies.
- [Node.js](https://nodejs.org/) (includes `npm`/`npx`) — used to run ESLint via `npx eslint`.
- Playwright's browser binaries — installed automatically by `make install`. On Linux this may also prompt for OS packages; follow Playwright's on-screen instructions if so.

`make install` runs `uv sync`, installs Playwright's Chromium browser, and runs `npm install` to install Node devDependencies (ESLint).

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

```
make test           # unit tests
make api-test       # API tests against a running instance of the app
make browser-test   # browser tests against a running instance of the app
```
