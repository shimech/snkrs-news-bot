install:
	poetry install

run:
	poetry run python ./src/main.py

debug-run:
	poetry run python ./src/main.py --test

stock-run:
	poetry run python ./src/main.py --stock

migrate:
	poetry run python ./src/main.py --migrate
