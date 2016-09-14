default: lint test

install:
	pip install -r requirements.pip

run:
	python main.py

lint:
	find . -name '*.py' -exec pylint --rcfile=.pylintrc {} +

test: run
	python -m unittest discover tests.smoke	
