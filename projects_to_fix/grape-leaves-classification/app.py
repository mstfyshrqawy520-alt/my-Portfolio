from fastapi import FastAPI, File, UploadFile
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import pickle
import io
from PIL import Image

app = FastAPI(title="Grape Leaf Classification API")

# Load model and labels
try:
    model = tf.keras.models.load_model('grape_leaf_model.h5')
    with open('labels.pkl', 'rb') as f:
        labels = pickle.load(f)
except:
    model = None
    labels = None

@app.get("/")
def home():
    return {"message": "Grape Leaf Classification API is running.", "model_loaded": model is not None}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if model is None:
        return {"error": "Model not loaded. Run train.py first."}
    
    # Read image
    contents = await file.read()
    img = Image.open(io.BytesIO(contents)).convert('RGB')
    img = img.resize((224, 224))
    
    # Preprocess
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    
    # Predict
    predictions = model.predict(img_array)
    class_idx = np.argmax(predictions[0])
    confidence = float(predictions[0][class_idx])
    
    return {
        "class": labels[class_idx],
        "confidence": round(confidence, 4)
    }
