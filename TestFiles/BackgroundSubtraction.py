import cv2

video = cv2.VideoCapture(1)

initialFrame = None

while True:

    running, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if initialFrame is None:
        initialFrame = gray
        continue

    frameChange = cv2.absdiff(initialFrame, gray)
    threshold = cv2.threshold(frameChange, 25, 255, cv2.THRESH_BINARY)[1]

    threshold = cv2.erode (threshold, None, iterations=2)
    threshold = cv2.dilate(threshold, None, iterations=2)

    _, contours, _ = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:

        if cv2.contourArea(contour) > 500:

            ((x, y), radius) = cv2.minEnclosingCircle(contour)

            moment = cv2.moments(contour)

            center = (int(moment["m10"] / moment["m00"]), int(moment["m01"] / moment["m00"]))

            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

    cv2.imshow("Initial Frame", initialFrame)
    cv2.imshow("Frame", frame)
    cv2.imshow("Threshold", threshold)
    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        break
