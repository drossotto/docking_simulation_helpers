from pathlib import Path
import argparse
import sys

from pydantic import BaseModel, model_validator, FilePath
import docker
import docker.errors
from docker.models.containers import Container
from Bio import PDB
import logging


logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout
)
logger = logging.getLogger(__name__)


class InputValidator(BaseModel):
    pdb_file: FilePath
    sdf_file: FilePath


def argument_parser(): 
    parser = argparse.ArgumentParser(
        description="Run the DeepGlycanSite single_case_prediction method with a \n protein and a ligand"
    )

    parser.add_argument(
        "--pdb_file",
        default=None,
        help="The file path to your protein structure in PDB format"
    )
    parser.add_argument(
        "--sdf_file",
        default=None,
        help="The file path to your ligand in SDF format"
    )

    args = parser.parse_args()
    return args


class DockerHandler:
    """
    Class to perform actions in the DeepGlycanSite Docker container
    """
    def __init__(self):
        self.client = self.ping_docker_engine()
        self.project_name = "docking_simulation_helpers" #Project root. Can be changed if deepglycansite is ran in a different network
        self.service_name = "deepglycansite"

    @staticmethod
    def ping_docker_engine():
        try:
            client: docker.client.DockerClient = docker.from_env()

            return client
        except Exception as e:
            raise docker.errors.DockerException
        
    @staticmethod
    def copy_to_docker_container(container: Container, src_path: Path, dest_path: str) -> None:
        with open(src_path, 'rb') as file:
            tar_stream = file.read()

        container.put_archive(dest_path, tar_stream)
        return None
    
    @staticmethod
    def copy_from_docker_container(container: Container, local_path: Path, docker_path: str):
        tar_stream, stat = container.get_archive()

        with open(local_path, 'wb') as file:
            for chunk in tar_stream:
                file.write(chunk)

        
    def initialize_docker_container(self):
        app_container: Container = None

        for container in self.client.containers.list(all=True):
            if f"{self.project_name}-{self.service_name}-1" in container.name:
                logger.info(f"Container: {container.name} started")

        
class PDBHandler:
    """
    Class to handle manipulations and storage of the PROTEIN structure
    in PDB format
    """

    def __init__(self, pdb_file_path):
        self.pdb_file_path: Path = pdb_file_path
        self.parser = PDB.PDBParser(
            QUIET=True
        )
        self.structure = self.parser(
            "protein",
            str(self.pdb_file_path)
        )

    def count_residues(self) -> tuple[list[str],int]:
        """
        Returns:
            - int: Returns the number of residues found on the structure
        """
        residues = set()
        for model in self.structure:
            for chain in model:
                for residue in chain:
                    if PDB.is_aa(residue, standard=True):
                        residues.add(residue.get_id())
        
        return (residues, len(residues))

def main():
    docker_handler = DockerHandler()
    if docker_handler.client:
        logger.info(f"Connected to Docker engine: {docker_handler.client}")
    
    args = argument_parser()
    input_validator = InputValidator(
        pdb_file=args.pdb_file,
        sdf_file=args.sdf_file
    )

    for container in docker_handler.client.containers.list(all=True):
        if f"{docker_handler.project_name}-{docker_handler.service_name}-1" in container.name:
            print(f"Container: {container.name} found")

     

if __name__ == "__main__":
    logger.info("Starting DeepGlycanSite single case prediction")
    main()