import pygame


class Snake():
    def __init__(self):
        self.head = [45, 45]
        self.body = [[45, 45], [34, 45], [23, 45]]

    def move_snake(self, control):
        if control.direction == "RIGTH":
            self.head[0] += 11
        elif control.direction == "LEFT":
            self.head[0] -= 11
        elif control.direction == "UP":
            self.head[1] -= 11
        elif control.direction == "DOWN":
            self.head[1] += 11

    def draw_snake(self, window):
        for part in self.body:
            pygame.draw.rect(window, pygame.Color('GREEN'),
                             pygame.Rect(part[0], part[1], 10, 10))

    def animation(self):
        self.body.insert(0, list(self.head))
        self.body.pop()

    def check_edge_window(self):
        if self.head[0] == 12:
            self.head[0] = 419
        elif self.head[0] == 419:
            self.head[0] = 23
        elif self.head[1] == 23:
            self.head[1] = 419
        elif self.head[1] == 419:
            self.head[1] = 34
