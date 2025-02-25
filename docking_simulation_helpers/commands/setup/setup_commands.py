import typer
from pathlib import Path

from ... import logger
from ...modules.data_store import store_data, get_directory, get_data
from ...modules.docker_handler import GeneralDockerMethods

app = typer.Typer()

@app.command()
def hello(name: str = "Davide"):
    """
    A simple command that greets the user. (For testing purposes)
    """
    typer.echo(f"Hello {name}!")

@app.command()
def set_network_name(project_name: str = "docking_simulation_helpers"):
    """
    Set the docker network name. Default should be docking_simulation_helpers.
    """
    store_data("network_name", project_name)
    logger.info(f"Docker network name set to {project_name}")

@app.command()
def return_network_name():
    """
    Provide the docker network name.
    """
    data_dir = get_directory("data")

    logger.info(f"Data directory: {data_dir}")

    logger.info(f"Network name: {str(get_data('network_name'))}")

@app.command()
def set_shared_volume_path(
    folder: Path = typer.Argument(
        ...,
        exists=True,
        file_okay=False,
        dir_okay=True,
        readable=True,
    )
):
    """
    Declare the folder which shares files between the host and the container. 
    """
    store_data("shared_volume_path", str(Path(folder).resolve()))
    logger.info(f"Shared volume path set to {folder}")


@app.command()
def return_shared_volume_path():
    """
    Provide the shared volume path.
    """
    logger.info(f"Shared volume path: {str(get_data('shared_volume_path'))}")