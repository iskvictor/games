import random
import pygame


class Food():
    def __init__(self):
        self.food_position = []

    def get_food_position(self, gui):
        self.food_position = random.choice(gui.field)
        print('++++', self.food_position)

    def draw_food(self, window):
        pygame.draw.rect(window, pygame.Color("RED"),
                         pygame.Rect(self.food_position[0],
                         self.food_position[1], 10, 10))
