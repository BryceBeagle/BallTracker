import cv2


def circlesFromContours(contours, count, frame):

    count = min(count, len(contours))

    for bearing in contours[ : count]:

        (x, y), radius = cv2.minEnclosingCircle(bearing)
        moment = cv2.moments(bearing)

        if 10 < radius < 100:

            try:
                center = (int(moment["m10"] / moment["m00"]), int(moment["m01"] / moment["m00"]))
            except ZeroDivisionError:
                print("Zero area circle?")
                continue

            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

    return frame
