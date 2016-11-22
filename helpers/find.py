import cv2

from helpers import color


def contours(mask):

    return cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]


# Finds the yellow markers on the feet of the robot
def contourColor(hsv, colorRange):

    # Isolate color range
    isolated = color.isolate(hsv, *colorRange)[0]

    # Dilate and erode to reduce noise
    dilated = cv2.erode(isolated, None, iterations=2)
    dilated = cv2.dilate(dilated, None, iterations=2)

    mask = cv2.split(dilated)[2]

    thresh = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    colorContours = contours(thresh.copy())
    colorContours = sorted(colorContours, key=cv2.contourArea, reverse=True)

    return colorContours
