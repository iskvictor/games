import pygame
from control import Control
from snake import Snake
from gui import Gui

pygame.init()
window = pygame.display.set_mode((441, 441))
pygame.display.set_caption('Змейка')
control = Control()
snake = Snake()
gui = Gui()
clock = pygame.time.Clock()
var_speed = 0
gui.create_file()
while control.play:
    control.control()
    window.fill(pygame.Color('BLACK'))
    snake.draw_snake(window)
    gui.draw_level(window)
    print(var_speed)
    if var_speed % 10 == 0 and control.pause:
        snake.move_snake(control)
        snake.check_edge_window()
        snake.animation()
    var_speed += 1
    pygame.display.flip()
    clock.tick(40)
