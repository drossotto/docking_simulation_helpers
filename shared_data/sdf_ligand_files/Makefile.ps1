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
        Write-Host "  build    - Build the project"
        Write-Host "  install  - Install dependencies"
        Write-Host "  test     - Run tests"
        Write-Host "  clean    - Remove build artifacts"
        Write-Host "  help     - Show this help message"
        Write-Host "  build-network - Build the Docker network"
    }
    "build-network" {
        Write-Host "Building the network..." -ForegroundColor Green
        docker compose up --build -d
    }
    "list-network" {
        Write-Host "Listing the network..." -ForegroundColor Green
        poetry run docking-help docker return-all-network-status
    }
    default {
        Write-Host "Unknown task: $task" -ForegroundColor Red
    }
}
