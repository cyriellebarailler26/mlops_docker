from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()
client = MongoClient('mongo', 27017)
db = client.test_database
collection = db.test_collection


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/add/{fruit}")
async def add_fruit(fruit: str):
    id = collection.insert_one({"fruit": fruit}).inserted_id 
    return {"id": str(id)}

@app.get("/list")
async def list_fruits():
    return {"results": list(collection.find({}, {"_id": False}))}

