# CV Multitask Hub

A unified Computer Vision pipeline built using **Hugging Face Transformers**. This project allows users to perform multiple vision tasks—**Classification, Object Detection, and Segmentation**—within a single, intuitive web interface.

## 🚀 Features
- **Image Classification**: Identify the primary subject of an image using Vision Transformers (ViT).
- **Object Detection**: Detect and bound multiple objects in an image using DETR.
- **Image Segmentation**: Pixel-level mask generation for complex scenes using MaskFormer.
- **Interactive UI**: Real-time processing and visualization powered by Gradio.

## 🛠️ Tech Stack
- **Framework**: Hugging Face Transformers
- **Back-end**: PyTorch
- **Frontend**: Gradio
- **Models**: google/vit-base, facebook/detr-resnet-50, facebook/maskformer-swin

## 📦 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/mstfyshrqawy520-alt/multi-task-computer-vision-huggingface.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Usage
Run the Web App:
```bash
python app.py
```

## 🧠 How it Works
This project leverages the `pipeline` abstraction from Hugging Face, which handles the preprocessing (resizing, normalization), model inference, and post-processing (drawing bounding boxes or generating masks) automatically.

---
Developed by **Mostafa Elsharqawi**
