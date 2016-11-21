import cv2

from helpers import color

# video = cv2.videoCapture(1)

# video.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
# video.set(cv2.CAP_PROP_FRAME_WIDTH,  1280)
# video.set(cv2.CAP_PROP_FRAME_HEIGHT,  720)

while True:

    # _, frame = video.read()
    frame = cv2.imread('testReferencePos.png')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    blueFrame, blueMask = color.isolate(hsv, *color.BLUE_RANGE)
    redFrame,    = color.isolate(hsv, *color.RED_RANGE)

