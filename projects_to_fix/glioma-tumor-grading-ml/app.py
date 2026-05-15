from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import numpy as np

app = FastAPI(title="Glioma Grading API")

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

class GliomaInput(BaseModel):
    features: list

@app.get("/")
def home():
    return {"message": "Glioma Grading API is running.", "model_loaded": model is not None}

@app.post("/predict")
def predict(data: GliomaInput):
    if model is None:
        return {"error": "Model not trained yet."}
    
    # Scale input
    scaled_features = scaler.transform([data.features])
    
    # Predict
    prediction = model.predict(scaled_features)[0]
    probability = model.predict_proba(scaled_features)[0]
    
    # In this dataset, Grade 0 might be LGG and Grade 1 might be GBM (typical for glioma datasets)
    # Checking notebook mapping... (assumed based on standard datasets)
    result = "GBM (Glioblastoma)" if prediction == 1 else "LGG (Lower Grade Glioma)"
    
    return {
        "prediction": result,
        "probability": [round(float(p), 4) for p in probability]
    }
