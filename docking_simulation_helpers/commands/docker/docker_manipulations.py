import os

import typer
from tabulate import tabulate
from python_on_whales import docker as py_docker

from ... import logger, PackageDirectory
from ...modules.data_store import get_data, store_data
from ...modules.docker_handler import GeneralDockerMethods

app = typer.Typer()

docker_methods = GeneralDockerMethods()

@app.command()
def return_all_network_status():
    """
    Return the status of all networks in the docker network.
    """
    network_name: str = str(get_data("network_name"))

    logger.info(f"Network name: {network_name}")

    print(
        tabulate(
            [[container.name.split("-")[1], container.status] for container in docker_methods.client.containers.list(all=True) if container.name.startswith(network_name)],
            headers=["Container Name", "Status"],
            tablefmt="grid",
        )
    )


@app.command()
def return_all_networks():
    """
    Return all networks in the docker network.
    """
    print(
        tabulate(
            [[network.name, network.id] for network in docker_methods.client.networks.list()],
            headers=["Network Name"],
            tablefmt="grid",
        )
    )

@app.command()
def initialize_docker_network(
    build: bool = typer.Option(True, help="Rebuild the docker network or not."),
    detach: bool = typer.Option(True, help="Run the docker network in detached mode or not. Unless debugging, do not set to False."),
):
    """
    Initialize the docker network shipped with the python package.
    """
    os.chdir(PackageDirectory().prod_network_directory)

    py_docker.compose.up(
        build=build,
        detach=detach,
    )

    os.chdir(PackageDirectory().package_root_directory)

    store_data("network_name", "prod_network")


    



