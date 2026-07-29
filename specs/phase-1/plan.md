# Phase 1 — Foundation: Plan

Implements [requirements.md](requirements.md). Verified by [validation.md](validation.md).

## File layout to produce

```
.
├── Makefile
├── pyproject.toml
├── uv.lock
├── README.md
└── app/
    ├── __init__.py
    └── main.py
```

## Steps

1. **Initialize UV project** (R1)
   - `uv init --package`, then `uv python pin 3.12.13` to write `.python-version`.
   - Set `requires-python = "==3.12.13"` in `pyproject.toml`.
   - `uv add flask`.
   - Commit `uv.lock` and `.python-version`.

2. **Flask app** (R2)
   - `app/main.py`: create `app = Flask(__name__)`, single route `@app.route("/")` returning `"<h1>Hello World</h1>"`.
   - No templates directory needed for a single static string — return it directly from the view function.

3. **Makefile** (R3)
   - `install:` target → `uv sync`.
   - `run:` target → `uv run flask --app app.main run --port=5000`.
   - Keep target names lowercase, one command per target, `.PHONY` declared.

4. **README** (R4)
   - Write after 1–3 are working, so instructions reflect the real commands.

## Sequencing note
Do R1→R2 first and confirm the app runs locally before writing the Makefile/README.
