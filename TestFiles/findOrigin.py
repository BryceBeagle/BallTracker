import cv2
import math

import helpers.calc
from helpers import find, draw, calc, distance, color

video = cv2.VideoCapture(1)

video.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
video.set(cv2.CAP_PROP_FRAME_WIDTH,  1280)
video.set(cv2.CAP_PROP_FRAME_HEIGHT,  720)

origin = 0, 0

while True:

    frame = video.read()[1]

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    yellowMarkers = find.contourColor(hsv, color.YELLOW_RANGE)[:2]

    if len(yellowMarkers) == 2:
        origin = calc.origin(yellowMarkers)
        mmPerPixel = calc.pixelRatio(yellowMarkers)  # TODO: Remove duplicate call to calc.contourCenter()

    cv2.circle(frame, origin, 3, color.GREEN, 3)

    frame = draw.circlesFromContours(frame, yellowMarkers, 2)
    cv2.imshow("Frame",  frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27: break
