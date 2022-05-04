dev:
	pip3 install -U pipenv
	pipenv install

serve:
	pipenv run mkdocs serve

build:
	pipenv run mkdocs build

update-requirements:
	pipenv requirements  > requirements.txt

deploy:
	pipenv run mkdocs gh-deploy --force

clean:
	rm -Rf site/
	pipenv --rm
