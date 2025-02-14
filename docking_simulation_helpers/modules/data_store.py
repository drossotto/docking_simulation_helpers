"""
This module allows the Command Line Interface to store and manipulate data
such as the project name and such.
"""
import importlib.resources
import dbm
from pathlib import Path
import os

from .. import logger, PackageDirectory

def get_directory(directory_name: str) -> Path:
    """Retrieve the data directory path."""
    try:
        # Access the data directory within the package
        data_dir = Path(PackageDirectory().package_root_directory / directory_name).resolve()
        if data_dir.exists():
            return data_dir
    except Exception:
        logger.error(f"Directory {directory_name} does not exist and cannot be accessed.")
        raise Path(PackageDirectory().package_root_directory)

from typing import Union

def get_docker_compose_path() -> Union[Path, None]:
    """Retrieve the path to the Docker Compose file."""
    try:
        prod_network_path = importlib.resources.files(__package__) / 'prod'
        if prod_network_path.exists():
            if (prod_network_path / 'docker-compose.yml').exists():
                return prod_network_path / 'docker-compose.yml'
            else:
                logger.error("Production network path does not contain a Docker Compose file.")

                return None
        else:
            logger.error("Production network path does not exist.")

            return None
    except Exception:
        logger.error("Docker Compose file does not exist and cannot be accessed.")
        return None


    # Fallback to a writable directory if the package data is not accessible
    return Path(os.path.expanduser('~')) / '.docking_simulation_helpers' / 'data'

def store_data(key: str, value: str):
    """Store a key-value pair in the database."""
    data_dir = get_directory("data")
    data_dir.mkdir(parents=True, exist_ok=True)
    db_path = data_dir / 'config.db'

    try:
        with dbm.open(str(db_path), 'c') as db:
            db[key] = value
    except dbm.error as e:
        logger.error(f"Error accessing the database: {e}")

def get_data(key: str) -> str:
    """Retrieve a value by its key from the database."""
    data_dir = get_directory("data")
    db_path = data_dir / 'config.db'

    try:
        with dbm.open(str(db_path), 'r') as db:
            value = db.get(key, None)
            if value is not None:
                return value.decode('utf-8')
            else:
                logger.warning(f"Key '{key}' not found in the database.")
                return None
    except dbm.error as e:
        logger.error(f"Error accessing the database: {e}")
        return None
