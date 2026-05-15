import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="House Rent Predictor", layout="wide")

st.title("🏠 House Rent Prediction System")
st.markdown("Enter the details of the house to estimate the monthly rent.")

col1, col2 = st.columns(2)

with col1:
    bhk = st.number_input("BHK", min_value=1, max_value=10, value=2)
    size = st.number_input("Size (sqft)", min_value=100, max_value=10000, value=1000)
    bathroom = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)
    city = st.selectbox("City", ["Kolkata", "Mumbai", "Bangalore", "Delhi", "Chennai", "Hyderabad"])

with col2:
    area_type = st.selectbox("Area Type", ["Super Area", "Carpet Area", "Built Area"])
    furnishing = st.selectbox("Furnishing Status", ["Unfurnished", "Semi-Furnished", "Furnished"])
    tenant = st.selectbox("Tenant Preferred", ["Bachelors/Family", "Bachelors", "Family"])
    contact = st.selectbox("Point of Contact", ["Contact Owner", "Contact Agent", "Contact Builder"])

if st.button("Predict Rent", use_container_width=True):
    payload = {
        "BHK": bhk,
        "Size": size,
        "Area_Type": area_type,
        "City": city,
        "Furnishing_Status": furnishing,
        "Tenant_Preferred": tenant,
        "Bathroom": bathroom,
        "Point_of_Contact": contact
    }
    
    try:
        # Assuming API is running locally on port 8000
        response = requests.post("http://localhost:8000/predict", json=payload)
        if response.status_status == 200:
            result = response.json()
            st.success(f"### Predicted Monthly Rent: ₹{result['predicted_rent']:,}")
        else:
            st.error("Error calling API. Make sure backend is running.")
    except Exception as e:
        # Fallback to direct prediction if API is not available (for simplified deployment)
        st.warning("Backend API not reachable. Attempting local prediction...")
        import pickle
        import os
        
        if os.path.exists('model.pkl'):
            with open('model.pkl', 'rb') as f:
                model = pickle.load(f)
            with open('encoders.pkl', 'rb') as f:
                encoders = pickle.load(f)
            with open('features.pkl', 'rb') as f:
                features = pickle.load(f)
            
            df = pd.DataFrame([payload])
            df.columns = [c.replace('_', ' ') for c in df.columns]
            
            for col, le in encoders.items():
                df[col] = le.transform(df[col])
            
            df = df[features]
            prediction = model.predict(df)[0]
            st.success(f"### Predicted Monthly Rent: ₹{round(float(prediction), 2):,}")
        else:
            st.error("Model artifacts not found. Please run 'python train.py' first.")

st.sidebar.info("This app uses a Machine Learning model (Random Forest) trained on historical rent data.")
