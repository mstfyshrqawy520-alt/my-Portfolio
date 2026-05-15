# 💳 Credit Customers Risk Analysis

A robust Machine Learning system for financial risk management. This project classifies bank customers into "Good" or "Bad" credit risks based on personal and financial profiles.

## 🚀 Features
*   **Predictive Model**: High-accuracy Random Forest classifier.
*   **Data Pipeline**: Automated handling of missing values and categorical encoding.
*   **FastAPI Backend**: Real-time scoring API for credit decisions.
*   **Streamlit Dashboard**: Interactive interface for customer profiling and risk evaluation.

## 🏗️ Structure
```text
├── train.py          # Data preprocessing and model training
├── app.py            # FastAPI scoring service
├── ui.py             # Streamlit management dashboard
├── requirements.txt  # Dependencies
├── model.pkl         # Trained model
└── encoders.pkl      # Categorical encoders
```

## 🛠️ Installation

1. Clone:
```bash
git clone https://github.com/mstfyshrqawy520-alt/credit-customers-risk-analysis.git
cd credit-customers-risk-analysis
```

2. Install:
```bash
pip install -r requirements.txt
```

## 🚦 How to Run

### 1. Training
```bash
python train.py
```

### 2. Backend
```bash
uvicorn app:app --reload
```

### 3. Frontend
```bash
streamlit run ui.py
```

---
Developed by **Mostafa Elsharqawi**
