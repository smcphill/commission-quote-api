# commission-quote-api
Coding chalenge for Bendigo Bank

## Approach

I recently experimented with Spec Driven Development (SDD) and liked the up-front context gathering it employs. These artifacts live under `./docs`:

- [mission.md](./docs/mission.md) - a digest of the provided `hiring-full-stack coding challenge.pdf`
- [roadmap.md](./docs/roadmap.md) - a development and delivery roadmap
- [tech-stack.md](./docs/tech-stack.md) - describes the language, frameworks and packages used


## AI Usage

Claude code was used for SDD for [roadmap](./docs/roadmap.md) phases 1 & 2, and also some minor out-of-phase work prior to phase 3 and beyond.

I curated spaces within `./specs` for phases 1 & 2 to facilitate the above. This was done with AI assistance.

All work undertaken in conjunction with AI is committed with a co-author statement from Claude code.

## Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/) — manages the Python version and dependencies.
- [Node.js](https://nodejs.org/) (includes `npm`/`npx`) — used to run ESLint via `npx eslint`.
- Playwright's browser binaries — installed automatically by `make install`. On Linux this may also prompt for OS packages; follow Playwright's on-screen instructions if so.

## Makefile actions

A `Makefile` has been provided to simplify development operations and running the app.

### Install

```
make install
```

- runs `uv sync` and `npm install`, and installs Playwright's Chromium browser


### Run

```
make run
```

The app will be available at http://localhost:5000/.

#### Enabling chaos mode

Under chaos mode, requests will randomly fail (either with a simulated server error or connection failure).

When accessed via http://localhost:5000/?use=dev, the UI will provide the option to enable chaos mode. This injects `X-Bendigo-Chaos: true` into the HTTP request header.

Alternatively, the api will enable choas mode with a `CHAOS_MODE=true` env var.

#### BYO API Key

When accessed via http://localhost:5000/?use=dev, the UI will provide the option to supply your own API key.

#### Runtime constraints

- Loan amount: $1,000 - $5,000,000
- Loan term (months): 1 - 240 (aka 20 years)
- Risk band: ["BELOW_AVERAGE", "AVERAGE", "VERY_GOOD", "EXCELLENT"]

### Lint

```
make lint
```

Runs `flake8`, `black --check`, and `eslint` against `app/` and `tests/`.

### Auto fix

```
make fix-lint
```

Fixes linting issues found by eslint/black

### Test

```
make test           # unit tests
make api-test       # API tests against a running instance of the app
make browser-test   # browser tests against a running instance of the app
```
#### ℹ️ erroneous 'error' reported on successful runs

API and browser tests will issue `make[1]: *** [run] Error 143` upon completion. This can be ignored. 

This comes about from the changes made to the Makefile in 9d709870f933a1c131427bd95e9b1a5a191c66a3 due to the way the test server is initialised.

TODO A fix would be the leverage pytest's `conftest.py` setup.

