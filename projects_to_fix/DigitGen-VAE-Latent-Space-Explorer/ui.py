import streamlit as st
import torch
import numpy as np
from PIL import Image
from model import VAE

# Page Config
st.set_page_config(
    page_title="DigitGen - VAE Latent Space Explorer",
    page_icon="🔢",
    layout="centered"
)

# Load Model
@st.cache_resource
def load_model():
    model = VAE()
    try:
        model.load_state_dict(torch.load("vae_mnist.pth", map_location=torch.device('cpu')))
    except FileNotFoundError:
        st.warning("Model weights not found. Please run train.py first or ensure vae_mnist.pth exists.")
    model.eval()
    return model

model = load_model()

# UI Content
st.title("🔢 DigitGen: VAE Latent Space Explorer")
st.markdown("""
Explore the latent space of a Variational Autoencoder (VAE) trained on the MNIST dataset. 
Adjust the sliders below to navigate the 20-dimensional latent space and generate synthetic digits.
""")

# Sliders for Latent Space
st.sidebar.header("Latent Vector (Z)")
z_values = []
for i in range(20):
    val = st.sidebar.slider(f"Dimension {i+1}", -3.0, 3.0, 0.0, step=0.1)
    z_values.append(val)

# Generation
if st.button("Generate Digit"):
    z = torch.tensor(z_values).float().unsqueeze(0)
    with torch.no_grad():
        generated_img = model.decode(z)
    
    # Reshape and post-process
    img_array = generated_img.numpy().reshape(28, 28)
    img_array = (img_array * 255).astype(np.uint8)
    img = Image.fromarray(img_array)
    
    # Display
    st.image(img, caption="Generated Digit", width=300, use_container_width=False)
    
st.info("The sliders represent the 'latent' features that the model has learned to associate with different digit shapes.")
