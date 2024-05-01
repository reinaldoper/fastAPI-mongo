.PHONY: install docker run test 

install:
	@pip install -r requirements.txt

docker:
	@docker-compose up -d

run:
	@uvicorn store.main:app --reload

test:
	@pytest

