import typer
from pathlib import Path

from . import logger
from .commands import setup_commands, docker_manipulations
from .modules.docker_handler import GeneralDockerMethods

app = typer.Typer()


### Setup and Testing Commands ###
app.add_typer(
    setup_commands.app,
    name="setup",
    help="Commands for setting up and testing the package.",
)

app.add_typer(
    docker_manipulations.app,
    name="docker",
    help="Commands for manipulating the Docker containers.",
)



"""
@app.command()
def 
"""

if __name__ == "__main__":
    app()

