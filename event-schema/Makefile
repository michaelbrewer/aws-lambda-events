dev:
	pip3 install -U pip poetry
	poetry install

format:
	poetry run isort --line-length=120 aws_lambda_publish_shared_event tests
	poetry run black --line-length=120 aws_lambda_publish_shared_event tests

clean:
	rm -Rf build aws_lambda_publish_shared_event.egg-info/ dist/ aws_lambda_publish_shared_event/events/ .pytest_cache/ coverage.xml .coverage
	rm -Rf htmlcov/

build: clean
	cp -Rf  ../docs/events aws_lambda_publish_shared_event/
	python3 setup.py build sdist bdist_wheel

install: build
	python3 setup.py install

publish: build
	poetry run twine upload dist/*

test: build
	poetry run pytest --cov=aws_lambda_publish_shared_event --cov-report=xml

coverage-html:
	poetry run pytest --cov=aws_lambda_publish_shared_event --cov-report=html
