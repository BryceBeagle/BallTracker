import cv2
import numpy as np

video = cv2.VideoCapture(1)

while True:

    _, frame = video.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerBlue = np.array([110,  50,  50])
    upperBlue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lowerBlue, upperBlue)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame' , frame)
    cv2.imshow('mask'  , mask)
    cv2.imshow('result', result)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

