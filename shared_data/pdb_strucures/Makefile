run-help:
	poetry run docking-help --help

build:
	poetry build

install:
	poetry install

build-network:
	docker compose up --build -docker

test:
	pytest

clean:
	rm -rf dist __pycache__ .pytest_cache

help:
	@echo "Available commands:"
	@echo "  build          - Build the project"
	@echo "  install        - Install dependencies"
	@echo "  test           - Run tests"
	@echo "  clean          - Remove build artifacts"
	@echo "  help           - Show this help message"
	@echo "  build-network  - Build the Docker network"