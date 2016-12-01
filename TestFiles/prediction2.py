import cv2

from helpers import color, find, draw

video = cv2.VideoCapture(1)

video.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
video.set(cv2.CAP_PROP_FRAME_WIDTH,  1280)
video.set(cv2.CAP_PROP_FRAME_HEIGHT,  720)

prevLoc = [None] * 1000
predLoc = [None] * 1000

while True:

    frame = video.read()[1]

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    blueBearings = find.contoursOfColor(hsv, color.BLUE_RANGE)

    for bearing in blueBearings:



    frame = draw.circlesFromContours(frame, blueBearings,  6, minRadius=10)

    cv2.imshow('Image', frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
