from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

app = FastAPI(title="Fake News Detection API")

# Load artifacts
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('tfidf.pkl', 'rb') as f:
        tfidf = pickle.load(f)
except:
    model = None

class NewsInput(BaseModel):
    text: str

def clean_text(text):
    lm = WordNetLemmatizer()
    ps = PorterStemmer()
    stop_words = set(stopwords.words('english'))
    review = re.sub('[^a-zA-Z0-9]', ' ', text)
    review = review.lower()
    review = review.split()
    review = [ps.stem(lm.lemmatize(x)) for x in review if x not in stop_words]
    return " ".join(review)

@app.get("/")
def home():
    return {"message": "Fake News Detection API is running.", "model_loaded": model is not None}

@app.post("/predict")
def predict(data: NewsInput):
    if model is None:
        return {"error": "Model not trained."}
    
    cleaned = clean_text(data.text)
    vectorized = tfidf.transform([cleaned])
    prediction = model.predict(vectorized)[0]
    probability = model.predict_proba(vectorized)[0]
    
    # 1 is Real, 0 is Fake (based on WELFake dataset)
    result = "REAL" if prediction == 1 else "FAKE"
    
    return {
        "prediction": result,
        "confidence": round(float(max(probability)), 4)
    }
