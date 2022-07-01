import uvicorn
import pandas as pd

from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()


# Initializing Database
client = AsyncIOMotorClient("mongodb://0.0.0.0:27017/")
db = client.get_database("my_database")
collection = db.get_collection("csv_collection")


async def insert_csv(uploaded_file: UploadFile):
    df = pd.read_csv(uploaded_file.file)
    await collection.insert_many(df.to_dict(orient="records"))


@app.post("/csv/")
async def read_csv(file: UploadFile):
    if file.content_type == "text/csv":
        await insert_csv(file)
        resp_body = jsonable_encoder({"detail": "csv was added to database successfully"})
        return JSONResponse(status_code=202, content=resp_body)
    raise HTTPException(status_code=400, detail="Only CSV")


@app.get("/")
async def get_csv_collection():
    items = [item async for item in collection.find({}, {"_id": False})]
    resp_body = jsonable_encoder(items)
    return JSONResponse(status_code=202, content=resp_body)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
