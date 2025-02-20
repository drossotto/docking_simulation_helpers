import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

import importlib.resources


class PackageDirectory:
    def __init__(self):
        self.package_root_directory = importlib.resources.files(__package__)
        self.data_directory = self.package_root_directory / "data"
        self.prod_network_directory = self.package_root_directory / "prod_network"

