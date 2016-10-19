import cv2

def circlesFromContours(contours, count, frame):

    count = min(count, len(contours))

    for bearingNumber in range(count):

        bearing = contours[bearingNumber]

        ((x, y), radius) = cv2.minEnclosingCircle(bearing)
        M = cv2.moments(bearing)

        if radius > 20:

            try:
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            except ZeroDivisionError:
                print("Zero area circle?")
                continue

            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

    return frame
