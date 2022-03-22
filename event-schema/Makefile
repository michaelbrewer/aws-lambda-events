dev:
	pip3 install -U pip poetry
	poetry install

format:
	poetry run isort --line-length=120 src tests
	poetry run black --line-length=120 src tests

clean:
	rm -Rf src/build src/aws_lambda_publish_shared_event.egg-info src/dist src/aws_lambda_publish_shared_event/events

build: clean
	cp -Rf  ../docs/events src/aws_lambda_publish_shared_event/
	cd src;  python3 setup.py build sdist bdist_wheel

install: build
	cd src;  python3 setup.py install

publish: build
	cd src; poetry run twine upload dist/*

test:
	poetry run pytest
