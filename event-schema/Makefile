dev:
	pip3 install -U pip poetry
	poetry install

format:
	poetry run isort aws_lambda_publish_shared_event tests
	poetry run black aws_lambda_publish_shared_event tests

lint: format
	poetry run flake8 aws_lambda_publish_shared_event/* tests/*

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

security-baseline:
	poetry run bandit -r aws_lambda_publish_shared_event

complexity-baseline:
	$(info Maintenability index)
	poetry run radon mi aws_lambda_publish_shared_event
	$(info Cyclomatic complexity index)
	poetry run xenon --max-absolute C --max-modules A --max-average A aws_lambda_publish_shared_event

mypy:
	poetry run mypy --pretty aws_lambda_publish_shared_event

pr: lint mypy test security-baseline complexity-baseline
