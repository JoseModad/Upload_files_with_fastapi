# Fastapi

from fastapi import FastAPI, UploadFile, File, status
from fastapi.responses import JSONResponse

# Typing

from typing import List


app = FastAPI()


@app.post("/multiple/files")
async def upload_multiple_files(files: List[UploadFile]= File(...)):
    try:
        for file in files:
            with open(file.filename, "wb") as myfile:
                content = await file.read()
                myfile.write(content)
                myfile.close()
                
        return JSONResponse(content = {
            "saved": True
        }, status_code = 200)
                
    except FileNotFoundError :
        return JSONResponse(content = {
            "saved": False
        }, status_code = 404)