install:
	@pip install -r requirements.txt

docker:
	@docker-compose up -d

run:
	@uvicorn store.main:app --reload

pre-commit:
	@pre-commit install

test:
	@pytest

create-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m $(d)

run-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head