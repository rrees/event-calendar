.PHONY: serve migrate deploy

serve:
	pipenv run python runserver.py

migrate:
	dbmate up

deploy:
	flyctl deploy