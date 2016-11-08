import cv2

red    = ((165,  80,  35), (180, 255, 255))
blue   = (( 95,  75,  35), (115, 255, 255))


def isolate(frame, lowerThreshold, upperThreshold):

    mask = cv2.inRange(frame, lowerThreshold, upperThreshold)
    result = cv2.bitwise_or(frame, frame, mask=mask)

    return result, mask
