from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel, Field, validator
from typing import List

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

@app.get("/min/")
async def calculate_min(input: Waveform):
    try:    
        return {"global minimum": input.getMin()}
    except Exception as e:
        return {"Error": str(e)}

@app.get("/max/")
async def calculate_max(input: Waveform):
    try:    
        return {"global maximum": input.getMax()}
    except Exception as e:
        return {"Error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8484)
