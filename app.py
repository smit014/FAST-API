from fastapi import FastAPI,HTTPException
from typing import Union,Optional,List
from pydantic import BaseModel

class Model(BaseModel):
    item_id: int
    username: str
    q: Optional[str]= None



class User(BaseModel):
    username : str
    texts : str

fake_db = []
app = FastAPI()

@app.get("/")
def read_root():
    return "hello world"

@app.get("/{name}/")
def read_name(names: str |None = None):
    return {"names": names}

@app.get("/users/{}")
def get_user(id: int):
    if id < 0 or id >= len(fake_db):
        raise HTTPException(status_code=404, detail="user not found")
    return fake_db[id]


@app.post("/user/",status_code=201)
def create_id( user :User ):
    user_id = len(fake_db)
    fake_db.append({"id": user_id, "name":user.username, "BIO":user.texts})
    return fake_db[user_id]

@app.post("/item/{id}")
def read_name( id : int, name : str):
    
    return {"id":id, "name":name}

