import cv2
import numpy as np
cap = cv2.VideoCapture('Artillery shell impacts in slow motion_Full-HD.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    framer = cv2.resize(frame, (960, 540))  # Resize image
    cv2.imshow("feed", framer)
    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()


