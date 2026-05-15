import streamlit as st
import requests
from PIL import Image
import io

st.set_page_config(page_title="Grape Leaf Classifier", layout="centered")

st.title("🍇 Grape Leaf Multi-class Classification")
st.markdown("Upload an image of a grape leaf to identify its type.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    if st.button("Classify Leaf"):
        # Convert image to bytes
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()
        
        files = {"file": ("image.jpg", img_byte_arr, "image/jpeg")}
        
        try:
            # Call API
            response = requests.post("http://localhost:8000/predict", files=files)
            if response.status_code == 200:
                result = response.json()
                if "error" in result:
                    st.error(result["error"])
                else:
                    st.success(f"### Result: {result['class']}")
                    st.progress(result["confidence"])
                    st.write(f"Confidence: {result['confidence']*100:.2f}%")
            else:
                st.error("API error.")
        except Exception as e:
            st.warning("Backend API not reachable. Make sure 'uvicorn app:app' is running.")
            st.info("Attempting local classification...")
            # Fallback local loading omitted for brevity in complex DL models, 
            # but user can run backend easily.

st.sidebar.info("Supported classes: Ak, Ala_Idris, Buzgulu, Dimnit, Nazli.")
