import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
import pickle
import os

def train():
    # Load dataset
    csv_path = 'credit_customers in ML/credit_customers .csv'
    if not os.path.exists(csv_path):
        print(f"Dataset not found at {csv_path}!")
        return

    df = pd.read_csv(csv_path)

    # Features and target
    X = df.drop('class', axis=1)
    y = df['class']

    # Impute missing values
    for col in X.columns:
        if X[col].dtype == 'object':
            X[col] = X[col].fillna(X[col].mode()[0])
        else:
            X[col] = X[col].fillna(X[col].mean())

    # Encode categorical features
    encoders = {}
    for col in X.columns:
        if X[col].dtype == 'object':
            le = LabelEncoder()
            X[col] = le.fit_transform(X[col])
            encoders[col] = le

    # Encode target
    le_target = LabelEncoder()
    y = le_target.fit_transform(y) # good=1, bad=0 usually

    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)

    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)

    # Save artifacts
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    with open('scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)
    with open('encoders.pkl', 'wb') as f:
        pickle.dump(encoders, f)
    with open('le_target.pkl', 'wb') as f:
        pickle.dump(le_target, f)
    with open('features.pkl', 'wb') as f:
        pickle.dump(X.columns.tolist(), f)

    print("Model trained and saved!")

if __name__ == "__main__":
    train()
