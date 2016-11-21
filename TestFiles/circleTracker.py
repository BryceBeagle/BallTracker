from collections import deque
import numpy as np
import imutils
import cv2

buffer = 64

greenLower = (29,  86,   6)
greenUpper = (64, 255, 255)

blueLower  = ( 90, 120, 100)
blueUpper  = (150, 255, 255)

orangeLower = ( 0, 120, 100)
orangeUpper = (60, 255, 255)

points = deque(maxlen=buffer)

video = cv2.VideoCapture(1)


running = True

while running:

    running, frame = video.read()

    frame = imutils.resize(frame, width=600)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, greenLower, greenUpper)

    mask = cv2.erode (mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    if len(contours) > 0:

        circle = max(contours, key=cv2.contourArea)

        ((x, y), radius) = cv2.minEnclosingCircle(circle)

        M = cv2.moments(circle)

        if radius > 20:

            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

    points.appendleft(center)

    for i in range(1, len(points)):

        if points[i - 1] is None or points[i] is None:
            continue

        thickness = int(np.sqrt(buffer) / float(i + 1) * 2.5)
        cv2.line(frame, points[i - 1], points[i], (0, 0, 255), thickness)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"): break

video.release()
cv2.destroyAllWindows()
