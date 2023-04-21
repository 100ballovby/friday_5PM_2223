import sys
import pygame as pg

pg.init()  # инициализируем pygame
pg.display.set_mode((1280, 720))  # создаем экран игры разрешением 1280х720px

while True:  # цикл игры
    for event in pg.event.get():  # обработчик событий pygame
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()




