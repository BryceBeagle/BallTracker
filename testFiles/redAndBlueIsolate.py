import cv2

from helpers import color
from helpers import draw

numBlue = 3
numRed  = 3

video = cv2.VideoCapture(1)

video.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
video.set(cv2.CAP_PROP_FRAME_WIDTH,  1280)
video.set(cv2.CAP_PROP_FRAME_HEIGHT,  720)

while True:

    _, frame = video.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    blueMask = cv2.inRange(hsv, *color.BLUE_RANGE)
    redMask  = cv2.inRange(hsv, *color.RED_RANGE)

    # blueMask = cv2.erode (blueMask, None, iterations=2)
    # blueMask = cv2.dilate(blueMask, None, iterations=2)

    blueResult = cv2.bitwise_and(frame, frame, mask=blueMask)
    redResult  = cv2.bitwise_and(frame, frame, mask=redMask)
    result     = cv2.bitwise_or(blueResult, redResult)

    blueContours = cv2.findContours(blueMask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    redContours  = cv2.findContours(redMask .copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    # Sort contours if there are more choices than the number of ball bearings
    if len(blueContours) > numBlue:
        blueContours = sorted(blueContours, key=cv2.contourArea, reverse=True)
    if len(redContours) > numRed:
        redContours  = sorted( redContours, key=cv2.contourArea, reverse=True)

    # Draw contours if any
    if len(blueContours) > 0:
        frameTemp = draw.circlesFromContours(blueContours, numBlue, frame)
    else:
        frameTemp = None
    if len(redContours) > 0:
        frame = draw.circlesFromContours(redContours, numRed, frame)
    else:
        frame = frameTemp

    if frameTemp is not None:
        frame = cv2.bitwise_or(frame, frameTemp)

    # Pyramid Mean Shift Filter
    # shifted = cv2.pyrMeanShiftFiltering(result, 21, 51)

    cv2.imshow('frame' , frame)
    cv2.imshow('mask'  , redMask)
    cv2.imshow('result', result)
    # cv2.imshow('Shifted', shifted)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

