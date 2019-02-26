import pygame

class Positioner:

    def __init__(self, surface):
        self.surface = surface
        self.x = 0
        self.y = 0
        self.oldX = 0
        self.oldY = 0
        self.direction = 0
    

    def updateDirection(self, directionVal):

        #if negative val is passed and goes less than zero
        if (self.direction + directionVal < 0):
            self.direction = 360 + directionVal

        #if positive val is passed and goes over 360
        elif (self.direction + directionVal > 360):
            self.direction = 360 - self.direction + directionVal

        else:
            self.direction += directionVal

    def updatePosition(self):
        self.oldX = self.x
        self.oldY = self.y

        if (self.direction == 0):
            self.x += 0
            self.y += 6

        elif (self.direction == 15):
            self.x += 1
            self.y += 5
        
        elif (self.direction == 30):
            self.x += 2
            self.y += 4

        elif (self.direction == 45):
            self.x += 3
            self.y += 3

        elif (self.direction == 60):
            self.x += 4
            self.y += 2

        elif (self.direction == 75):
            self.x += 5
            self.y += 1

        elif (self.direction == 90):
            self.x += 6
            self.y += 0

        elif (self.direction == 105):
            self.x += 5
            self.y += -1

        elif (self.direction == 120):
            self.x += 4
            self.y += -2

        elif (self.direction == 135):
            self.x += 3
            self.y += -3

        elif (self.direction == 150):
            self.x += 2
            self.y += -4

        elif (self.direction == 165):
            self.x += 1
            self.y += -5

        elif (self.direction == 180):
            self.x += 0
            self.y += -6

        elif (self.direction == 195):
            self.x += -1
            self.y += -5

        elif (self.direction == 210):
            self.x += -2
            self.y += -4

        elif (self.direction == 225):
            self.x += -3
            self.y += -3

        elif (self.direction == 240):
            self.x += -4
            self.y += -2

        elif (self.direction == 255):
            self.x += -5
            self.y += -1

        elif (self.direction == 270):
            self.x += -6
            self.y += 0

        elif (self.direction == 285):
            self.x += -5
            self.y += 1

        elif (self.direction == 300):
            self.x += -4
            self.y += 2

        elif (self.direction == 315):
            self.x += -3
            self.y += 3

        elif (self.direction == 330):
            self.x += -2
            self.y += 4

        elif (self.direction == 345):
            self.x += -1
            self.y += 5

        elif (self.direction >= 360):
            self.direction = 0
            self.x += 0
            self.y += 6

    

    def drawLinesFromData(self):
        width, height = self.surface.get_size()
        halfWidth = int(width/2)
        halfHeight = int(height/2)

        pygame.draw.line(self.surface, (0,0,0), (halfWidth + self.oldX, halfHeight + self.oldY), (halfWidth + self.x, halfHeight + self.y), 2)