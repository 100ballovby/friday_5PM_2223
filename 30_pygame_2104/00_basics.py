import sys
import pygame as pg

pg.init()  # инициализируем pygame
screen = pg.display.set_mode((1280, 720))  # создаем экран игры разрешением 1280х720px
clock = pg.time.Clock()
FPS = 120

RED = (240, 54, 41)
BLUE = (105, 220, 224)
r = 30
x = 50
y = 720 // 2  # центр окна по вертикали

LEFT = 'left'
RIGHT = 'right'
STOP = 'stop'
motion = STOP

while True:  # цикл игры

    screen.fill((255, 255, 255))  # залить фон игры белым цветом
    for event in pg.event.get():  # обработчик событий pygame
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:  # если нажата какая-то кнопка
            if event.key == pg.K_d:  # pg.K_RIGHT
                motion = RIGHT
            elif event.key == pg.K_a:  # pg.K_RIGHT
                motion = LEFT
        elif event.type == pg.KEYUP:  # если кнопку отпустили
            if event.key in [pg.K_a, pg.K_d]:  # если кнопка в списке
                motion = STOP

    pg.draw.rect(screen, RED, (0, 0, 200, 130))
    # pg.draw.rect(screen, BLUE, (270, 180, 280, 75), 10)  (экран, цвет, (х, у, ширина, высота), толщина рамок)
    pg.draw.circle(screen, BLUE, (x, y), r)  # нарисовал кружочек в координатах х и у с радиусом r
    pg.display.update()  # чтобы на экране обновлялось изображение

    if motion == LEFT:
        x -= 5
    elif motion == RIGHT:
        x += 5

    clock.tick(FPS)  # включает смену кадров

