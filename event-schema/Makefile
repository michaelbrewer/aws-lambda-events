dev:
	pip3 install -U pip poetry
	poetry install

format:
	poetry run isort --line-length=120 src
	poetry run black --line-length=120 src/*.py

run:
	poetry run python3 src/main.py