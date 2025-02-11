typecheck:
	pipenv run mypy .

format:
	pipenv run ruff format .

lint:
	pipenv run ruff check . --fix

run:
	pipenv run python manage.py runserver

makemigrations:
	pipenv run python manage.py makemigrations

migrate:
	pipenv run python manage.py migrate

test:
	pipenv run pytest