"""
This module allows the Command Line Interface to store and manipulate data
such as the project name and such.
"""
import importlib.resources
import dbm
from pathlib import Path
import os

from .. import logger

def get_data_directory():
    """Retrieve the data directory path."""
    try:
        # Access the data directory within the package
        data_dir = importlib.resources.files(__package__) / 'data'
        if data_dir.exists():
            return data_dir
    except Exception:
        pass

    # Fallback to a writable directory if the package data is not accessible
    return Path(os.path.expanduser('~')) / '.docking_simulation_helpers' / 'data'

def store_data(key: str, value: str):
    """Store a key-value pair in the database."""
    data_dir = get_data_directory()
    data_dir.mkdir(parents=True, exist_ok=True)
    db_path = data_dir / 'config.db'

    try:
        with dbm.open(str(db_path), 'c') as db:
            db[key] = value
    except dbm.error as e:
        logger.error(f"Error accessing the database: {e}")

def get_data(key: str) -> str:
    """Retrieve a value by its key from the database."""
    data_dir = get_data_directory()
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