import cv2

from helpers import color, find

video = cv2.VideoCapture(1)

video.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
video.set(cv2.CAP_PROP_FRAME_WIDTH,  1280)
video.set(cv2.CAP_PROP_FRAME_HEIGHT,  720)

prevLoc = [None] * 1000
predLoc = [None] * 1000

while True:

    _, frame = video.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    _, blueMask = color.isolate(hsv, *color.BLUE_RANGE)

    # blueMask = cv2.erode (blueMask, None, iterations=2)
    # blueMask = cv2.dilate(blueMask, None, iterations=2)

    cv2.imshow('frame', frame)

    blueThresh = cv2.threshold(blueMask, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    blueContours = find.contours(blueThresh.copy())

    blueContours = sorted(blueContours, key=cv2.contourArea, reverse=True)

    for (i, contour) in enumerate(blueContours):

        if cv2.contourArea(contour) < 50:
            continue

        (x, y), radius = cv2.minEnclosingCircle(contour)
        cv2.drawContours(frame, [contour], -1, (0, 0, 255), 2)

        x = int(x)
        y = int(y)

        if prevLoc[i] is not None:
            cv2.line(frame, (x, y), prevLoc[i], (255, 0, 0))
            predLoc[i] = ((x + ((x - prevLoc[i][0]) * 5)), (y + (y - prevLoc[i][1]) * 5))
            cv2.circle(frame, predLoc[i], 5, (0, 255, 0), 5)

        prevLoc[i] = (int(x), int(y))

    cv2.imshow('Image', frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
