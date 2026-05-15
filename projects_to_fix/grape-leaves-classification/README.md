# 🍇 Grape Leaves Disease Classification

An advanced Deep Learning solution for agricultural diagnostic precision. This application uses computer vision to identify various grape leaf diseases from images.

## 🚀 Features
*   **Deep Learning Model**: Based on the **ResNet50** architecture for high-performance image classification.
*   **Transfer Learning**: Fine-tuned on a specialized dataset of grape leaf pathology.
*   **FastAPI Backend**: Provides a scalable API endpoint for image inference.
*   **Interactive UI**: A Streamlit dashboard where users can upload photos and get instant diagnosis.

## 🏗️ Structure
```text
├── train.py           # Model training and fine-tuning script
├── app.py             # FastAPI inference service
├── ui.py              # Streamlit frontend
├── requirements.txt   # Project dependencies
└── grape_leaf_model.h5 # Trained ResNet50 model
```

## 🛠️ Installation

1. Clone:
```bash
git clone https://github.com/mstfyshrqawy520-alt/grape-leaves-classification.git
cd grape-leaves-classification
```

2. Install deps:
```bash
pip install -r requirements.txt
```

## 🚦 How to Run

### 1. Model Training
```bash
python train.py
```

### 2. Launch Backend
```bash
uvicorn app:app --reload
```

### 3. Launch Frontend
```bash
streamlit run ui.py
```

---
Developed by **Mostafa Elsharqawi**
