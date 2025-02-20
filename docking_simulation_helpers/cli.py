import typer
from pathlib import Path

from . import logger
from .commands.deepglycansite import deepglycansite
from .commands.docker import docker_manipulations
from .commands.setup import setup_commands
from .commands.files import file_operations


app = typer.Typer()


### Setup and Testing Commands ###
app.add_typer(
    setup_commands.app,
    name="setup",
    help="Commands for setting up and testing the package.",
)

### Docker Manipulation Commands ###
app.add_typer(
    docker_manipulations.app,
    name="docker",
    help="Commands for manipulating the Docker containers.",
)

### Add Files Commands ###
app.add_typer(
    file_operations.app,
    name="files",
    help="Commands for adding files to the application."
)

### DeepGlycanSite Commands ###
app.add_typer(
    deepglycansite.app,
    name="deepglycansite",
    help="Commands for running DeepGlycanSite. Have you added your files and checked your application network?",
)

if __name__ == "__main__":
    app()

