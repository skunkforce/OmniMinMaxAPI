from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.responses import PlainTextResponse
import uvicorn
from pydantic import BaseModel, Field, validator
from typing import List
import json

APP_VERSION = "default"
COMMIT_HASH = "default"
BUILD_DATE = "default"
MAINTAINER = "default"

class Waveform(BaseModel):
    x: List[float]        
    y: List[float]

    @validator('y')
    def check_lengths(cls, y, values):
        if 'x' in values and len(y) != len(values['x']):
            raise ValueError("x and y need to have the same length")
        return y

    def getMin(self):
        return min(self.y) if self.y else None

    def getMax(self):
        return max(self.y) if self.y else None

app = FastAPI()

@app.post("/min/")
async def calculate_min(input: Waveform):
    try:    
        return {"global minimum": input.getMin()}
    except Exception as e:
        return {"Error": str(e)}

@app.post("/max/")
async def calculate_max(input: Waveform):
    try:    
        return {"global maximum": input.getMax()}
    except Exception as e:
        return {"Error": str(e)}
    
@app.get("/version")
async def version():
    """
    This is a debug endpoint that returns the version information of the application.

    Returns:
        dict: A dictionary containing the version information.
    """
    return {
        "app_version": APP_VERSION,
        "commit_hash": COMMIT_HASH,
        "build_date": BUILD_DATE,
        "maintainer": MAINTAINER
    }

@app.post("/to_txt/", response_class=PlainTextResponse)
async def to_txt(request: Request):
    """
    This is a debug endpoint that helps debugging calls to the application.

    Args:
        request (Request): The request object.

    Returns:
        a file with the request in json format
    """
    try:
        request_json = await request.json()
        request_text = json.dumps(request_json, indent=4)
        headers = {"Content-Disposition": "attachment; filename=data.txt"}
        return PlainTextResponse(request_text, headers=headers)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8484)
