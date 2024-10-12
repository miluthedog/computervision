import cv2
import serial
import time

# Replace 'COM3' with your Arduino port
arduino = serial.Serial('COM5', 9600)  # Adjust the port as necessary
time.sleep(2)  # Wait for Arduino to reset

# Load the Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start the video capture
cap = cv2.VideoCapture(0)  # Use 0 for the default camera

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Assuming only one face is detected
    if len(faces) > 0:
        (x, y, w, h) = faces[0]
        # Draw rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Calculate the x-coordinate relative to the frame width
        frame_width = frame.shape[1]
        x_center = x + w // 2
        normalized_x = int((x_center / frame_width) * 180)  # Normalize to 0-180 for the servo
        
        # Send the x-coordinate to Arduino
        arduino.write((str(normalized_x) + '\n').encode())  # Send data with a newline

    cv2.imshow('Face Detection', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
arduino.close()
