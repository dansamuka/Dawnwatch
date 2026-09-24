.PHONY: install lint test run

install:
	pip install -e ".[dev]"

lint:
	ruff check .

test:
	pytest -q

run:
	uvicorn dawnwatch.api:app --reload
