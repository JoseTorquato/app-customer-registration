export PYTHONPATH=$(shell pwd)/src/
export PYTHONDONTWRITEBYTECODE=1
export POETRY_VIRTUALENVS_CREATE=false

.PHONY=help

venv:
	@source ./venv/bin/activate

install:
	@python3 -m venv venv
	@source ./venv/bin/activate
	@pip install -r requirements.txt

format:
	@isort src/
	@black src/

lint:
	@isort src/
	@black src/
	@prospector

test:
	@pytest -vv

test-print:
	@pytest -s -vv