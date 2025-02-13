import typer
from pathlib import Path
from enum import Enum
import shutil

from .. import logger
from ..modules.data_store import get_data

app = typer.Typer()

class file_types(str, Enum):
    ligand = "ligand"
    enzyme = "enzyme"


@app.command()
def add_files(
    file_path: Path = typer.Argument(
        ...,
        dir_okay=False,
        file_okay=True,
        help="Path to the file to be added to the container.",
    ),
    structure: file_types = typer.Option(
        ...,
        help="Add either a ligand in .sdf format or an enzyme in .pdb format.",
        case_sensitive=False,
        show_choices=True,
        show_default=True,
    )
):
    """
    Add files to the application here. 
    """
    def copy_file(source_path: Path, destination_path: Path):
        try:
            shutil.copy(source_path, destination_path)
            logger.info(f"Copied {source_path} to {destination_path}")
        except shutil.Error as e:
            logger.error(f"Error copying file: {e}")
        except OSError as e:
            logger.error(f"OS error: {e}")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")

    if structure == file_types.ligand:
        destination_path = Path(get_data("shared_volume_path") + "/sdf_ligand_files").resolve()
        copy_file(file_path, destination_path)

    elif structure == file_types.enzyme:
        destination_path = Path(get_data("shared_volume_path") + "/pdb_enzyme_files").resolve()
        copy_file(file_path, destination_path)

@app.command()
def list_files(
    structure: file_types = typer.Option(
        ...,
        help="List either ligand in .sdf format or enzyme in .pdb format.",
        case_sensitive=False,
        show_choices=True,
        show_default=True
    ),
):
    """
    List all files in the shared volume path.
    """
    if structure == file_types.ligand:
        destination_path = Path(get_data("shared_volume_path") + "/sdf_ligand_files").resolve()
        files = list(destination_path.glob("*.sdf"))
        if files:
            logger.info(f"Files in {destination_path}:")
            for file in files:
                logger.info(file.name)
        else:
            logger.info(f"No .sdf files found in {destination_path}")

    elif structure == file_types.enzyme:
        destination_path = Path(get_data("shared_volume_path") + "/pdb_enzyme_files").resolve()
        files = list(destination_path.glob("*.pdb"))
        if files:
            logger.info(f"Files in {destination_path}:")
            for file in files:
                logger.info(file.name)
        else:
            logger.info(f"No .pdb files found in {destination_path}")

