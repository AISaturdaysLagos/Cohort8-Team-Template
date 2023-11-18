.DEFAULT_GOAL := run

activate:
	source ./venv/bin/activate
.PHONY:activate

deactivate:
	deactivate
.PHONY:deactivate

freeze:
	pip freeze > requirements.txt
.PHONY:freeze

install:
	pip install -r requirements.txt
.PHONY:install

run:
	gunicorn --bind 0.0.0.0:5000 wsgi:app
.PHONY:run

start:
	docker-compose up --build -d
.PHONY:start

