import datetime
import os
import sys
import time
import cv2
import numpy as np
import pyautogui
import pygame
from mss import mss
from PIL import Image

from centerGameScreen import *
from checkIfTargetSelected import *
from findInRangeOfTarget import *
from findTargetInWorld import *
from viewHealthBar import *
from alternateRangeCheck import *
from positionalData import *
from checkMiniMapMovement import *
from handleMapMovement import *

screenWidth = 1800
screenHeight = 900


def main():

    pygame.init()
    pygame.font.init()
    myfont = pygame.font.SysFont('Arial', 16)

    mapSurface = pygame.Surface((1000, 800))
    mapSurface.fill((100, 100, 100))

    positioner = Positioner(mapSurface)

    size = width, height = 1000, 1000
    white = 255, 255, 255

    rangeChecked = False

    screen = pygame.display.set_mode(size)

    targetCoord = 0
    gameStarted = False
    initialMove = False


    while (not gameStarted):
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.draw.rect(screen, (150, 100, 200), (700, 100, 200, 100))
        mouse = pygame.mouse.get_pos()

            # print (mouse)
        click = pygame.mouse.get_pressed()
        if (mouse[0] >= 700 and mouse[0] <= 900 and mouse[0] >= 100 and mouse[1] <= 200 and click[0] == 1):
            gameStarted = True

        screen.blit(mapSurface, (0, 300))
        pygame.display.flip()


    while gameStarted:

        targetSeen = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        with mss() as sct:
            playerStats = {"top": 20, "left": 20,
                           "width": 200, "height": 80}
            targetStats = {"top": 20, "left": 240,
                           "width": 200, "height": 80}
            worldView = {"top": 100, "left": 0,
                         "width": screenWidth, "height": 900}

            miniMapView = {"top": 0, "left": 0,
                           "width": 2000, "height": 1100}

            playerStatsImg = np.array(sct.grab(playerStats))
            targetStatsImg = np.array(sct.grab(targetStats))
            worldViewImg = np.array(sct.grab(worldView))
            miniMapImg1 = np.array(sct.grab(miniMapView))
            # time.sleep(0.05)
            miniMapImg2 = np.array(sct.grab(miniMapView))

            health, mana = getCurrentStats(playerStatsImg)
            target = getTargetStats(targetStatsImg)

            playerHealthText = myfont.render(
                "Player Health: " + health, False, (0, 0, 0))
            playerManaText = myfont.render(
                "Player Mana: " + mana, False, (0, 0, 0))

            if (target != ""):

                    if (target == "enemy"):
                        coord, canSeeTarget = findTarget(worldViewImg)
                        targetCoord = coord
                        targetSeen = canSeeTarget

                    else:
                        targetSeen = False

            screen.fill(white)

            if (target == "enemy"):
                stopMovement(positioner)

                playerCurrentTarget = myfont.render(
                    "Player Target: " + target, False, (0, 0, 0))
                enemyHealth, enemyMana = getCurrentStats(targetStatsImg)
                currTargetStats = myfont.render(
                    "Target Health: " + enemyHealth, False, (0, 0, 0))
                screen.blit(currTargetStats, (0, 80))

                screen.blit(playerCurrentTarget, (0, 40))

                if (targetSeen and target == "enemy"):
                    losText = myfont.render(
                        "Enemy is in sight", False, (0, 0, 0))
                    screen.blit(losText, (0, 60))
                    isCentered = centerScreen(targetCoord, positioner)

                    if (isCentered):

                        # isInRange = rangeCheck(worldViewImg)
                        if (not rangeChecked):
                            isInRange = castRangeCheck(worldViewImg)

                        # target is in range
                        if (isInRange):
                            rangeChecked = True
                            pyautogui.press('1')

                        # target not in range
                        else:
                            pyautogui.keyDown('w')
                            time.sleep(0.25)
                            pyautogui.keyUp('w')
                            positioner.updatePosition()
                            positioner.drawLinesFromData()

                elif (not targetSeen):
                    losText = myfont.render(
                        "Enemy not in sight", False, (0, 0, 0))
                    screen.blit(losText, (0, 60))

            # no enemy target
            else:
                pyautogui.press('tab')
                rangeChecked = False
                releaseControls()

                #check for another target before we decide to turn and move
                target = getTargetStats(targetStatsImg)

                if (target != "enemy"):

                    moveAboutMap(positioner)
                    # as long as we are moving (not stuck), continue to call movement
                    moving = checkMapMovement(miniMapImg1, miniMapImg2)

                    if (moving):
                        positioner.updatePosition()
                        positioner.drawLinesFromData()

                    else:
                        pyautogui.press('space')
                        moveSideWays(positioner)

            #print (positioner.direction)
            screen.blit(playerHealthText, (0, 0))
            screen.blit(playerManaText, (0, 20))
            screen.blit(mapSurface, (0, 300))
            pygame.display.flip()

        screen.fill(white)



main()
