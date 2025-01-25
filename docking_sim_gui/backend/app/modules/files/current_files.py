from pathlib import Path
from typing import List
from fastapi import HTTPException, APIRouter

router = APIRouter()

def list_files_in_directory(directory: Path) -> List[str]:
    try:
        if not directory.is_dir():
            raise ValueError(f"The path {directory} is not a directory.")
        
        files = [str(file) for file in directory.iterdir() if file.is_file()]
        return files
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error list files: {str(e)}"
        )

@router.get("/currentfilestorage")
def get_all_files_in_file_upload(directory: Path):
    files = list_files_in_directory(directory=directory)

    return {
        "files": files
    }
