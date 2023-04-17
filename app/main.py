from typing import Annotated, Union
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlmodel import Session, SQLModel

from models.WorkoutModel import WorkoutModel
from routers import users
from routers.users import oauth2_scheme
from repositories.database import create_db_and_tables, engine
import uuid


import uvicorn

app = FastAPI()

app.include_router(users.router)







@app.get('/')
def read_root():
    return {"Hello": "World"}

@app.get('/items/{item_id}')
def read_item(item_id: int, token: Annotated[str, Depends(oauth2_scheme)], q: Union[str, None  ] = None):
    return {"item_id": item_id, "q": q}

# @app.post('/workout/import')
# def workout_import(workout: Workout):
#     print(workout)
#     # return {"status": 200}
#     return workout

def test_add():
    workout_1 = WorkoutModel(guid=str(uuid.uuid4()), total_distance=3.14, average_heart_rate=152)
    with Session(engine) as session:
        session.add(workout_1)
        session.commit()

if __name__ == "__main__":
    create_db_and_tables()
    # test_add()
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info", reload="true")
