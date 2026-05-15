from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import numpy as np

app = FastAPI(title="Credit Risk API")

# Load artifacts
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    with open('encoders.pkl', 'rb') as f:
        encoders = pickle.load(f)
    with open('le_target.pkl', 'rb') as f:
        le_target = pickle.load(f)
    with open('features.pkl', 'rb') as f:
        features = pickle.load(f)
except:
    model = None

class CreditInput(BaseModel):
    data: dict

@app.get("/")
def home():
    return {"message": "Credit Risk API is running.", "model_loaded": model is not None}

@app.post("/predict")
def predict(input_data: CreditInput):
    if model is None:
        return {"error": "Model not trained."}
    
    # Convert input to DataFrame
    df_input = pd.DataFrame([input_data.data])
    
    # Encode categorical
    for col, le in encoders.items():
        if col in df_input.columns:
            # Handle unseen labels by mapping to a default or handling error
            try:
                df_input[col] = le.transform(df_input[col])
            except:
                df_input[col] = 0 # Default fallback
                
    # Ensure feature order
    df_input = df_input[features]
    
    # Scale
    scaled = scaler.transform(df_input)
    
    # Predict
    pred = model.predict(scaled)[0]
    prob = model.predict_proba(scaled)[0]
    
    result = le_target.inverse_transform([pred])[0]
    
    return {
        "class": result,
        "confidence": round(float(max(prob)), 4)
    }
