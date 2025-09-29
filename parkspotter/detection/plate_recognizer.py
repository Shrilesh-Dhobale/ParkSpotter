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