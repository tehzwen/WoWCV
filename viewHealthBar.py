import numpy as np
import cv2
from mss import mss
from PIL import Image
import time
import os

maxHealth = 671
maxMana = 682


def getCurrentStats(img):

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mana = ""
    health = ""

    lower_blue = np.array([100, 200, 80])
    upper_blue = np.array([120, 255, 255])

    lower_green = np.array([60, 80, 80])
    upper_green = np.array([90, 255, 255])

    blueMask = cv2.inRange(hsv, lower_blue, upper_blue)
    greenMask = cv2.inRange(hsv, lower_green, upper_green)

    manaBar = cv2.bitwise_and(img, img, mask=blueMask)
    healthBar = cv2.bitwise_and(img, img, mask=greenMask)

    _, blueContours, _ = cv2.findContours(
        blueMask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # max area for health bar is 671

    for contour in blueContours:
        manaArea = cv2.contourArea(contour)
        mana = str(int((manaArea/maxMana)*100))

    _, greenContours, _ = cv2.findContours(
        greenMask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # max area for mana bar is 682

    for contour in greenContours:
        healthArea = cv2.contourArea(contour)
        health = str(int((healthArea/maxHealth) * 100))


    return health, mana
