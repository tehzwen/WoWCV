import os
import time

import cv2
import numpy as np
from mss import mss
from PIL import Image


def getTargetStats(img):

    target = ""

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_yellow = np.array([20, 200, 200])
    upper_yellow = np.array([50, 255, 255])

    lower_red = np.array([0, 200, 200])
    upper_red = np.array([20, 255, 255])

    redMask = cv2.inRange(hsv, lower_red, upper_red)
    enemyTarget = cv2.bitwise_and(img, img, mask=redMask)

    yellowMask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    neutralTarget = cv2.bitwise_and(img, img, mask=yellowMask)

    _, yellowContours, _ = cv2.findContours(
        yellowMask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # max area for health bar is 671

    for contour in yellowContours:
        yellowArea = cv2.contourArea(contour)

        if (yellowArea > 20):
            #print("Looking at neutral unit")
            target = "neutral"

    _, redContours, _ = cv2.findContours(
        redMask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # max area for health bar is 671

    for contour in redContours:
        redArea = cv2.contourArea(contour)

        if (redArea > 20):
            #print("Looking at enemy unit")
            target = "enemy"

    return target
