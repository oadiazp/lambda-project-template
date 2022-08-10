run:
	chalice local

lint:
	autopep8 -ri . --exclude .venv
	flake8 --exclude .venv .

test:
	pytest tests/
	behave
