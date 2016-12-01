import cv2

RED_RANGE    = ((165,  80,  35), (180, 255, 255))
YELLOW_RANGE = (( 15,  60, 100), ( 30, 255, 255))
GREEN_RANGE  = (None, None)
BLUE_RANGE   = ((100, 145,  30), (115, 255, 255))

RED    = (  0,   0, 255)
YELLOW = (  0, 255, 255)
GREEN  = (  0, 255,   0)
BLUE   = (255,   0,   0)

colorRanges = {RED    : RED_RANGE,
               YELLOW : YELLOW_RANGE,
               GREEN  : GREEN_RANGE,
               BLUE   : BLUE_RANGE}


def isolate(frame, lowerThreshold, upperThreshold):

    mask = cv2.inRange(frame, lowerThreshold, upperThreshold)
    result = cv2.bitwise_or(frame, frame, mask=mask)

    return result, mask

