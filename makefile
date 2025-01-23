.PHONY: config build start stop rmv interface

VENV_DIR := .venv 

config:
	@cp .env.template .env
	@test -d $(VENV_DIR) || python3 -m venv $(VENV_DIR)
	@echo "Python virtual environment criado em $(VENV_DIR)"
	@$(VENV_DIR)/bin/pip install --upgrade pip
	@$(VENV_DIR)/bin/pip install -r requirements.txt
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
	@export PYTHONPATH="./source/"
	@python ./source/main.py

int@delete:
	@export PYTHONPATH="./source/"
	@python ./source/main.py delete

int@reset:
	@export PYTHONPATH="./source/"
	@python ./source/main.py reset