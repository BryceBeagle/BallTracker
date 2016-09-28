import cv2
import numpy as np

video = cv2.VideoCapture(1)

greenLower = (29,  86,   6)
greenUpper = (64, 255, 255)

fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)

while True:

    running, frame = video.read()

    fgmask = fgbg.apply(frame)

    fgmask = cv2.inRange(fgmask, 255, 255)

    # fgmaskTemp = cv2.GaussianBlur(fgmaskTemp)

    cv2.imshow('Mask', fgmask)

    height, width = fgmask.shape[:2]

    _, contours, _ = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    color = cv2.bitwise_and(frame, frame, mask=fgmask)

    for contour in contours:

        if cv2.contourArea(contour) > 1000:
            ((x, y), radius) = cv2.minEnclosingCircle(contour)

            moment = cv2.moments(contour)

            center = (int(moment["m10"] / moment["m00"]), int(moment["m01"] / moment["m00"]))

            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

    cv2.imshow("Frame", frame)
    cv2.imshow("Color", color)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break










