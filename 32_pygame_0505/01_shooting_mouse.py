'''Напишите код в котором имитируется полет снаряда (пусть его роль сыграет круг)
в место клика мышью. Снаряд должен вылетать из нижнего края окна и лететь вверх,
т. е. изменяться должна только координата y. Пока летит один, другой не должен
появляться. Когда снаряд достигает цели, должен имитировать взрыв, например, в этом
месте прорисовываться квадрат.'''

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

# начальные параметры пули
bullet_r = 10
bullet_speed = 3
bullet_x = WIN_WIDTH // 2
bullet_y = WIN_HEIGHT

# флаг, запрещающий вылет пули, пока летит другая
bullet_flying = False

# параметры цели
target_x = WIN_WIDTH // 2
target_y = 100
target_width = 50
target_height = 50

screen.fill(WHITE)
pg.display.update()

while True:  # цикл игры
    for event in pg.event.get():  # обработчик событий pygame
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    pressed = pg.mouse.get_pressed()  # определяет, какая клавиша мыши была нажата
    pos = pg.mouse.get_pos()  # определяет позицию мыши в реальном времени

    if pressed[0] and not bullet_flying:
        bullet_x = pos[0]
        bullet_flying = True

    # движение снаряда
    if bullet_flying:
        bullet_y -= bullet_speed
        if bullet_y < 0:
            # если снаряд достиг нижней границы
            bullet_flying = False
            bullet_y = WIN_HEIGHT
        elif ((bullet_x - target_x) ** 2 + (bullet_y - target_y) ** 2) <= (bullet_r ** 2 + target_width ** 2) / 4: # если снаряд попал в цель
            target_rect = pg.Rect(target_x, target_y, target_width, target_height)  # мы создаем квадрат
            pg.draw.rect(screen, ORANGE, (target_x, target_y, target_width, target_height))  # нарисовать оранжевый квадратик на экране в координатах target_rect
            bullet_flying = False
            bullet_y = WIN_HEIGHT

    # отрисовываем происходящее на экране
    screen.fill(WHITE)
    if bullet_flying:
        pg.draw.circle(screen, BLUE, (bullet_x, bullet_y), bullet_r)
    pg.draw.rect(screen, PINK, (target_x, target_y, target_width, target_height), 2)

    pg.display.flip()







