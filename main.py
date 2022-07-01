import uvicorn
import pandas as pd

from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
