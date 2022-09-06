PROJECT?='{{ cookiecutter.project_name }}'

run:
	chalice local

lint:
	autopep8 -ri . --exclude .venv
	flake8 --exclude .venv .

test:
	#pytest tests/
	behave

deploy:
	chalice deploy

clean:
	python clean_functions.py $(PROJECT)

redeploy:
	python clean_functions.py $(PROJECT) && \
 	rm -Rf .chalice/deployed && \
 	chalice deploy

