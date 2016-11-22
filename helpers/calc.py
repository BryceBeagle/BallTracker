import math
from helpers import distance

# Distance between two points
import cv2


def pythag(x1, y1, x2, y2):

    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


# Average of two points
def average(x1, y1, x2, y2):

    xAve = (x1 + x2) / 2
    yAve = (y1 + y2) / 2

    return xAve, yAve


# For use only with the two yellow marker contours
def origin(yellowMarkers):

    marker1 = contourCenter(yellowMarkers[0])
    marker2 = contourCenter(yellowMarkers[1])

    # marker1 needs to have larger y value
    if marker2[1] < marker1[1]:
        x1, y1 = marker1
        x2, y2 = marker2
    else:
        x1, y1 = marker2
        x2, y2 = marker1

    xAve, yAve = average(x1, y1, x2, y2)

    xOrig = int(xAve + (y1   - yAve))
    yOrig = int(yAve + (xAve -   x1))

    return xOrig, yOrig


def pixelRatio(yellowMarkers):

    marker1 = contourCenter(yellowMarkers[0])
    marker2 = contourCenter(yellowMarkers[1])

    markerDistance = pythag(*marker1, *marker2)

    return distance.BETWEEN_YELLOW / markerDistance


# Find the center of a contour using moments
def contourCenter(contour):

    moment = cv2.moments(contour)

    try:
        center = (int(moment["m10"] / moment["m00"]), int(moment["m01"] / moment["m00"]))
    except ZeroDivisionError:
        print("Zero area circle?")
        return

    return center
