param (
    [string]$task = "help"
)

switch ($task) {
    "build" {
        Write-Host "Building the project..." -ForegroundColor Green
        poetry build
    }
    "install" {
        Write-Host "Installing dependencies..." -ForegroundColor Green
        poetry install
    }
    "test" {
        Write-Host "Running tests..." -ForegroundColor Green
        pytest
    }
    "clean" {
        Write-Host "Cleaning up..." -ForegroundColor Yellow
        Remove-Item -Recurse -Force dist, __pycache__, .pytest_cache -ErrorAction SilentlyContinue
    }
    "help" {
        Write-Host "Available commands:" -ForegroundColor Cyan
        Write-Host "  build          - Build the project"
        Write-Host "  install        - Install dependencies"
        Write-Host "  test           - Run tests"
        Write-Host "  clean          - Remove build artifacts"
        Write-Host "  help           - Show this help message"
        Write-Host "  build-network  - Build the Docker network"
        Write-Host "  redo-install   - Reinstall the package"
        Write-Host "  list-included  - List the files included in the wheel"
        Write-Host "  publish-deepglycansite-docker - Publish the deepglycansite docker image"
    }
    "build-network" {
        Write-Host "Building the network..." -ForegroundColor Green
        docker compose up --build -d
    }
    "list-network" {
        Write-Host "Listing the network..." -ForegroundColor Green
        poetry run docking-help docker return-all-network-status
    }
    "redo-install" {
        if (pipx list | Select-String -Pattern "docking-simulation-helpers") {
            Write-Host "Uninstalling existing package..." -ForegroundColor Yellow
            poetry run pipx uninstall docking-simulation-helpers
        } else {
            Write-Host "No existing package found" -ForegroundColor Yellow
        }
        poetry install
        poetry build
        if (Test-Path "dist") {
            poetry run pipx install dist/docking_simulation_helpers-*.whl
        } else {
            Write-Host "Build directory 'dist' not found" -ForegroundColor Red
        }
    }
    "list-included" {
        Write-Host "Listing the files included in the wheel..." -ForegroundColor Green
        unzip -l dist/docking_simulation_helpers-0.1.0-py3-none-any.whl
    }
    "publish-deepglycansite-docker" {
        Write-Host "Publishing the deepglycansite Docker image..." -ForegroundColor Green
        docker push drossotto/deepglycansite:latest
    }
    default {
        Write-Host "Unknown task: $task" -ForegroundColor Red
    }
}