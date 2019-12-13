import pygame
from control import Control
from snake import Snake
pygame.init()
window = pygame.display.set_mode((441,441))
pygame.display.set_caption('Змейка')
control = Control()
snake = Snake()
clock = pygame.time.Clock()
var_speed = 0
while control.play:
    control.control()
    window.fill(pygame.Color('BLACK'))
    snake.draw_snake(window)
    print(var_speed)
    if var_speed % 10 == 0:
        snake.move_snake(control)
    var_speed += 1
    pygame.display.flip()
    clock.tick(40)
