from typing import Annotated
from pathlib import Path

from fastapi import APIRouter, UploadFile, File, HTTPException

from ... import logger


router = APIRouter()

@router.post("/upload")
async def store_file(file: Annotated[UploadFile, File()]):
    file_path = Path(f"uploaded_files/{file.filename}").resolve()

    try:
        with open(file_path, "wb") as file_buffer:
            file_buffer.write(await file.read())

        logger.info(f"File {file.filename} uploaded successfully.")
        return {"message": f"File {file.filename} uploaded successfully."}
    
    except Exception as e:
        logger.error(f"Failed to upload {file.filename}: {str(e)}")
        raise HTTPException(
            status_code=500, 
            detail=f"Failed to upload file: {str(e)}")
    
