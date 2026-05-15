import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
import pickle
import os

def train():
    # Load dataset
    csv_path = 'Glioma-Grading-main/dataset.csv'
    if not os.path.exists(csv_path):
        print(f"Dataset not found at {csv_path}!")
        return

    df = pd.read_csv(csv_path)

    # Features and target
    X = df.drop('Grade', axis=1)
    y = df['Grade']

    # Handle missing values if any
    X = X.fillna(X.mean())

    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Oversampling
    smote = SMOTE(random_state=42)
    X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train_res)

    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train_res)

    # Save artifacts
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    with open('scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)
    
    with open('features.pkl', 'wb') as f:
        pickle.dump(X.columns.tolist(), f)

    print("Model trained and saved successfully!")

if __name__ == "__main__":
    train()
