import cv2
import pytesseract
import re

try:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
except FileNotFoundError:
    print("Tesseract OCR executable not found.")
    exit()

def recognize_and_store_plate():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    plate_cascade_path=cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml'
    plate_cascade = cv2.CascadeClassifier(plate_cascade_path)

    if plate_cascade.empty():
        print("Error: Could not load the cascade classifier.")
        return

    stored_plates= set()
    print("Starting webcam feed. Press 'q' to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame from camera.")
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        plates = plate_cascade.detectMultiScale(gray,scaleFactor=1.2, minNeighbors=5, minSize=(25, 25))