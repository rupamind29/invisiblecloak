# Import Libraries

import numpy as np
import cv2
import time 

cap=cv2.VideoCapture(0)

time.sleep(2)

background = 0

#Capturing the Background
for i in range(30):

    ret, background=cap.read()

while(cap.isOpened()):

    ret, img = cap.read()

    if not ret:
        break

    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # HSV = Huge Saturation Value || 

    #HSV Values for Mask1
    lower_red=np.array([0,120,70])
    upper_red=np.array([10,255,255])
    mask1=cv2.inRange(hsv, lower_red, upper_red) #Seperating the cloack part1

    #HSV Values for Mask2
    lower_red=np.array([170,120,70])
    upper_red=np.array([180,255,255])
    mask2=cv2.inRange(hsv, lower_red, upper_red) #Seperating the cloack part2


    mask1=mask1+mask2 

    mask1=cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations=2) 
    mask1=cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3,3), np.uint8), iterations=1)


    mask2=cv2.bitwise_not(mask1)


    res1=cv2.bitwise_and(background, background, mask=mask1) 
    res2=cv2.bitwise_and(img, img, mask=mask2) 

    final_output=cv2.addWeighted(res1, 1, res2, 1, 0)

    cv2.imshow('Rupam!', final_output)
    k=cv2.waitKey(10)
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()