import math
from helpers import distance

# Distance between two points
import cv2
import numpy as np


def pythag(x1, y1, x2, y2):

    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def displacement(x, y, theta1, ratio):

    theta = theta1 + math.atan(x/y)

    hypot = math.sqrt(x**2 + y**2)

    xPixels = hypot * math.cos(theta)
    yPixels = hypot * math.sin(theta)

    xRatio = xPixels * ratio
    yRatio = yPixels * ratio

    return xRatio, yRatio


def angle(x1, y1, x2, y2):

    if x1 == x2: return math.pi / 2
    else:        return math.atan((y1 - y2) / (x1 - x2))


# Average of two points
def average(x1, y1, x2, y2):

    xAve = (x1 + x2) / 2
    yAve = (y1 + y2) / 2

    return xAve, yAve


# For use only with the two yellow marker contours
def origin(marker1, marker2):

    # Todo: refactor for better use with contour object
    # center1 = contourCenterFromMoment(marker1.contour)
    # center2 = contourCenterFromMoment(marker2.contour)

    # Todo: figure out this issue
    if marker1 is None or marker2 is None:
        return 1, 1

    # marker1 needs to have larger y value
    if marker1.location[1] > marker2.location[1]:
        x1, y1 = marker1.location
        x2, y2 = marker2.location
    else:
        x1, y1 = marker2.location
        x2, y2 = marker1.location

    xAve, yAve = average(x1, y1, x2, y2)

    xOrig = int(xAve + (y1   - yAve))
    yOrig = int(yAve + (xAve -   x1))

    return xOrig, yOrig


def pixelRatio(marker1, marker2, distanceKnown):

    # # Todo: refactor for better use with contour object
    # marker1 = contourCenterFromMoment(marker1.contour)
    # marker2 = contourCenterFromMoment(marker2.contour)

    markerDistance = pythag(*marker1.location, *marker2.location)

    return distanceKnown / markerDistance


# Find the center of a contour using moments
def contourCenterFromMoment(contour):

    moment = cv2.moments(contour)

    try:
        center = (int(moment["m10"] / moment["m00"]), int(moment["m01"] / moment["m00"]))
    except ZeroDivisionError:
        print("Zero area circle?")
        return

    return center


def contourXYR(contour):

    location, radius = cv2.minEnclosingCircle(contour)

    return location, radius


def pixelsToMM(pixel, ratio):

    return pixel * ratio


def coordTransformation(objX, objY, origX, origY, ratio, objZ=0, origZ=0):

    objX  = pixelsToMM(objX,  ratio)
    objY  = pixelsToMM(objY,  ratio)
    objZ  = pixelsToMM(objZ,  ratio)

    origX = pixelsToMM(origX, ratio)
    origY = pixelsToMM(origY, ratio)
    origZ = pixelsToMM(origZ, ratio)


def referenceFrame(markers):

    if len(markers) < 2: return
    from objects.objects import ReferenceFrame

    return ReferenceFrame(*markers)


def rotationMatrix(theta):

    zRot = theta - math.pi/2
    # matrix1 = np.matrix([[math.cos(zRot), -math.sin(zRot), 0],
    #                      [math.sin(zRot),  math.cos(zRot), 0],
    #                      [             0,               0, 1]])
    # matrix2 = np.matrix([[1,  0,  0],
    #                      [0, -1,  0],
    #                      [0,  0, -1]])
    #
    # return np.dot(matrix1, matrix2)

    matrix = np.matrix([[math.cos(zRot),  math.sin(zRot),  0],
                        [math.sin(zRot), -math.cos(zRot),  0],
                        [             0,               0, -1]])

    return matrix


def distanceMatrix(x, y, z=0):

    matrix = np.matrix([[x],
                        [y],
                        [z]])

    return matrix


def homogeneousMatrix(rotMat, dstMat):

    bottomRow = np.matrix([0, 0, 0, 1])
    matrixTemp = np.concatenate((rotMat, dstMat), axis=1)
    matrixTemp = np.concatenate((matrixTemp, bottomRow))

    return matrixTemp


def location(homoMatrix, ratio, x, y, z=0):

    x *= ratio
    y *= ratio
    z *= ratio

    pointMatrix = np.matrix([[x],
                             [y],
                             [z],
                             [1]])
    newPointMatrix = np.dot(homoMatrix, pointMatrix)

    coords = tuple(map(tuple, np.asarray(newPointMatrix).transpose()))[0][:3]

    return coords

