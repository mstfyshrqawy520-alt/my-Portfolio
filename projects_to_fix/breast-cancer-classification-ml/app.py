from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import numpy as np

app = FastAPI(title="Breast Cancer Prediction API")

# Load model artifacts
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    with open('features.pkl', 'rb') as f:
        features = pickle.load(f)
except FileNotFoundError:
    model = None

class CancerInput(BaseModel):
    features: list

@app.get("/")
def home():
    return {"message": "Breast Cancer Prediction API is running. Model loaded: " + str(model is not None)}

@app.post("/predict")
def predict(data: CancerInput):
    if model is None:
        return {"error": "Model not trained yet."}
    
    # Scale input
    scaled_features = scaler.transform([data.features])
    
    # Predict
    prediction = model.predict(scaled_features)[0]
    probability = model.predict_proba(scaled_features)[0][1]
    
    result = "Malignant" if prediction == 1 else "Benign"
    
    return {
        "prediction": result,
        "probability_malignant": round(float(probability), 4)
    }
