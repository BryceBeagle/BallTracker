import cv2

from helpers import color, find


video = cv2.VideoCapture(1)

video.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
video.set(cv2.CAP_PROP_FRAME_WIDTH,  1280)
video.set(cv2.CAP_PROP_FRAME_HEIGHT,  720)

while True:

    _, frame = video.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    _, blueMask = color.isolate(hsv, *color.blueRange)
    # _, redMask  = color.isolate(hsv, *color.red)

    # shifted = cv2.pyrMeanShiftFiltering(blueFrame, 21, 51)

    blueMask = cv2.erode (blueMask, None, iterations=2)
    blueMask = cv2.dilate(blueMask, None, iterations=2)
    # redMask  = cv2.erode (redMask,  None, iterations=2)
    # redMask  = cv2.dilate(redMask,  None, iterations=2)

    cv2.imshow('frame', frame)

    # gray = cv2.cvtColor(blueFrame, cv2.COLOR_BGR2GRAY)

    blueThresh = cv2.threshold(blueMask, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # redThresh  = cv2.threshold(redMask,  0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    blueContours = find.contours(blueThresh.copy())
    # redContours  = find.contours(redThresh.copy())
    print("[INFO] {} blue contours found".format(len(blueContours)))
    # print("[INFO] {} red  contours found".format(len(redContours)))

    for (i, contour) in enumerate(blueContours):

        (x, y), radius = cv2.minEnclosingCircle(contour)
        cv2.putText(frame, "#{}".format(i + 1), (int(x) - 10, int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.drawContours(frame, [contour], -1, (255, 0, 0), 2)


    # for (i, contour) in enumerate(redContours):
    #
    #     (x, y), radius = cv2.minEnclosingCircle(contour)
    #     cv2.putText(frame, "#{}".format(i + 1), (int(x) - 10, int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    #     cv2.drawContours(frame, [contour], -1, (0, 0, 255), 2)

    cv2.imshow('Image', frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break