import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle
import os

# Download NLTK data
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

def clean_text(text):
    if not isinstance(text, str):
        return ""
    lm = WordNetLemmatizer()
    ps = PorterStemmer()
    stop_words = set(stopwords.words('english'))
    
    # Remove non-alphanumeric
    review = re.sub('[^a-zA-Z0-9]', ' ', text)
    review = review.lower()
    review = review.split()
    
    # Lemmatize and remove stopwords
    review = [ps.stem(lm.lemmatize(x)) for x in review if x not in stop_words]
    return " ".join(review)

def train():
    # Load dataset
    # Based on notebook, it uses WELFake_Dataset.csv
    csv_path = 'WELFake_Dataset.csv'
    if not os.path.exists(csv_path):
        # Check if it's in the subfolder
        csv_path = 'fake-news-using-n-gram_text_column-main/WELFake_Dataset.csv'
        
    if not os.path.exists(csv_path):
        print("Dataset WELFake_Dataset.csv not found!")
        return

    print("Loading data...")
    df = pd.read_csv(csv_path)
    df = df.dropna()
    
    # Sample for training speed (like in notebook)
    df_0 = df[df['label'] == 0].sample(min(5000, len(df[df['label']==0])))
    df_1 = df[df['label'] == 1].sample(min(5000, len(df[df['label']==1])))
    df = pd.concat([df_0, df_1])
    
    print("Cleaning text...")
    df['clean_text'] = df['text'].apply(clean_text)
    
    X = df['clean_text']
    y = df['label']
    
    # TF-IDF
    tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1, 3))
    X_tfidf = tfidf.fit_transform(X)
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)
    
    # Model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    
    # Save artifacts
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    with open('tfidf.pkl', 'wb') as f:
        pickle.dump(tfidf, f)
        
    print(f"Model trained. Accuracy: {model.score(X_test, y_test):.4f}")

if __name__ == "__main__":
    train()
