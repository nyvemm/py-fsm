install:
	poetry install

run:
	poetry run flask run --host=0.0.0.0 --port=8000

test:
	poetry run python -m unittest discover -s . -v
	
up:
	docker-compose up -d --build

down:
	docker-compose down

build:
	docker-compose build
