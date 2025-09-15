from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from PIL import Image
import io
import keras
import numpy as np

model = keras.saving.load_model(f"model_2025-05-28_10-54_valacc0.8134.keras")
classes = {
    0: 'coastguard',
    1: 'containership',
    2: 'corvette',
    3: 'cruiser',
    4: 'cv',
    5: 'destroyer',
    6: 'ferry',
    7: 'methanier',
    8: 'sailing',
    9: 'smallfish',
    10: 'submarine',
    11: 'tug', 
    12: 'vsmallfish'
}

app = FastAPI()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image_array = np.array(Image.open(io.BytesIO(image_bytes)))
    X = np.expand_dims(image_array, axis=0)
    y_prob = model.predict(X)
    y_class = np.argmax(y_prob, axis=1)[0]
    return JSONResponse({
        "predicted_class": classes[int(y_class)],
        "probabilities": {classes[i]: float(prob) for i, prob in enumerate(y_prob[0])}
        })
