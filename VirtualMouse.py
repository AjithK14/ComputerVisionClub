from collections import deque #list-like data structure -- fast appends & pops
import numpy as np
import imutils #resizing frames
import cv2
lower_blue = (90,50,50)
upper_blue = (140,255,255) #initialize color to be detected
pts = deque(maxlen=32) #32 is buffer length -- size of trail increases with length
counter = 0
(dX, dY) = (0, 0)
direction = ""
camera = cv2.VideoCapture("TestVid.mp4")
while True:
	(grabbed, frame) = camera.read() #(boolean,array)
	if not grabbed:
                break
	frame = imutils.resize(frame, width=1000,height=1000)
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, lower_blue, upper_blue)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)[-2]
	center = None
	if len(cnts) > 0:
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
		if radius > 10:
			cv2.circle(frame, (int(x), int(y)), int(radius),
				(0, 255, 255), 2)
			cv2.circle(frame, center, 5, (0, 0, 255), -1)
			pts.appendleft(center)
	for i in np.arange(1, len(pts)):
		if pts[i - 1] is None or pts[i] is None:
			continue
		if counter >= 10 and i == 1 and pts[-10] is not None:
			dX = pts[-10][0] - pts[i][0]
			dY = pts[-10][1] - pts[i][1]
		thickness = int(np.sqrt(32 / float(i + 1)) * 2.5)
		cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	counter += 1
	if key == ord("q"):
		break
camera.release()
cv2.destroyAllWindows()
