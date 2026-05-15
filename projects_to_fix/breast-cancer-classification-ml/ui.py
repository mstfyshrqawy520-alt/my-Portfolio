import streamlit as st
import pandas as pd
import numpy as np
import requests

st.set_page_config(page_title="Breast Cancer Diagnostic", layout="wide")

st.title("🩺 Breast Cancer Diagnostic System")
st.markdown("Enter the cell nuclei measurements to predict if the tumor is Malignant or Benign.")

# Categorize features based on the dataset
mean_features = ['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean', 'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean']
se_features = [f.replace('mean', 'se') for f in mean_features]
worst_features = [f.replace('mean', 'worst') for f in mean_features]

all_features = mean_features + se_features + worst_features

st.sidebar.header("Input Parameters")

def user_input_features():
    data = {}
    
    st.sidebar.subheader("Mean Metrics")
    for feature in mean_features:
        data[feature] = st.sidebar.number_input(feature.replace('_', ' ').title(), value=0.0, format="%.4f")
    
    # For simplicity, we'll allow entering SE and Worst metrics in tabs or set defaults
    tab1, tab2 = st.tabs(["Standard Error Metrics", "Worst Metrics"])
    
    with tab1:
        for feature in se_features:
            data[feature] = st.number_input(feature.replace('_', ' ').title(), value=0.0, format="%.4f", key=feature)
            
    with tab2:
        for feature in worst_features:
            data[feature] = st.number_input(feature.replace('_', ' ').title(), value=0.0, format="%.4f", key=feature)
            
    return data

input_data = user_input_features()

if st.button("Run Diagnostic", use_container_width=True):
    # Convert to list in correct order
    try:
        import pickle
        with open('features.pkl', 'rb') as f:
            feature_order = pickle.load(f)
        
        ordered_features = [input_data[f] for f in feature_order]
        
        payload = {"features": ordered_features}
        
        # Call API
        try:
            response = requests.post("http://localhost:8000/predict", json=payload)
            if response.status_code == 200:
                result = response.json()
                
                color = "red" if result['prediction'] == "Malignant" else "green"
                st.markdown(f"<h2 style='text-align: center; color: {color};'>Prediction: {result['prediction']}</h2>", unsafe_allow_html=True)
                st.metric("Probability of Malignancy", f"{result['probability_malignant']*100:.2f}%")
            else:
                st.error("API error.")
        except:
            # Local fallback
            import pickle
            with open('model.pkl', 'rb') as f:
                model = pickle.load(f)
            with open('scaler.pkl', 'rb') as f:
                scaler = pickle.load(f)
            
            scaled = scaler.transform([ordered_features])
            pred = model.predict(scaled)[0]
            prob = model.predict_proba(scaled)[0][1]
            
            diag = "Malignant" if pred == 1 else "Benign"
            color = "red" if diag == "Malignant" else "green"
            st.markdown(f"<h2 style='text-align: center; color: {color};'>Prediction: {diag}</h2>", unsafe_allow_html=True)
            st.metric("Probability of Malignancy", f"{prob*100:.2f}%")
            
    except Exception as e:
        st.error(f"Error: {e}. Make sure to run 'python train.py' first.")

st.info("Note: This tool is for educational purposes and should not be used for actual medical diagnosis.")
