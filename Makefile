.PHONY: install run lint test api-test browser-test

install:
	uv sync
	uv run playwright install chromium
	npm install

run:
	uv run flask --app app.main run --port=5000

lint:
	uv run flake8 app tests
	uv run black --check app tests
	npx eslint .

test:
	uv run pytest tests/unit

api-test:
	$(MAKE) run & pid=$$!; \
	trap 'kill $$pid' EXIT; \
	sleep 2; \
	uv run pytest tests/api

browser-test:
	$(MAKE) run & pid=$$!; \
	trap 'kill $$pid' EXIT; \
	sleep 2; \
	uv run pytest tests/browser
