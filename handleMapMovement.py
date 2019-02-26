import pyautogui
import random
import time

def moveAboutMap(positioner):

    #will check if position has already been visited
    pyautogui.keyDown('w')
    #time.sleep(3)
    #pyautogui.keyUp('w')
    

def stopMovement(positioner):

    pyautogui.keyUp('w')
    

def moveSideWays(positioner):
    choice = random.randint(0,1)

    if (choice == 1):
        pyautogui.keyDown('a')
        time.sleep(0.15)
        pyautogui.keyUp('a')
        positioner.updateDirection(-45)

    else:
        pyautogui.keyDown('d')
        time.sleep(0.15)
        pyautogui.keyUp('d')
        positioner.updateDirection(45)
