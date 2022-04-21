import cv2
import numpy as np


cap = cv2.VideoCapture("d:\\MOV_5702.avi")
a = []

if cap:
    while True:
        ret, frame = cap.read()
        if ret:
            contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            cv2.drawContours(frame, contours, -1, (0, 255, 0), cv2.cv.CV_FILLED, 32)
            try:
                hierarchy = hierarchy[0]
            except:
                hierarchy = []
            for contour, hier in zip(contours, hierarchy):
                (x, y, w, h) = cv2.boundingRect(contour)

                if w > 20 and h > 20:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (180, 0, 0), 1)
                    (x, y, w, h) = cv2.boundingRect(contour)

                    x1 = w / 2
                    y1 = h / 2
                    cx = x + x1
                    cy = y + y1
                    a.append([cx, cy])
                    print(len(a))
                    a = []

            cv2.imshow('BGS', fgmask)
            cv2.imshow('Ori+Bounding Box', frame)
            key = cv2.waitKey(100)
            if key == ord('q'):
                break
cap.release()
cv2.destroyAllWindows()