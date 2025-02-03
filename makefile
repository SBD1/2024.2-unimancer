.PHONY: config build start stop rmv interface

VENV_DIR := $(CURDIR)/.venv
PYTHONPATH=$(CURDIR)/source

config:
	@cp .env.template .env
	@test -d $(VENV_DIR) || python3 -m venv $(VENV_DIR)
	@echo "Python virtual environment criado em $(VENV_DIR)"
	@$(VENV_DIR)/bin/pip install --upgrade pip
	@echo "Dependencias instaladas com sucesso."

build:
	@sudo docker compose up --build

start:
	@sudo docker compose up

stop:
	@sudo docker compose down

rmv:
	@sudo docker compose down -v

int:
	@export PYTHONPATH="./src/"
	@python ./src/__init__.py

int@delete:
	@export PYTHONPATH="./src/"
	@python ./src/__init__.py delete

int@reset:
	@export PYTHONPATH="./src/"
	@python ./src/__init__.py reset

mkdocs@build:
	@mkdocs build