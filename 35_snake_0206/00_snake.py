import sys
import pygame as pg
import random as r
import time


def draw_snake(s_block, s_list):
    for x in s_list:
        pg.draw.rect(screen, GREEN, [x[0], x[1], s_block, s_block])


def show_message(msg, color, surface):
    text = font_style.render(msg, True, color)
    surface.blit(text, [20, H // 2])

W = 300
H = 300

BLUE = (120, 84, 240)
RED = (255, 0, 0)
GREEN = (74, 225, 74)
VIOLET = (248, 240, 255)
ORANGE = (252, 186, 3)
SNAKE_BLOCK = 10

pg.font.init()
font_style = pg.font.SysFont(bold=True, size=15, name='comicsans')
score_font = pg.font.SysFont('comicsans', 20)

pg.init()  # инициализируем pygame
screen = pg.display.set_mode((W, H))  # создаем экран игры разрешением 1280х720px
clock = pg.time.Clock()


def game_loop():
    x_change = 0
    y_change = 0
    x1 = 200
    y1 = 200

    food_x = round(r.randrange(0, W - SNAKE_BLOCK) / 10) * 10
    food_y = round(r.randrange(0, H - SNAKE_BLOCK) / 10) * 10

    done = False
    game_over = False

    snake_list = []
    snake_length = 1

    while not done:  # цикл игры

        while game_over:  # когда случился проигрыш (стена или съели сами себя), игра встает на паузу
            screen.fill(VIOLET)
            show_message('Game over. Press C to continue', BLUE, screen)
            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        game_over = False  # отключаем паузу
                        done = True  # закрыть игру
                    elif event.key == pg.K_c:
                        game_loop()  # перезапускаем игру

        clock.tick(5)
        for event in pg.event.get():  # обработчик событий pygame
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x_change = -SNAKE_BLOCK
                    y_change = 0
                elif event.key == pg.K_RIGHT:
                    x_change = SNAKE_BLOCK
                    y_change = 0
                elif event.key == pg.K_UP:
                    x_change = 0
                    y_change = -SNAKE_BLOCK
                elif event.key == pg.K_DOWN:
                    x_change = 0
                    y_change = SNAKE_BLOCK

        x1 += x_change
        y1 += y_change

        screen.fill(BLUE)
        #pg.draw.rect(screen, GREEN, [x1, y1, SNAKE_BLOCK, SNAKE_BLOCK])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            snake_list.pop(0)

        for block in snake_list[:-1]:
            if block == snake_head:  # когда змея двигается вправо, ход влево закончит игру
                game_over = True
        draw_snake(SNAKE_BLOCK, snake_list)
        pg.draw.rect(screen, RED, [food_x, food_y, SNAKE_BLOCK, SNAKE_BLOCK])  # рисуем еду
        pg.display.update()

        if x1 == food_x and y1 == food_y:  # если координаты змеи совпадают с координатами еды
            food_x = round(r.randrange(0, W - SNAKE_BLOCK) / 10) * 10
            food_y = round(r.randrange(0, H - SNAKE_BLOCK) / 10) * 10
            snake_length += 1


game_loop()
