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

redo-install:
	poetry install
	poetry build
	pipx install dist/docking_simulation_helpers-0.1.0-py3-none-any.whl --force

list-included:
	unzip -l dist/docking_simulation_helpers-0.1.0-py3-none-any.whl

publish-deepglycansite-docker:
	docker push drossotto/deepglycansite:latest

help:
	@echo "Available commands:"
	@echo "  build          - Build the project"
	@echo "  install        - Install dependencies"
	@echo "  test           - Run tests"
	@echo "  clean          - Remove build artifacts"
	@echo "  help           - Show this help message"
	@echo "  redo-install   - Reinstall the package"
	@echo "  list-included  - List the files included in the wheel"
	@echo "  publish-deepglycansite-docker - Publish the deepglycansite docker image"
	
