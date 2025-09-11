from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pandas as pd
import joblib

model = joblib.load("regression.joblib")
app = FastAPI()

class Item(BaseModel):
    size: float
    nb_rooms: int
    garden: bool

@app.post("/predict")
async def predict(item: Item):
    return {"y_pred": int(model.predict(pd.DataFrame({"size": [item.size], "nb_rooms": [item.nb_rooms], "garden": [item.garden]})))}
