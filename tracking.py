import cv2
import numpy as np

#cap = cv2.VideoCapture(0)
kernel = np.ones((5,5),np.uint8)

while(1):

    # Take each frame
    #_, frame = cap.read()
    frame = cv2.imread("Colors.jpg")
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    #converting to grayscale
    gray= cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
    #converting to binary
    ret,thresh = cv2.threshold(gray,127,255,0)
    # Remove the noise
    #opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    # Repairing the object
    #closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    #finding contours
    #contours, hierarchy = cv2.findContours(thresh,1,2)
    #cnt = contours[0]
    M = cv2.moments(thresh)
    #print M
    if M['m00'] == 0:
        M['m00'] = 0.01
    else:
        M['m00'] = M['m00']
    
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    print cx
    print cy
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    #cv2.imshow('res',opening)
    k = cv2.waitKey(5) & 0xFF
    if k == 10:
        break

cv2.destroyAllWindows()
