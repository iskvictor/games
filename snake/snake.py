import pygame

class Snake():
    def __init__(self):
        self.head = [45, 45]

    def move_snake(self, control):
        if control.direction == "RIGTH":
            self.head[0] += 25
        elif control.direction == "LEFT":
            self.head[0] -= 25
        elif control.direction == "UP":
            self.head[1] -= 25
        elif control.direction == "DOWN":
            self.head[1] += 25


    def draw_snake(self, window):
        pygame.draw.rect(window, pygame.Color('GREEN'), pygame.Rect(self.head[0], self.head[1], 10, 10))
