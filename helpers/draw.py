import cv2

from helpers import find, color, calc


def circlesFromContours(frame, contours, count,
                        outerColor=color.YELLOW, innerColor=color.RED,
                        minRadius=10, maxRadius=100):

    count = min(count, len(contours))

    for contour in contours[ : count]:

        if minRadius < contour.radius < maxRadius:

            center = calc.contourCenterFromMoment(contour.contour)
            cv2.circle(frame, (int(contour.x), int(contour.y)), int(contour.radius), outerColor,  2)
            cv2.circle(frame,                           center,                   5, innerColor, -1)

    return frame


def text(frame, string, x, y, textColor=color.GREEN):

    cv2.putText(frame, string, (x + 10, y + 10), cv2.FONT_HERSHEY_PLAIN, 2, textColor)
    return frame
