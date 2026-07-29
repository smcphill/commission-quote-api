# Phase 1 — Foundation: Validation

Run these checks, in order, to confirm [requirements.md](requirements.md) is satisfied. Each maps to one or more requirement IDs.

## V1 — UV setup (R1)
```
rm -rf .venv
uv sync
echo "exit: $?"        # expect 0
test -d .venv && echo "PASS: .venv created"
uv run python --version
# expect: Python 3.12.13
```

## V2 — Local run + Hello World (R2, R3)
```
make run &
sleep 2
curl -s -o /tmp/body -w "%{http_code}\n" http://localhost:5000/
# expect: 200
cat /tmp/body
# expect: <h1>Hello World</h1>
kill %1
```

## V3 — README accuracy (R4)
- Manual check: follow README.md's Install + Run sections verbatim on a clean clone. No undocumented steps should be needed.

## Exit criteria for Phase 1
All of V1–V3 pass. This phase is the base commit that Phase 2's tests and linters will run against — do not proceed to Phase 2 until `GET /` is confirmed working locally.
