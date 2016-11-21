from collections import deque

import cv2
import numpy as np

from helpers import color

buffer = 64

points = deque(maxlen=buffer)

video = cv2.VideoCapture(2)

running = True

while running:

    running, frame = video.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, *color.BLUE_RANGE)

    blur = cv2.GaussianBlur(mask, (5,5), 0)
    _, frameOtsu = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    frameOtsu = cv2.erode (frameOtsu, None, iterations=2)
    frameOtsu = cv2.dilate(frameOtsu, None, iterations=2)

    contours = cv2.findContours(frameOtsu.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    if len(contours) > 0:

        circle = max(contours, key=cv2.contourArea)

        ((x, y), radius) = cv2.minEnclosingCircle(circle)

        moment = cv2.moments(circle)

        if radius > 20:

            center = (int(moment["m10"] / moment["m00"]), int(moment["m01"] / moment["m00"]))

            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255),  2)
            cv2.circle(frame,           center,           5, (0,   0, 255), -1)

    points.appendleft(center)

    for i in range(1, len(points)):

        if points[i - 1] is None or points[i] is None:
            continue

        thickness = int(np.sqrt(buffer) / float(i + 1) * 2.5)
        cv2.line(frame, points[i - 1], points[i], (0, 0, 255), thickness)

    cv2.imshow("Frame",     frame)
    cv2.imshow("FrameOtsu", frameOtsu)
    cv2.imshow("Blur",      blur)
    key = cv2.waitKey(1) & 0xFF

    if key == 27: break

video.release()
cv2.destroyAllWindows()
