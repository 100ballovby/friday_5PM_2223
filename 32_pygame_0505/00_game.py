import sys
import pygame as pg

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
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:  # левая кнопка мыши
                pg.draw.circle(screen, ORANGE, event.pos, 20)
            elif event.button == 3:  # правая кнопка мыши
                pg.draw.rect(screen, BLUE, event.pos, 20)





