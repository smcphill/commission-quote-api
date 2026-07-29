# Phase 2 — Testing & Linting: Validation

Run these checks, in order, to confirm [requirements.md](requirements.md) is satisfied.

## V1 — Unit tests (R1)
```
make test
echo "exit: $?"   # expect 0
```
Expect pytest output showing ≥1 passed test in `tests/unit/`.

## V2 — API tests (R1)
```
make api-test
echo "exit: $?"   # expect 0
```
Expect the target to start the app, run `tests/api/`, report ≥1 passed, and leave no orphaned server process (`ps aux | grep flask` shows nothing after the target completes).

## V3 — Browser tests (R2)
```
make browser-test
echo "exit: $?"   # expect 0
```
Expect ≥1 passed test in `tests/browser/`, confirming the page rendered from `app/templates/index.html` contains an `<h1>` element with text `Hello World` in a real Chromium context.

## V4 — Linting (R3, R4)
```
make lint
echo "exit: $?"   # expect 0
```
Expect all three sub-checks (flake8, black --check, eslint) to report no issues. Intentionally break formatting in a scratch file first, confirm `make lint` fails (non-zero exit), then revert — this proves the target actually catches violations rather than silently passing.

## V5 — README accuracy (R6)
- Manual check: on a clean clone (with Phase 1 already validated), follow the README's Prerequisites, Lint, and Test sections verbatim, including installing `uv`, Node.js/npm, and the one-time `playwright install` step. No undocumented steps should be needed.

## Exit criteria for Phase 2
All of V1–V5 pass, and `make lint`/`make test`/`make api-test`/`make browser-test` are all green on a clean checkout. This is the base that Phase 3 (`POST /api/quote`) will add tests against using the same patterns established here.
