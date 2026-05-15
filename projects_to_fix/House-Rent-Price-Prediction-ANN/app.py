from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import numpy as np

app = FastAPI(title="House Rent Prediction API")

# Load model artifacts
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('encoders.pkl', 'rb') as f:
        encoders = pickle.load(f)
    with open('features.pkl', 'rb') as f:
        features = pickle.load(f)
except FileNotFoundError:
    model = None

class HouseInput(BaseModel):
    BHK: int
    Size: float
    Area_Type: str
    City: str
    Furnishing_Status: str
    Tenant_Preferred: str
    Bathroom: int
    Point_of_Contact: str

@app.get("/")
def home():
    return {"message": "House Rent Prediction API is running. Model loaded: " + str(model is not None)}

@app.post("/predict")
def predict(data: HouseInput):
    if model is None:
        return {"error": "Model not trained yet. Run train.py first."}
    
    # Prepare input dataframe
    input_dict = {
        'BHK': [data.BHK],
        'Size': [data.Size],
        'Area Type': [data.Area_Type],
        'City': [data.City],
        'Furnishing Status': [data.Furnishing_Status],
        'Tenant Preferred': [data.Tenant_Preferred],
        'Bathroom': [data.Bathroom],
        'Point of Contact': [data.Point_of_Contact]
    }
    
    df = pd.DataFrame(input_dict)
    
    # Encode categorical features
    for col, le in encoders.items():
        try:
            df[col] = le.transform(df[col])
        except ValueError:
            # Handle unseen categories by using the first known one
            df[col] = le.transform([le.classes_[0]])

    # Reorder columns to match training
    df = df[features]
    
    prediction = model.predict(df)[0]
    return {"predicted_rent": round(float(prediction), 2)}
