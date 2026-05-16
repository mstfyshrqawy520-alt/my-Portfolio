# DigitGen – VAE Latent Space Explorer

DigitGen is a Deep Learning project that implements a **Variational Autoencoder (VAE)** to generate synthetic handwritten digits. By exploring the **Latent Space**, users can understand how the model represents complex data in a lower-dimensional form.

## 🚀 Features
- **VAE Architecture**: Built with PyTorch using an encoder-decoder structure.
- **Latent Space Exploration**: Navigate a 20-dimensional latent space using real-time sliders.
- **Real-time Generation**: Generate digits instantly based on your latent vector inputs.
- **Interactive UI**: Clean and intuitive interface powered by Streamlit.

## 🛠️ Tech Stack
- **Framework**: PyTorch
- **Frontend**: Streamlit
- **Libraries**: NumPy, Pillow, Torchvision
- **Dataset**: MNIST (Handwritten Digits)

## 📦 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/mstfyshrqawy520-alt/-DigitGen-VAE-Latent-Space-Explorer.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Usage
1. **Train the model** (optional, a pre-trained model is recommended):
   ```bash
   python train.py
   ```
2. **Run the Web App**:
   ```bash
   streamlit run ui.py
   ```

## 🧠 How it Works
The VAE consists of two main parts:
1. **Encoder**: Compresses the 28x28 input image into a mean vector and a standard deviation vector in the latent space.
2. **Decoder**: Samples from the latent distribution and reconstructs the original image.
By manually providing coordinates in the latent space (via sliders), we can "force" the decoder to generate specific types of digits.

---
Developed by **Mostafa Elsharqawi**
