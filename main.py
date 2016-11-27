import cv2
from helpers import find, draw, calc, color

video = cv2.VideoCapture(1)

video.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
video.set(cv2.CAP_PROP_FRAME_WIDTH,  1280)
video.set(cv2.CAP_PROP_FRAME_HEIGHT,  720)

origin = 0, 0

while True:

    frame = video.read()[1]


    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    yellowMarkers = find.bearingsOfColor(hsv, color.YELLOW_RANGE)
    blueBearings  = find.bearingsOfColor(hsv, color.BLUE_RANGE)

    if yellowMarkers and len(yellowMarkers) == 2:
        origin     = calc.origin(yellowMarkers)
        mmPerPixel = calc.pixelRatio(yellowMarkers)  # TODO: Remove duplicate call to calc.contourCenterFromMoment()

    cv2.circle(frame, origin, 3, color.GREEN, 3)

    if yellowMarkers:
        frame = draw.circlesFromContours(frame, yellowMarkers, 2, minRadius=5)
    if blueBearings:
        frame = draw.circlesFromContours(frame, blueBearings,  6, minRadius=15)

    frame = cv2.line(frame, (5, 5), (  5, 100), color.RED, 2)
    frame = cv2.line(frame, (5, 5), (200,   5), color.RED, 2)

    cv2.imshow("Frame",  frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27: break

