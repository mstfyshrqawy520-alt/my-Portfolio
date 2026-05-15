import streamlit as st
import requests

st.set_page_config(page_title="Fake News Detector", layout="centered")

st.title("📰 Fake News Detection System")
st.markdown("Analyze news articles to determine if they are likely to be real or fake.")

news_text = st.text_area("Enter News Article Text:", height=300, placeholder="Paste the news content here...")

if st.button("Check Authenticity", use_container_width=True):
    if news_text.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        with st.spinner("Analyzing text..."):
            try:
                response = requests.post("http://localhost:8000/predict", json={"text": news_text})
                if response.status_code == 200:
                    res = response.json()
                    label = res['prediction']
                    confidence = res['confidence']
                    
                    if label == "REAL":
                        st.success(f"### Result: {label}")
                        st.info(f"Confidence: {confidence*100:.2f}%")
                    else:
                        st.error(f"### Result: {label}")
                        st.warning(f"Confidence: {confidence*100:.2f}%")
                else:
                    st.error("API Error.")
            except:
                st.info("API is not reachable. Ensure 'uvicorn app:app' is running.")

st.sidebar.title("About")
st.sidebar.info("This system uses Natural Language Processing (NLP) and a Logistic Regression classifier to detect fake news articles based on their linguistic patterns.")
