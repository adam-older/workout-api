from typing import Union
from fastapi import FastAPI

import uvicorn

from api.models.Workout import Workout

app = FastAPI()

@app.get('/')
def read_root():
    return {"Hello": "World"}

@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post('/workout/import')
def workout_import(workout: Workout):
    print(workout)
    return {"status": 200}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info", reload="true")