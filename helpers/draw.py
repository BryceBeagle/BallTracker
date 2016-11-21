import cv2
from helpers import find, color


def circlesFromContours(frame, contours, count):

    count = min(count, len(contours))

    for contour in contours[ : count]:

        (x, y), radius = cv2.minEnclosingCircle(contour)

        if 10 < radius < 100:

            center = find.contourCenter(contour)

            cv2.circle(frame, (int(x), int(y)), int(radius), color.YELLOW, 2)
            cv2.circle(frame, center, 5, color.RED, -1)

    return frame
