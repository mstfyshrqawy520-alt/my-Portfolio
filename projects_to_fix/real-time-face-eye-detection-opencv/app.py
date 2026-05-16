import cv2 
import numpy as np
import os

# Path to Haar Cascade files
FACE_CASCADE_PATH = 'cascades/haarcascade_frontalface_default.xml'
EYE_CASCADE_PATH = 'cascades/haarcascade_eye.xml'

# Ensure cascades directory exists
if not os.path.exists(FACE_CASCADE_PATH) or not os.path.exists(EYE_CASCADE_PATH):
    print("Error: Cascade files not found in 'cascades/' directory.")
    exit()

face_classifier = cv2.CascadeClassifier(FACE_CASCADE_PATH)
eye_classifier = cv2.CascadeClassifier(EYE_CASCADE_PATH)

def face_and_eye_detector(image):
    # Convert to grayscale for detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detecting faces
    faces = face_classifier.detectMultiScale(gray, 1.2, 5)
    
    for (x, y, w, h) in faces:
        # Draw rectangle around face
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Region of interest for eyes (within the face)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]

        # Detecting eyes
        eyes = eye_classifier.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    
    # Optional: flip image for mirror effect
    image = cv2.flip(image, 1)        
    return image        

def main():
    capture = cv2.VideoCapture(0)
    print("Press 'q' to quit.")

    while True:
        ret, frame = capture.read()
        if not ret:
            break
            
        processed_frame = face_and_eye_detector(frame)
        cv2.imshow("Real-time Face & Eye Detection", processed_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
