import cv2

from TestFiles import colors

video = cv2.VideoCapture(1)

video.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
video.set(cv2.CAP_PROP_FRAME_WIDTH,  1920)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)


while True:

    _, frame = video.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    blueMask = cv2.inRange(hsv, *colors.blue)
    redMask  = cv2.inRange(hsv, *colors.red)

    blueResult = cv2.bitwise_and(frame, frame, mask=blueMask)
    redResult  = cv2.bitwise_and(frame, frame, mask=redMask)
    result     = cv2.bitwise_or(blueResult, redResult)

    cv2.imshow('frame' , frame)
    cv2.imshow('mask'  , redMask)
    cv2.imshow('result', result)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

