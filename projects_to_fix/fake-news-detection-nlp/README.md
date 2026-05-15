# 📰 Fake News Detection (NLP)

A state-of-the-art Natural Language Processing (NLP) system designed to detect disinformation. This project classifies news articles as "REAL" or "FAKE" based on linguistic patterns and semantic features.

## 🚀 Features
*   **NLP Pipeline**: Advanced text cleaning (Lemmatization, Stemming) and TF-IDF vectorization.
*   **Optimized Model**: Logistic Regression classifier trained on a balanced subset of news data.
*   **FastAPI Backend**: Scalable API for real-time news authenticity analysis.
*   **Interactive UI**: A Streamlit dashboard where users can paste article text and receive instant results.

## 🏗️ Structure
```text
├── train.py          # NLP pipeline and model training
├── app.py            # FastAPI inference service
├── ui.py             # Streamlit user interface
├── requirements.txt  # Dependencies
├── model.pkl         # Trained model
└── tfidf.pkl         # TF-IDF vectorizer artifact
```

## 🛠️ Installation

1. Clone:
```bash
git clone https://github.com/mstfyshrqawy520-alt/fake-news-detection-nlp.git
cd fake-news-detection-nlp
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
