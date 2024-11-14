import cv2
import numpy as np
from keras import models
import sys
sys.stdout.reconfigure(encoding='utf-8')

model = models.load_model('testmeomeo.keras')

cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()

    frame_resized = cv2.resize(frame, (128, 128)) / 255.0
    frame_resized = np.expand_dims(frame_resized, axis=0)

    prediction = model.predict(frame_resized)
    confidence = prediction[0][0] * 100
    label = "meo meo" if prediction[0] > 0.5 else "???"

    cv2.putText(frame, f"{label} ({confidence:.2f}%)", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    cv2.imshow('Meo meo finder', frame)

    pressEsc = cv2.waitKey(1) & 0xff
    if pressEsc == 27:
        break

cam.release()
cv2.destroyAllWindows()
