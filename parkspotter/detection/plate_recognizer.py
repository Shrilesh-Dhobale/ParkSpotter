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

        for(x,y,w,h) in plates:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

            plate_roi = gray[y:y+h, x:x+w]

            _, plate_image = cv2.threshold(plate_roi, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

            config= '--psm 8 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
            #--psm 8 treat image as single word
            #-c tessedit_char_whitelist: Restrict characters to alphanumeric
            try:
                plate_text = pytesseract.image_to_string(plate_image, config=config).strip()
                if re.match(r'^[A-Z0-9]+$', plate_text):
                    if plate_text not in stored_plates:
                        stored_plates.add(plate_text)
                        print("Detected Plate:", plate_text)
                        print("Stored Plates:", stored_plates)
            except Exception as e:
                pass
        cv2.imshow('Webcam Feed', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

