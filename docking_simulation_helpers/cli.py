import typer
from pathlib import Path

from . import logger
from .commands import setup_commands, docker_manipulations, add_files, deepglycansite
from .modules.docker_handler import GeneralDockerMethods


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
    add_files.app,
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

