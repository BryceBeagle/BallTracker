from helpers import calc, distance
import math


class Bearing:

    def __init__(self, contour, color):

        self.contour = contour

        (x, y), self.radius = calc.contourXYR(contour)
        self.location = int(x), int(y)

        self.color = color

        self.speed     = None
        self.direction = None

        self.prevLocation = None

    def getSpeed(self):

        # Todo: maybe add a check to see if already calculated this frame
        if self.prevLocation is None or self.location is None:
            return None
        self.speed = calc.pythag(*self.location, *self.prevLocation)
        return self.speed

    def getDirection(self):

        # Todo: maybe add a check to see if already calculated this frame
        if self.prevLocation is None or self.location is None:
            return None
        self.direction = calc.angle(*self.location, *self.prevLocation)
        return self.direction


class Marker:

    def __init__(self, contour, color):

        self.contour = contour

        (x, y), self.radius = calc.contourXYR(contour)
        self.location = int(x), int(y)

        self.color = color


class ReferenceFrame:

    def __init__(self, marker1, marker2):

        self.marker1 = marker1
        self.marker2 = marker2

        # marker1.location = 1200, 400
        # marker2.location =  800, 800

        # Todo: perform these calculations only when needed
        self.originP = calc.origin(marker1, marker2)
        # Todo: make better use of tuple unpacking (passed like this because we need atan(x/y)
        self.rotation = -calc.angle(marker1.location[1], marker1.location[0], marker2.location[1], marker2.location[0])

        self.pixelRatio = calc.pixelRatio(self.marker1, self.marker2, distance.BETWEEN_YELLOW)

        self.rotationMatrix = calc.rotationMatrix(self.rotation)

        self.originMM = calc.displacement(*self.originP, self.rotation, self.pixelRatio)
        self.distanceMatrix = calc.distanceMatrix(*self.originMM)

        self.homogeneousMatrix = calc.homogeneousMatrix(self.rotationMatrix, self.distanceMatrix)


