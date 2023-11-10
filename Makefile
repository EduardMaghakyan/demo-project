lint:
	poetry run mypy src/
	poetry run flake8 src/
	poetry run isort --gitignore --check-only src/
	poetry run black --check --diff src/

test: lint
	poetry run pytest src/

tdd:
	poetry run ptw --clear src/

start_api:
	poetry run uvicorn demo_setup.interface.api.main:app --reload

build_image:
	docker build -f Dockerfile -t demo_setup . --rm

run_container_api: build_image
	docker run -p 8000:8000 demo_setup
