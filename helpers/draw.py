import cv2

import helpers.calc
from helpers import find, color


def circlesFromContours(frame, contours, count,
                        outerColor=color.YELLOW, innerColor=color.RED):

    count = min(count, len(contours))

    for contour in contours[ : count]:

        (x, y), radius = cv2.minEnclosingCircle(contour)

        if 10 < radius < 100:

            center = helpers.calc.contourCenter(contour)

            cv2.circle(frame, (int(x), int(y)), int(radius), outerColor,  2)
            cv2.circle(frame,           center,           5, innerColor, -1)

    return frame


def text(frame, string, x, y, textColor=color.GREEN):

    cv2.putText(frame, string, (x + 10, y + 10), cv2.FONT_HERSHEY_PLAIN, 2, textColor)
    return frame
