import cv2
import serial
import time

arduino = serial.Serial('COM5', 9600)
time.sleep(2)  # Wait for Arduino to reset

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)

while True:
    status, info = cam.read()
    if not status:
        break

    gray = cv2.cvtColor(info, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5)

    if len(faces) > 0:
        (x, y, w, h) = faces[0] # (x, y) are coord of top left pixel, w h are width height
        cv2.rectangle(info, (x, y), (x+w, y+h), (255, 255, 0), 2) # b-r-g color
        
        frameWidth = info.shape[1] # take width
        centerX = x + w // 2
        normalizedX = int((centerX / frameWidth) * 180)
        
        arduino.write((str(normalizedX) + '\n').encode())

    cv2.imshow('Pha tracking', info)

    pressEsc = cv2.waitKey(1) & 0xff
    if pressEsc == 27:
        break

# Clean up
cam.release()
cv2.destroyAllWindows()
arduino.close()
