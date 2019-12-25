import pygame
from control import Control
from snake import Snake
from gui import Gui
from food import Food

pygame.init()
window = pygame.display.set_mode((441, 441))
pygame.display.set_caption('Змейка')
control = Control()
snake = Snake()
gui = Gui()
clock = pygame.time.Clock()
var_speed = 0
gui.create_file()
gui.fill_field()
food = Food()
food.get_food_position(gui)
while control.play:
    gui.check_win_lose()
    control.control()
    window.fill(pygame.Color('BLACK'))
    if gui.game == "GAME":
        snake.draw_snake(window)
        food.draw_food(window)
    elif gui.game == "LOSE":
        gui.draw_lose(window)
    elif gui.game == "WIN":
        gui.draw_win(window)
    gui.draw_indicator(window)
    gui.draw_level(window)
    print(var_speed)
    if var_speed % 10 == 0 and control.pause and gui.game == "GAME":
        snake.move_snake(control)
        snake.cheak_barrier(gui)
        snake.check_edge_window()
        snake.eat(food, gui)
        snake.animation()
    var_speed += 1
    pygame.display.flip()
    clock.tick(40)
