import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import pickle
import os

def train():
    # Load dataset
    csv_path = 'breast cancer-classifacaton model in ML/breast.csv'
    if not os.path.exists(csv_path):
        print(f"Dataset not found at {csv_path}!")
        return

    df = pd.read_csv(csv_path)

    # Drop non-feature columns
    df = df.drop(columns=['id'])

    # Encode target
    df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B': 0})

    # Split features and target
    X = df.drop('diagnosis', axis=1)
    y = df['diagnosis']

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # Train model
    model = LogisticRegression()
    model.fit(X_train, y_train)

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
