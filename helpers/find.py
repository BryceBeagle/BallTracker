import cv2
from helpers import color


def contours(mask):

    return cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]


# Find the center of a contour using moments
def contourCenter(contour):

    moment = cv2.moments(contour)

    try:
        center = (int(moment["m10"] / moment["m00"]), int(moment["m01"] / moment["m00"]))
    except ZeroDivisionError:
        print("Zero area circle?")
        return

    return center


# Finds the yellow markers on the feet of the robot
def yellowMarkers(frame):

    yellowFrame       = color.isolate(frame, *color.yellowRange)[0]

    # Dilate and erode to reduce noise
    yellowFrameDilate = cv2.erode(yellowFrame, None, iterations=2)
    yellowFrameDilate = cv2.dilate(yellowFrameDilate, None, iterations=2)

    yellowMask        = cv2.split(yellowFrameDilate)[2]

    yellowThresh      = cv2.threshold(yellowMask, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    yellowContours    = contours(yellowThresh.copy())
    yellowContours    = sorted(yellowContours, key=cv2.contourArea, reverse=True)

    return yellowContours[0 : 1]
