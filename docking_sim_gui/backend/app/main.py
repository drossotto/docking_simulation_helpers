import os
from typing import Annotated
from pathlib import Path

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from . import logger
from app.modules.files.current_files import router as current_file_router
from app.modules.files.upload_files import router as upload_file_router

app = FastAPI()

app.mount(
    "/static", 
    StaticFiles(directory="../frontend/dist", html=True), 
    name = "frontend"
)

#Move access to

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

os.makedirs("uploaded_files", exist_ok=True)
    
app.include_router(
    current_file_router, 
    prefix="/files"
)

app.include_router(
    upload_file_router,
    prefix="/files"
)