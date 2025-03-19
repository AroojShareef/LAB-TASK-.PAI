import cv2
import numpy as np

def detect_features(image_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    
    image = cv2.imread(r"c:\Users\BIT LAPTOP\Downloads\download (1).jpg")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        face_size = w * h
        
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        eye_sizes = []
        eye_distances = []
        
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
            eye_sizes.append(ew * eh)
            
        if len(eyes) >= 2:
            eye_distances.append(abs(eyes[0][0] - eyes[1][0]))
        
        personality = predict_personality(face_size, eye_sizes, eye_distances)
        cv2.putText(image, personality, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    
    cv2.imshow('Face Profiling', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def predict_personality(face_size, eye_sizes, eye_distances):
    if face_size > 50000:
        if len(eye_sizes) > 0 and max(eye_sizes) > 1500:
            return "Extrovert"
        else:
            return "Confident"
    elif len(eye_distances) > 0 and min(eye_distances) < 40:
        return "Introvert"
    return "Balanced"

if __name__ == "__main__":
    detect_features(r'c:\Users\BIT LAPTOP\Downloads\download (1).jpg')  # Replace with your image path
