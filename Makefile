typecheck:
	uv run mypy .

format:
	uv run ruff format .

lint:
	uv run ruff check . --fix

run:
	uv run daphne -b 0.0.0.0 -p 8000 mynewproject.asgi:application

makemigrations:
	uv run python manage.py makemigrations

migrate:
	uv run python manage.py migrate

test:
	uv run pytest mynewproject/tests

init:
	uv sync --frozen

fix:
	make format typecheck lint

collectstatic:
	uv run python manage.py collectstatic --noinput