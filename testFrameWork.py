import numpy as np
import cv2
from mss import mss


def rangeCheck():

    screenWidth = 2000
    screenHeight = 900

    with mss() as sct:
        worldView = {"top": 0, "left": 0,
                     "width": screenWidth, "height": 1100}

        while "Screen capturing":

            # Get raw pixels from the screen, save it to a Numpy array
            img = np.array(sct.grab(worldView))

            # text is red so we will mask for red
            inRangeTextImg = img[0:200, 1400:1900]
            lower_red = np.array([150, 0, 0])
            upper_red = np.array([255, 255, 255])

            inRangeTextImg = cv2.cvtColor(inRangeTextImg, cv2.COLOR_BGR2HSV)
            redMask = cv2.inRange(inRangeTextImg, lower_red, upper_red)
            wording = cv2.bitwise_and(inRangeTextImg, inRangeTextImg, mask=redMask)

            _, redContours, _ = cv2.findContours(
                redMask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

            #print (redContours)

            for contour in redContours:
                redArea = cv2.contourArea(contour)
                #print(redArea)

            # Display the picture
            cv2.imshow("OpenCV/Numpy normal", inRangeTextImg)
            cv2.imshow(" normal", wording)

            # Press "q" to quit
            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break


rangeCheck()
