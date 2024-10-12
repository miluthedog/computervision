import cv2

# Try capturing video from webcam (0 is usually the default camera)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Error: Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow('Camera', frame)

    esc = cv2.waitKey(30) & 0xff
    if esc == 27:
        break

cap.release()
cv2.destroyAllWindows()