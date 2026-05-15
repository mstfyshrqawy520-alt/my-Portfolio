import streamlit as st
import pandas as pd
import numpy as np
import requests
import pickle

st.set_page_config(page_title="Glioma Grading Tool", layout="wide")

st.title("🧠 Glioma Tumor Grading System")
st.markdown("Predict the grade of a Glioma tumor based on clinical and genetic markers.")

# Load features to get names
try:
    with open('features.pkl', 'rb') as f:
        feature_names = pickle.load(f)
except:
    feature_names = []

if not feature_names:
    st.error("Please run 'python train.py' first to generate model artifacts.")
    st.stop()

# Define categories
clinical_features = ['Gender', 'Age_at_diagnosis', 'Race']
genetic_features = [f for f in feature_names if f not in clinical_features]

st.sidebar.header("Patient Data")

def get_user_inputs():
    inputs = {}
    
    st.sidebar.subheader("Clinical Info")
    inputs['Gender'] = st.sidebar.selectbox("Gender", options=[0, 1], format_func=lambda x: "Male" if x == 0 else "Female")
    inputs['Age_at_diagnosis'] = st.sidebar.number_input("Age at Diagnosis", min_value=0.0, max_value=120.0, value=50.0)
    inputs['Race'] = st.sidebar.selectbox("Race Code", options=[0, 1, 2, 3]) # Codes from dataset

    st.subheader("Genetic Mutations")
    cols = st.columns(4)
    for i, feature in enumerate(genetic_features):
        with cols[i % 4]:
            inputs[feature] = st.checkbox(f"{feature} Mutation", value=False)
            inputs[feature] = 1 if inputs[feature] else 0
            
    return inputs

user_data = get_user_inputs()

if st.button("Predict Grade", use_container_width=True):
    # Order features
    ordered_features = [user_data[f] for f in feature_names]
    
    payload = {"features": ordered_features}
    
    try:
        response = requests.post("http://localhost:8000/predict", json=payload)
        if response.status_code == 200:
            res = response.json()
            st.success(f"### Prediction: {res['prediction']}")
            
            # Display probabilities
            prob_df = pd.DataFrame({
                "Grade": ["LGG", "GBM"],
                "Probability": res['probability']
            })
            st.bar_chart(prob_df.set_index("Grade"))
        else:
            st.error("API error.")
    except:
        # Fallback
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('scaler.pkl', 'rb') as f:
            scaler = pickle.load(f)
        
        scaled = scaler.transform([ordered_features])
        pred = model.predict(scaled)[0]
        prob = model.predict_proba(scaled)[0]
        
        diag = "GBM (Glioblastoma)" if pred == 1 else "LGG (Lower Grade Glioma)"
        st.success(f"### Prediction: {diag}")
        st.write(f"Confidence: {max(prob)*100:.2f}%")

st.info("LGG: Lower Grade Glioma (Grade II/III). GBM: Glioblastoma (Grade IV).")
