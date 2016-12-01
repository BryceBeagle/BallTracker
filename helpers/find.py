import cv2

from helpers import color, calc
from objects.objects import *


def bearingsOfColor(hsv, desiredColor):

    bearingObjects = []
    bearings = contoursOfColor(hsv, desiredColor)

    for bearing in bearings:

        bearingObjects.append(Bearing(bearing, desiredColor))

    return bearingObjects


# Todo: Merge with bearingsOfColor somehow. Duplicated code is bad
# http://stackoverflow.com/questions/1436444/python-passing-a-class-name-as-a-parameter-to-a-function
def markersOfColor(hsv, desiredColor):

    markerObjects = []
    markers = contoursOfColor(hsv, desiredColor)

    for marker in markers:

        markerObjects.append(Marker(marker, desiredColor))

    return markerObjects


def contours(mask):

    return cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]


# Finds the yellow markers on the feet of the robot
def contoursOfColor(hsv, desiredColor):

    # Isolate color range
    isolated = color.isolate(hsv, *color.colorRanges.get(desiredColor))[0]

    # Dilate and erode to reduce noise
    dilated = cv2.erode(isolated, None, iterations=1)
    dilated = cv2.dilate(dilated, None, iterations=1)

    grayscale = cv2.split(dilated)[2]

    thresh = cv2.threshold(grayscale, 0, 255, cv2.THRESH_BINARY)[1]

    colorContours = contours(thresh)
    colorContours = sorted(colorContours, key=cv2.contourArea, reverse=True)

    return colorContours
