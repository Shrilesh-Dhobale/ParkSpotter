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