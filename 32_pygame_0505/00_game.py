import sys
import pygame as pg
import random

WIN_WIDTH = 1280
WIN_HEIGHT = 720
WHITE = (255, 255, 255)
ORANGE = (252, 186, 3)
GREEN = (22, 217, 15)
BLUE = (36, 127, 224)
PINK = (224, 36, 177)


pg.init()  # инициализируем pygame
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # создаем экран игры разрешением 1280х720px

screen.fill(WHITE)
pg.display.update()

while True:  # цикл игры
    for event in pg.event.get():  # обработчик событий pygame
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    pressed = pg.mouse.get_pressed()  # определяет, какая клавиша мыши была нажата
    pos = pg.mouse.get_pos()  # определяет позицию мыши в реальном времени
    if pressed[0]:  # левая кнопка мыши
        pg.draw.circle(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255) ), pos, 20)
    elif pressed[2]:  # правая кнопка мыши
        pg.draw.circle(screen, BLUE, pos, 20)
        pg.draw.rect(screen, GREEN, (pos[0] - 10, pos[1] - 10, 20, 20))
    elif pressed[1]:  # нажато колесо мыши
        screen.fill(WHITE)
    pg.display.update()




