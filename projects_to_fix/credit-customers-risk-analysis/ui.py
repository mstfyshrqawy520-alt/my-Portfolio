import streamlit as st
import pandas as pd
import numpy as np
import requests
import pickle

st.set_page_config(page_title="Credit Risk Analyzer", layout="wide")

st.title("💳 Credit Customer Risk Analysis")
st.markdown("Assess the risk of credit customers based on their financial history and status.")

# Load feature info
try:
    with open('features.pkl', 'rb') as f:
        features = pickle.load(f)
    with open('encoders.pkl', 'rb') as f:
        encoders = pickle.load(f)
except:
    features = []

if not features:
    st.error("Please run 'python train.py' first.")
    st.stop()

st.sidebar.header("Customer Profile")

def get_user_inputs():
    inputs = {}
    
    # Split into columns for better layout
    col1, col2, col3 = st.columns(3)
    
    for i, feature in enumerate(features):
        target_col = [col1, col2, col3][i % 3]
        
        if feature in encoders:
            options = list(encoders[feature].classes_)
            inputs[feature] = target_col.selectbox(f"{feature.replace('_', ' ').title()}", options=options)
        else:
            # Numerical
            if feature == 'credit_amount':
                inputs[feature] = target_col.number_input(f"{feature.title()}", min_value=0, value=2500)
            elif feature == 'age':
                inputs[feature] = target_col.number_input(f"{feature.title()}", min_value=18, max_value=100, value=30)
            else:
                inputs[feature] = target_col.number_input(f"{feature.title()}", value=0)
                
    return inputs

user_data = get_user_inputs()

if st.button("Evaluate Risk", use_container_width=True):
    try:
        response = requests.post("http://localhost:8000/predict", json={"data": user_data})
        if response.status_code == 200:
            res = response.json()
            color = "green" if res['class'] == 'good' else "red"
            st.markdown(f"<h2 style='text-align: center; color: {color};'>Risk Result: {res['class'].upper()}</h2>", unsafe_allow_html=True)
            st.metric("Confidence", f"{res['confidence']*100:.2f}%")
        else:
            st.error("API error.")
    except:
        st.warning("API is not running. Please start uvicorn app:app.")

st.sidebar.markdown("---")
st.sidebar.info("This tool predicts whether a customer is a 'Good' or 'Bad' credit risk.")
