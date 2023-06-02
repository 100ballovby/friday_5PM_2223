import sys
import pygame as pg
import random as r

W = 1280
H = 720

pg.init()  # инициализируем pygame
screen = pg.display.set_mode((W, H))  # создаем экран игры разрешением 1280х720px

# colors
BLACK = (0, 0, 0)
GREEN = (74, 255, 38)
RED = (255, 38, 38)


def snake(s_block, s_list):
    for x in s_list:
        pg.draw.rect(screen, GREEN, [x[0], x[1], s_block, s_block])

# snake
snake_block = 20
snake_speed = 5
snake_body = []
snake_length = 1

# food
food_x = 200
food_y = 200

# game variables
x_change = 0
y_change = 0
s_x = 200
s_y = 200

while True:  # цикл игры
    for event in pg.event.get():  # обработчик событий pygame
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    food = pg.Rect(food_x, food_y, 20, 20)

    # screen
    screen.fill(BLACK)
    snake(snake_block, snake_body)
    pg.draw.rect(screen, RED, food)

    pg.display.update()



