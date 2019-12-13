import pygame
from pygame.locals import *

class Control():
    def __init__(self):
        self.play = True
        self.direction = "RIGTH"


    def control(self):
        for i in pygame.event.get():
            if i.type == QUIT:
                self.play = False
            elif i.type == KEYDOWN:
                if i.key == K_RIGHT:
                    self.direction = "RIGTH"
                elif i.key == K_LEFT:
                    self.direction = "LEFT"
                elif i.key == K_UP:
                    self.direction = "UP"
                elif i.key == K_DOWN:
                    self.direction = "DOWN"
