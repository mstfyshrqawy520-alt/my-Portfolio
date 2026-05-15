# 🏠 House Rent Price Prediction (ANN)

A production-ready Deep Learning application that predicts house rental prices using an Artificial Neural Network (ANN). This project has been modernized with a **FastAPI** backend and a **Streamlit** interactive frontend.

## 🚀 Features
*   **Deep Learning Model**: Uses a Multi-Layer Perceptron (ANN) built with TensorFlow/Keras.
*   **REST API**: Serving inferences via FastAPI for high performance.
*   **Interactive UI**: A sleek Streamlit dashboard for real-time price estimation.
*   **Automated Pipeline**: Modular scripts for training, API serving, and user interaction.

## 🏗️ Architecture
```text
├── train.py          # Data preprocessing and ANN training
├── app.py            # FastAPI backend for model serving
├── ui.py             # Streamlit frontend for user input
├── requirements.txt  # Project dependencies
└── house_rent_model.h5 # Trained model (generated)
```

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/mstfyshrqawy520-alt/House-Rent-Price-Prediction-ANN.git
cd House-Rent-Price-Prediction-ANN
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚦 How to Run

### 1. Train the Model (Optional)
If you want to retrain the model on the latest data:
```bash
python train.py
```

### 2. Start the Backend (FastAPI)
```bash
uvicorn app:app --reload
```

### 3. Launch the Frontend (Streamlit)
```bash
streamlit run ui.py
```

## 📊 Technical Stack
*   **ML/DL**: TensorFlow, Keras, Scikit-learn, Pandas
*   **Backend**: FastAPI, Uvicorn
*   **Frontend**: Streamlit
*   **Deployment**: Ready for Render/Streamlit Cloud

---
Developed by **Mostafa Elsharqawi**
