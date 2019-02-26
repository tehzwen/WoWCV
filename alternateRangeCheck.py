import numpy as np
import cv2
import time
import pyautogui
from mss import mss


def castRangeCheck(img):

    pyautogui.press('1')
    # time.sleep(2)

    # text is red so we will mask for red
    inRangeTextImg = img[830:880, 800:1100]
    lower_yellow = np.array([20, 200, 200])
    upper_yellow = np.array([50, 255, 255])

    inRangeTextImg = cv2.cvtColor(inRangeTextImg, cv2.COLOR_BGR2HSV)
    yellowMask = cv2.inRange(inRangeTextImg, lower_yellow, upper_yellow)

    lower_red = np.array([0, 200, 200])
    upper_red = np.array([20, 255, 255])

    inRangeTextImg = cv2.cvtColor(inRangeTextImg, cv2.COLOR_BGR2HSV)
    redMask = cv2.inRange(inRangeTextImg, lower_red, upper_red)

    _, yellowContours, _ = cv2.findContours(
        yellowMask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    _, redContours, _ = cv2.findContours(
        redMask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    #cv2.imshow("OpenCV/Numpy normal", inRangeTextImg)

    # Press "q" to quit
    #if cv2.waitKey(25) & 0xFF == ord("q"):
       # cv2.destroyAllWindows()

    if (yellowContours or redContours):
        return True

    else:
        return False
