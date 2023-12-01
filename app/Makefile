.DEFAULT_GOAL := run

start:
	cd app && docker compose down && docker compose up --build -d
.PHONY:start

stop:
	cd app && docker compose down
.PHONY:stop

