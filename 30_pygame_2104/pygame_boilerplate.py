import sys
import pygame as pg

WIN_WIDTH = 1280
WIN_HEIGHT = 720

pg.init()  # инициализируем pygame
pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # создаем экран игры разрешением 1280х720px

while True:  # цикл игры
    for event in pg.event.get():  # обработчик событий pygame
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()




