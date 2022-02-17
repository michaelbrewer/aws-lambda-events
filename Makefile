dev:
	pip3 install -U pipenv
	pipenv install

serve:
	pipenv run mkdocs serve
