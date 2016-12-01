import cv2
from helpers import find, draw, calc, color, robot
from communication import CommunicationProtocol as com
from time import sleep


video = cv2.VideoCapture(1)

video.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
video.set(cv2.CAP_PROP_FRAME_WIDTH,  1280)
video.set(cv2.CAP_PROP_FRAME_HEIGHT,  720)

referenceFrame = None

bot = com.Device('COM5')
base, main, scnd = robot.move(0, 200, 50)
bot.setServo(0, base)
bot.setServo(1, main)
bot.setServo(2, scnd)
bot.setServoDetach(3)

sleep(1.5)
location = None

while True:

    frame = video.read()[1]
    frame = frame[0 : 720, 0 : 1100]

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    yellowMarkers = find.markersOfColor( hsv, color.YELLOW)
    blueBearings  = find.bearingsOfColor(hsv, color.BLUE)

    tempRF = calc.referenceFrame(yellowMarkers[:2])
    if tempRF is not None:
        referenceFrame = tempRF
        # print(referenceFrame.rotationMatrix)

    if referenceFrame:
        cv2.circle(frame, referenceFrame.originP, 3, color.GREEN, 3)
    if yellowMarkers:
        draw.circlesFromContours(frame, yellowMarkers, 2, minRadius=0)
    if blueBearings:
        draw.circlesFromContours(frame, blueBearings,  6, minRadius=15)
    if referenceFrame and blueBearings:
        location = calc.location(referenceFrame.homogeneousMatrix,
                                 referenceFrame.pixelRatio,
                                 *blueBearings[0].location)
        print(location)

    frame = cv2.line(frame, (5, 5), (  5, 100), color.RED, 2)
    frame = cv2.line(frame, (5, 5), (200,   5), color.RED, 2)

    # x2 = int(referenceFrame.originP[0] - referenceFrame.originMM[1] * math.cos(referenceFrame.rotation))
    # y2 = int(referenceFrame.originP[1] + referenceFrame.originMM[0] * math.sin(referenceFrame.rotation))
    # frame = cv2.line(frame, referenceFrame.originP, (x2, y2), color.GREEN, 2)

    cv2.imshow("Frame",  frame)

    k = cv2.waitKey(5) & 0xFF

    if location:
        if k == ord('a'):
            base, main, scnd = robot.move(location[0], location[1], location[2] + 50)
            bot.setServo(0, base)
            bot.setServo(1, main)
            bot.setServo(2, scnd)

    if k == 27: break

