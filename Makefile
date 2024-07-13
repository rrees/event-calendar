.PHONY: serve

serve:
	pipenv run python runserver.py

migrate:
	dbmate up