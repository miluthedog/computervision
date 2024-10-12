import cv2

trainedData = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

videoCam = cv2.VideoCapture(0)

while True:
    status, info = videoCam.read()

    color = cv2.cvtColor(info, cv2.COLOR_BGR2GRAY)
    face = trainedData.detectMultiScale(color, 1.1, 4)
    for (x, y, w, h) in face:
        cv2.rectangle(info, (x, y), (x + w, y + h), (0, 255, 255), 2)

    cv2.imshow('image', info)

    esc = cv2.waitKey(30) & 0xff
    if esc == 27:
        break

videoCam.release()
cv2.destroyAllWindows()

