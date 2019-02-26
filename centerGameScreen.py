import pyautogui
import time

screenWidth = 1800
screenHeight = 900

def centerScreen(coord, positioner):
    
    if (coord > 0):

        #target is centered
        if (abs(screenWidth/2 - coord) < 150):
            pyautogui.keyUp('d')
            pyautogui.keyUp('a')

            return True

        #target is to the right
        elif (coord > screenWidth/2):
            pyautogui.keyDown('d')
            time.sleep(0.05)
            pyautogui.keyUp('d')
            positioner.updateDirection(positioner.direction + 15)
            return False

        #target is to the left
        elif (coord < screenWidth/2):
            pyautogui.keyDown('a')
            time.sleep(0.05)
            pyautogui.keyUp('a')
            positioner.updateDirection(positioner.direction - 15)
            return False


def releaseControls():
    pyautogui.keyUp('d')
    pyautogui.keyUp('a')