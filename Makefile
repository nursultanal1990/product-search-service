DC = docker compose

.PHONY: build
up:
	${DC} up --build -d

.PHONY: down
down:
	${DC} -f ${APP} down -v

.PHONY: check
check:
	pre-commit run --show-diff-on-failure --color=always --all-files
