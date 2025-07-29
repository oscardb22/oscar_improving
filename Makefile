unit-tests:
	python manage.py test --timing -v 2 --settings='oscar_improving.settings'

bdd-api-tests:
	python manage.py behave --settings='oscar_improving.settings' --simple

lint:
	ruff format --check --force-exclude
	ruff check --select=F,E,W,I --force-exclude --ignore=F403,F405,E722,E721 .

lint-fix:
	ruff format --force-exclude
	ruff check --fix --select=F,E,W,I --force-exclude --ignore=F403,F405,E722,E721 .
