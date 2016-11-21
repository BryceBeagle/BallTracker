import cv2
import math

from helpers import color, find, draw

video = cv2.VideoCapture(1)

video.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
video.set(cv2.CAP_PROP_FRAME_WIDTH,  1280)
video.set(cv2.CAP_PROP_FRAME_HEIGHT,  720)

while True:

    frame = video.read()[1]

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    yellowFrame, _ = color.isolate(hsv, *color.yellowRange)

    yellowFrameDilate = cv2.erode (yellowFrame, None, iterations=2)
    yellowFrameDilate = cv2.dilate(yellowFrameDilate, None, iterations=2)

    yellowMask = cv2.split(yellowFrameDilate)[2]

    yellowThresh = cv2.threshold(yellowMask, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    yellowContours = find.contours(yellowThresh.copy())
    yellowContours = sorted(yellowContours, key=cv2.contourArea, reverse=True)

    frame = draw.circlesFromContours(frame, yellowContours, 2)
    cv2.imshow("Frame",  frame)

    # yellowDistance =

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break