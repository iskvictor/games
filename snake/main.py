import pygame
from control import Control

pygame.init()
window = pygame.display.set_mode((441,441))
pygame.display.set_caption('Змейка')
control = Control()
#Координаты головы змеи
head = [45,45]
clock = pygame.time.Clock()
FPS = 2
while control.play:
    control.control()
    window.fill(pygame.Color('BLACK'))
    pygame.draw.rect(window, pygame.Color('GREEN'), pygame.Rect(head[0], head[1], 10, 10))
    head[0] += 25
    pygame.display.flip()
    clock.tick(FPS)
