from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime

from fastapi import HTTPException, APIRouter


router = APIRouter()

def get_file_metadata(file_path: Path) -> Dict[str, Any]:
    metadata = {
        'name': file_path.name,
        'type': "folder" if file_path.is_dir() else "file",
        'size': f"{file_path.stat().st_size / (1024 * 1024):.2f} MB" if file_path.is_file() else None,
        "modified": datetime.fromtimestamp(file_path.stat().st_mtime).strftime("%Y-%m-%d"),
        "url": file_path.as_uri(),
        "children": []
    }
    if file_path.is_dir():
        for item in file_path.iterdir():
            metadata["children"].append(get_file_metadata(item))
    return metadata

@router.get("/currentfilestorage")
def get_all_files_in_file_upload(directory: Path):
    if not directory.is_dir():
        raise HTTPException(status_code=404, detail="Directory not found")
    
    file_tree = get_file_metadata(directory)
    return file_tree
