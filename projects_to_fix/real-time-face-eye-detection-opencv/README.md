# Real-time Face and Eye Detection

A Computer Vision application that uses **OpenCV** and **Haar Cascade Classifiers** to detect faces and eyes in real-time through a webcam.

## 🚀 Features
- **Real-time Detection**: High-speed processing for webcam feeds.
- **Face Localization**: Automatically draws bounding boxes around detected faces.
- **Eye Localization**: Detects and highlights eyes within the face region.
- **Efficient Inference**: Uses lightweight Haar Cascades for low-latency performance.

## 🛠️ Tech Stack
- **Library**: OpenCV (Open Source Computer Vision Library)
- **Language**: Python
- **Models**: Haar Cascades (xml)

## 📦 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/mstfyshrqawy520-alt/real-time-face-eye-detection-opencv.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Usage
Run the application:
```bash
python app.py
```
*Note: Ensure your webcam is connected.*

## 🧠 How it Works
The system uses pre-trained Haar Cascade XML files provided by OpenCV.
1. The frame is converted to grayscale.
2. The `detectMultiScale` function scans the image for face-like patterns.
3. Once a face is found, the system narrows its search to the face region to find eyes, improving accuracy and speed.

---
Developed by **Mostafa Elsharqawi**
