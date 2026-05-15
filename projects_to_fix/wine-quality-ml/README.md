# 🍷 Wine Quality ML System

### Production-Ready Machine Learning Web Application

---

## 🚀 Overview

Wine Quality ML System is a production-style Machine Learning application designed to predict wine quality using physicochemical features.

The project demonstrates a complete ML lifecycle including data preprocessing, feature engineering, model training, evaluation, serialization, and deployment through a Flask-based web interface.

This repository reflects practical ML engineering principles rather than experimental notebook-based modeling.

---

## 🎯 Objective

To build a reliable and deployable classification model capable of predicting wine quality based on measurable chemical attributes.

The goal is to simulate a real-world ML deployment workflow.

---

## 🧠 System Architecture

**1. Data Processing Layer**

* Data cleaning
* Feature selection
* Feature scaling using StandardScaler

**2. Modeling Layer**

* Supervised classification algorithms
* Model evaluation & comparison
* Best model selection

**3. Deployment Layer**

* Model serialization (`wine_model.pkl`)
* Scaler serialization (`scaler.pkl`)
* Flask backend for inference
* HTML/CSS frontend for user interaction

---

## 📊 Model Performance

The selected model was evaluated using industry-standard classification metrics:

* Accuracy
* Precision
* Recall
* Confusion Matrix

The final trained model is optimized for inference within the web application.

---

## 🖥 Live Prediction Interface

The application provides a clean user interface where users can input wine attributes and receive real-time quality predictions powered by the trained model.

The backend ensures consistent preprocessing by applying the saved scaler before inference.

---

## 📂 Repository Structure

```
wine-quality-ml/
│
├── app.py
├── wine_model.pkl
├── scaler.pkl
├── Wine_Quality_Prediction_.ipynb
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## ⚙️ Installation & Execution

Clone the repository:

```
git clone <repository-link>
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
python app.py
```

Access the system at:

```
http://127.0.0.1:5000
```

---

## 🛠 Technology Stack

* Python
* Scikit-learn
* Flask
* HTML / CSS
* Pickle

---

## 💡 Engineering Highlights

* Clear separation between training and inference
* Serialized model pipeline
* Web-based inference layer
* Structured project architecture

---

## 🔮 Future Enhancements

* Hyperparameter tuning
* Cross-validation strategy
* Cloud deployment (Render / AWS)
* CI/CD integration

---

## 👨‍💻 Author

Mostafa Sharqawy
AI Engineer | Machine Learning | Deep Learning | AI Systems

---

🚀
