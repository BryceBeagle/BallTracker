from helpers import calc
import math


class Bearing:

    # def __init__(self, color, location, radius):

    def __init__(self, bearing, color):

        self.contour = bearing

        (self.x, self.y), self.radius = calc.contourXYR(bearing)

        self.color     = color

        self.speed     = None
        self.direction = None

        self.xP        = None
        self.yP        = None

    def getSpeed(self):

        # Todo: maybe add a check to see if already calculated this frame
        if self.xP is None:
            return None
        self.speed = calc.pythag(self.x, self.y, self.xP, self.yP)
        return self.speed

    def getDirection(self):

        # Todo: maybe add a check to see if already calculated this frame
        if self.xP is None:
            return None
        self.direction = math.atan((self.y - self.yP)/(self.x - self.xP))
        return self.direction
