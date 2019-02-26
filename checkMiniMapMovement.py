import numpy as np
import cv2
from mss import mss


def checkMapMovement(img, img2):

    originalMiniMapImg = img[50:100, 1780:1900]
    newMiniMapImg = img2[50:100, 1780:1900]

    difference = newMiniMapImg - originalMiniMapImg
    distance = (difference.astype(float)**2).sum(axis=2)

    if (distance.sum() > 100000000):
        #val = (abs(100000000 - distance.sum()))/10
        return True

    else:
        return False

