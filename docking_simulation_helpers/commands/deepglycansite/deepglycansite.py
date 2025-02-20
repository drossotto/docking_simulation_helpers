import typer
from pathlib import Path

from ... import logger
from ...modules.data_store import get_data
from ...modules.docker_handler import GeneralDockerMethods

app = typer.Typer()

@app.command()
def single_case_prediction(
    enzyme_file: str = typer.Option(
        ...,
        help="Name of the pdb file to be used for the enzyme. \
        Get a list of pdb files using the files list_files command.",
    ),
    ligand_file: str = typer.Option(
        ...,
        help="Name of the sdf file to be used for the ligand. \
        Get a list of sdf files using the files list_files command.",
    ),
):
    """
    Run the DeepGlycanSite prediction model for a single case.
    """
    docker_methods = GeneralDockerMethods()
    client = docker_methods.client

    container_name = f"{get_data('network_name')}-deepglycansite-1"
    print(f"Container name: {container_name}")

    # Check if the container is running
    if docker_methods.check_if_container_is_running(container_name):
        logger.info(f"Container {container_name} is running.")
    else:
        logger.error(f"Container {container_name} is not running.")
        raise SystemExit(1)
    
    # Check if the files exist within the container
    