import math


# Distance between two points
def distance(x1, y1, x2, y2):

    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


# Finds average of two points
def average(x1, y1, x2, y2):

    xAve = (x1 + x2) / 2
    yAve = (y1 + y2) / 2

    return xAve, yAve


# For use with the two coordinates of the yellow markers
def origin(x1, y1, x2, y2):

    xAve, yAve = average(x1, y1, x2, y2)

    xOrig = int(xAve + (y1   - yAve))
    yOrig = int(yAve + (xAve -   x1))

    return xOrig, yOrig
