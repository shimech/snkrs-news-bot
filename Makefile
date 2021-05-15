install:
	poetry install

run:
	poetry run python ./src/main.py

debug:
	poetry run python ./src/main.py --debug

migrate:
	poetry run python ./src/main.py --migrate --debug

test:
	poetry run pytest --verbose -rfs
