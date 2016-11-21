import cv2
from helpers import find


def circlesFromContours(frame, contours, count):

    count = min(count, len(contours))

    for contour in contours[ : count]:

        (x, y), radius = cv2.minEnclosingCircle(contour)

        if 10 < radius < 100:

            center = find.contourCenter(contour)

            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

    return frame
