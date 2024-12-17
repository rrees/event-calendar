
serve:
	pipenv run python runserver.py

migrate:
	dbmate up

deploy:
	flyctl deploy