dev:
	pip3 install -U pipenv
	pipenv install

serve:
	pipenv run mkdocs serve

build:
	pipenv run mkdocs build

deploy:
	pipenv run mkdocs gh-deploy --force

clean:
	rm -Rf site/
	pipenv --rm
