.PHONY: install run

install:
	uv sync

run:
	uv run flask --app app.main run --port=5000
