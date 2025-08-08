from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd
from fastapi.responses import RedirectResponse


# Load model, scaler, and features
model = joblib.load("model.joblib")
scaler = joblib.load("scaler.joblib")
features = joblib.load("features.pkl")

app = FastAPI()

app.title = "House Price Prediction API"
app.description = "API for predicting house prices based on various features."
@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")

# Define expected input schema based on features
class HouseInput(BaseModel):
    sqft_living: float
    grade: float
    sqft_above: float
    sqft_living15: float
    bathrooms: float
    view: float
    sqft_basement: float
    bedrooms: float
    lat: float

@app.post("/predict")
def predict(data: HouseInput):
    # Convert input to DataFrame
    input_data = pd.DataFrame([data.dict()])

    # Ensure correct feature order
    input_data = input_data[features]

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Predict
    pred_price = model.predict(input_scaled)[0]

    return {
        "predicted_price": float(np.exp(pred_price)) # Convert log price to actual price

    }
