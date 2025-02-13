import typer

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

    containers_found = False
    for container in docker_methods.client.containers.list(all=True):
        if container.name.startswith(network_name):
            logger.info(f"Container {container.name.split('-')[1]} is {container.status}")
            containers_found = True
    if not containers_found:
        logger.info(f"No containers found in the network {network_name}. Try setting the network name with 'set-network-name'. "
                    "Or try running the 'docker-compose up' command in the root directory of the project.")
        
    