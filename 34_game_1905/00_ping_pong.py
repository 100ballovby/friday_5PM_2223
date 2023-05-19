import sys
import pygame as pg


def ball_move(ball):
    global speed_x, speed_y
    ball.x += speed_x
    ball.y += speed_y

    if ball.top <= 0 or ball.bottom >= WIN_HEIGHT:  # если мяч ударился об верхнюю или нижнюю границу экрана
        speed_y *= -1  # развернуть его в обратную сторону
    elif ball.left <= 0 or ball.right >= WIN_WIDTH:
        speed_x *= -1
    elif ball.colliderect(player) or ball.colliderect(opponent):
        speed_x *= -1


WIN_WIDTH = 1280
WIN_HEIGHT = 720

GRAY = (230, 230, 230)
WHITE = (255, 255, 255)
GREEN = (83, 247, 74)

pg.init()  # инициализируем pygame
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # создаем экран игры разрешением 1280х720px
clock = pg.time.Clock()
FPS = 60

# игровые сущности
player = pg.Rect(WIN_WIDTH - 20, WIN_HEIGHT // 2, 10, 150)
opponent = pg.Rect(10,  WIN_HEIGHT // 2, 10, 150)
ball = pg.Rect(WIN_WIDTH // 2 - 15, WIN_HEIGHT // 2 - 15, 30, 30)

# переменные для игры
p_speed = 0
o_speed = 0
ball_moving = False
speed_x = 7
speed_y = 7

finished = False
while not finished:  # цикл игры
    clock.tick(FPS)
    for event in pg.event.get():  # обработчик событий pygame
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    # отображение игровых объектов
    screen.fill(GRAY)
    pg.draw.aaline(screen, WHITE, [WIN_WIDTH // 2, 0], [WIN_WIDTH // 2, WIN_HEIGHT])
    pg.draw.rect(screen, GREEN, player)
    pg.draw.rect(screen, GREEN, opponent)
    pg.draw.ellipse(screen, GREEN, ball)
    pg.display.update()

    # логика игры
    ball_move(ball)