# 🩺 Breast Cancer Classification

A high-precision Machine Learning system for breast cancer diagnostic assistance. This project identifies whether a cell mass is malignant or benign based on clinical measurements.

## 🚀 Features
*   **Predictive Model**: Trained with Scikit-learn (Random Forest) achieving state-of-the-art accuracy.
*   **FastAPI Backend**: A robust REST API serving model inferences.
*   **Streamlit Dashboard**: A user-friendly interface for clinicians to input data and receive diagnostic probabilities.
*   **Scalable Architecture**: Modular code separating training, serving, and UI logic.

## 🏗️ Structure
```text
├── train.py          # Preprocessing and model training script
├── app.py            # FastAPI backend (Inference API)
├── ui.py             # Streamlit web interface
├── requirements.txt  # Project dependencies
└── model.pkl         # Serialized model artifact
```

## 🛠️ Installation

1. Clone:
```bash
git clone https://github.com/mstfyshrqawy520-alt/breast-cancer-classification-ml.git
cd breast-cancer-classification-ml
```

2. Install deps:
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
