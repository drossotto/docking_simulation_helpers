"""
This module defines methods to interact with Docker containers.
Should not directly define any commands in the cli. 
"""


import docker
import docker.errors
import docker.models
import docker.models.containers
from .. import logger

class GeneralDockerMethods:
    def __init__(self):
        self.client = self.ping_docker_engine()

    @staticmethod
    def ping_docker_engine():
        try:
            client: docker.client.DockerClient = docker.from_env()

            return client
        
        except Exception as e:
            raise docker.errors.DockerException
        
    @staticmethod
    def place_file_in_container(
        container: docker.models.containers.Container,
        file_path: str,
        destination_path: str,
    ):
        """
        Place a file in a container.
        """

        try:
            with open(file_path, "rb") as file:
                container.put_archive(destination_path, file)

        except Exception as e:
            logger.error(f"Error placing file in container: {e}")

