import numpy as np
import cv2
import time
import pygame
import sys
from mss import mss
from positionalData import *


def turnRight(positioner):
    positioner.updateDirection(abs(positioner.direction + 45))

#def turnLeft(positioner):
    

def rangeCheck():
    pygame.init()
    pygame.font.init()
    myfont = pygame.font.SysFont('Arial', 16)

    mapSurface = pygame.Surface((1000, 800))
    mapSurface.fill((100, 100, 100))

    size = width, height = 1000, 1000
    white = 255, 255, 255


    screen = pygame.display.set_mode(size)
    positioner = Positioner(mapSurface)

    while 1:
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        #turnLeft(positioner)


        print (positioner.direction)
        positioner.updateDirection(45)
        positioner.drawLinesFromData()
        positioner.updateDirection(-45)
        #time.sleep(1)



        screen.blit(mapSurface, (0, 300))
        pygame.display.flip()

rangeCheck()
