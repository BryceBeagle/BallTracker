import cv2
import math

from helpers import find, draw, calc, distance, color

video = cv2.VideoCapture(1)

video.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
video.set(cv2.CAP_PROP_FRAME_WIDTH,  1280)
video.set(cv2.CAP_PROP_FRAME_HEIGHT,  720)

while True:

    frame = video.read()[1]

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    yellowMarkers = find.yellow(hsv)[:2]
    frame = draw.circlesFromContours(frame, yellowMarkers, 2)

    marker1 = find.contourCenter(yellowMarkers[0])
    marker2 = find.contourCenter(yellowMarkers[1])

    # marker1 needs to have larger y value
    if marker2[1] > marker1[1]:
        temp = marker1
        marker1 = marker2
        marker2 = temp

    frame = draw.text(frame, str(marker1), *marker1)
    frame = draw.text(frame, str(marker2), *marker2)

    markerDistance = calc.distance(*marker1, *marker2)
    mmPerPixel = distance.BETWEEN_YELLOW / markerDistance

    origin = calc.origin(*marker1, *marker2)

    cv2.circle(frame, origin, 3, color.GREEN, 3)

    cv2.imshow("Frame",  frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27: break
