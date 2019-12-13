import pygame
from pygame.locals import *

class Control():
    def __init__(self):
        self.play = True
        self.direction = "RIGTH"
        self.pause = True

    def control(self):
        for i in pygame.event.get():
            if i.type == QUIT:
                self.play = False
            elif i.type == KEYDOWN:
                if i.key == K_RIGHT and self.direction != "LEFT":
                    self.direction != "RIGTH"
                elif i.key == K_LEFT and self.direction != "RIGHT":
                    self.direction = "LEFT"
                elif i.key == K_UP and self.direction != "DOWN":
                    self.direction = "UP"
                elif i.key == K_DOWN and self.direction != "UP":
                    self.direction = "DOWN"
                elif i.key ==K_ESCAPE:
                    self.play = False
                elif i.key == K_SPACE:
                    if self.pause == False:
                        self.pause = True
                    elif self.pause == True:
                        self.pause = False
