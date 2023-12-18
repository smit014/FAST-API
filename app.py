from fastapi import FastAPI
from typing import Union,Optional
from pydantic import BaseModel

class Model(BaseModel):
    item_id: int
    username: str
    q: Optional[str]= None

app = FastAPI()

@app.get("/")
def read_root():
    return "hello world"

@app.get("/name/")
def read_name(name: str):
    return {"name": name}

@app.get("/items/{item_id}")
def read_id(item_id : int,username : str):
    return {"item_id": item_id,"username": username}

@app.post("/items/{item_id}")
def create_id(item_id : int , q : Union[str, None] = None):
    return {"item_id": item_id, "message": q}
