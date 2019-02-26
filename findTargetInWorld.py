import numpy as np
import cv2
from mss import mss
from PIL import Image
import time
import os

screenWidth = 1800
screenHeight = 900


def findTarget(img):

    coord = 0
    canSeeTarget = False

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 200, 200])
    upper_red = np.array([20, 255, 255])

    redMask = cv2.inRange(hsv, lower_red, upper_red)
    enemyTarget = cv2.bitwise_and(img, img, mask=redMask)

    _, redContours, _ = cv2.findContours(
        redMask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contour in redContours:
        redArea = cv2.contourArea(contour)

        if (redArea > 1):
            canSeeTarget = True
            indices = np.where(enemyTarget != [0])
            coordinates = list(zip(indices[0], indices[1]))
            coord = coordinates[0][1]


    return coord, canSeeTarget
