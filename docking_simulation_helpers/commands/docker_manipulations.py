import typer
from tabulate import tabulate

from .. import logger
from ..modules.data_store import get_data
from ..modules.docker_handler import GeneralDockerMethods

app = typer.Typer()

@app.command()
def return_all_network_status():
    """
    Return the status of all networks in the docker network.
    """
    docker_methods = GeneralDockerMethods()
    network_name: str = str(get_data("network_name"))

    logger.info(f"Network name: {network_name}")

    print(
        tabulate(
            [[container.name.split("-")[1], container.status] for container in docker_methods.client.containers.list(all=True) if container.name.startswith(network_name)],
            headers=["Container Name", "Status"],
            tablefmt="grid",
        )
    )

