import sys
import pygame as pg

WIN_WIDTH = 1280
WIN_HEIGHT = 720

pg.init()  # инициализируем pygame
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # создаем экран игры разрешением 1280х720px

img = pg.image.load('angry-birds.png')  # загрузить картинку в игру
img.convert()  # перевести картинку в тот формат, в котором ее воспринимает PyGame
img_rect = img.get_rect()  # мы превращаем картинку в игровой объект, у которого есть осязаемые границы
img_rect.center = WIN_WIDTH // 2, WIN_HEIGHT // 2  # позиционирую картинку по центру экрана

moving = False
scale = 1
angle = 0
img1 = img
img_rect1 = img1.get_rect()
img_rect1.center = WIN_WIDTH // 2, WIN_HEIGHT // 2

while True:  # цикл игры
    for event in pg.event.get():  # обработчик событий pygame
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:  # если кнопка мыши нажата
            if img_rect.collidepoint(event.pos):  # если квадрат картинки совпадает с местом, где кликнули мышкой
                moving = True  # мы разрешаем картинке двигаться
        if event.type == pg.MOUSEBUTTONUP:
            moving = False
        if event.type == pg.MOUSEMOTION and moving:  # если мышку двигают и картинке можно перемещаться
            img_rect.move_ip(event.rel)  # двигаем картинку за мышкой
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                if event.mod and pg.KMOD_SHIFT:
                    angle -= 10
                else:
                    angle += 10
                img1 = pg.transform.rotozoom(img, angle, scale)
            if event.key == pg.K_s:
                if event.mod and pg.KMOD_SHIFT:
                    scale /= 1.1
                else:
                    scale *= 1.1
                img1 = pg.transform.rotozoom(img, angle, scale)
            rect1 = img1.get_rect()
            rect1.center = WIN_WIDTH // 2, WIN_HEIGHT // 2

    screen.fill((63, 63, 63))
    screen.blit(img1, img_rect1)
    pg.draw.rect(screen, (255, 0, 0), img_rect1, 1)
    pg.display.update()
