import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import pickle
import os

def train():
    # Load dataset
    if not os.path.exists('House_Rent_Dataset.csv'):
        print("Dataset not found!")
        return

    df = pd.read_csv('House_Rent_Dataset.csv')

    # Drop columns not easily used in a simple UI for now
    cols_to_drop = ['Posted On', 'Area Locality', 'Floor']
    df = df.drop(columns=[c for c in cols_to_drop if c in df.columns])

    # Handle missing values
    df = df.dropna()

    # Encoding
    encoders = {}
    cat_cols = ['Area Type', 'City', 'Furnishing Status', 'Tenant Preferred', 'Point of Contact']
    
    for col in cat_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le

    # Split features and target
    X = df.drop('Rent', axis=1)
    y = df['Rent']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save model and metadata
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    with open('encoders.pkl', 'wb') as f:
        pickle.dump(encoders, f)
    
    with open('features.pkl', 'wb') as f:
        pickle.dump(X.columns.tolist(), f)

    print("Model trained and saved successfully!")

if __name__ == "__main__":
    train()
