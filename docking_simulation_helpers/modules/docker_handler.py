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
    
    def execute_command_in_container(
        self,
        container_name: str,
        command: str,
        detach: bool = False,
    ) -> tuple[int, str]:
        """
        Execute a command within a docker container.
        """

        container: docker.models.containers.Container = self.client.containers.get(
            container_name
        )
        
        try:
            exit_code, result = container.exec_run(
                command,
                detach=detach,
            )
        except docker.api.client.APIError as e:
            raise docker.errors.APIError
        except Exception as e:
            raise docker.errors.DockerException
        
        if detach:
            return exit_code, "Command executed in detached mode"
        else:  
            return exit_code, result.decode("utf-8")
        
    def check_if_container_is_running(
        self,
        container_name: str,
    ) -> bool:
        """
        Check if a docker container is running.
        """
        try:
            container: docker.models.containers.Container = self.client.containers.get(
                container_name
            )
            return container.status == "running"
        
        except docker.errors.NotFound:
            return False
        except Exception as e:
            raise docker.errors.DockerException