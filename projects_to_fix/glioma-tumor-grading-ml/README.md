# 🧠 Glioma Tumor Grading (ML)

A specialized Machine Learning application for oncological risk assessment. This system predicts the grade of glioma tumors (LGG vs. GBM) using clinical data and molecular markers (IDH1, TP53, ATRX, etc.).

## 🚀 Features
*   **Precision Model**: Uses a Random Forest classifier with **SMOTE** oversampling to handle class imbalance.
*   **FastAPI Backend**: Efficient REST API for real-time patient risk profiling.
*   **Interactive UI**: A Streamlit dashboard designed for clinical decision support.
*   **Standardized Pipeline**: Clear separation between data processing, training, and inference.

## 🏗️ Structure
```text
├── train.py          # Training script with SMOTE and Scaling
├── app.py            # FastAPI inference engine
├── ui.py             # Streamlit clinical dashboard
├── requirements.txt  # Dependencies
├── model.pkl         # Trained model
└── scaler.pkl        # Data scaler
```

## 🛠️ Installation

1. Clone:
```bash
git clone https://github.com/mstfyshrqawy520-alt/glioma-tumor-grading-ml.git
cd glioma-tumor-grading-ml
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
