import numpy as np
import cv2
from mss import mss

#need to add pressing attack to check range

def rangeCheck(img):

    isInRange = False

    # text is red so we will mask for red
    inRangeTextImg = img[20:50, 800:1100]
    lower_red = np.array([0, 200, 200])
    upper_red = np.array([20, 255, 255])

    inRangeTextImg = cv2.cvtColor(inRangeTextImg, cv2.COLOR_BGR2HSV)
    redMask = cv2.inRange(inRangeTextImg, lower_red, upper_red)
    #wording = cv2.bitwise_and(inRangeTextImg, inRangeTextImg, mask=redMask)

    _, redContours, _ = cv2.findContours(
        redMask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # max area for health bar is 671

    #print (redContours)

    if (not redContours):

        return True

    else:
        return False
