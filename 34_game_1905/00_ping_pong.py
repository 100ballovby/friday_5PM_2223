import sys
import pygame as pg


def ball_move(ball):
    global speed_x, speed_y
    ball.x += speed_x
    ball.y += speed_y

    if ball.top <= 0 or ball.bottom >= H:  # если мяч ударился об верхнюю или нижнюю границу экрана
        speed_y *= -1  # развернуть его в обратную сторону
    elif ball.left <= 0 or ball.right >= W:
        speed_x *= -1
    elif ball.colliderect(player) or ball.colliderect(opponent):
        speed_x *= -1
        
        
def player_motion(speed, pl):
    pl.y += speed 
    
    if pl.top <= 0:  # если мы ушли за верхнюю границу экрана
        pl.top = 0  # останавливаем платформу там 
    elif pl.bottom >= H:
        pl.bottom = H


W = 1280
H = 720

GRAY = (230, 230, 230)
WHITE = (255, 255, 255)
GREEN = (83, 247, 74)

pg.init()  # инициализируем pygame
screen = pg.display.set_mode((W, H))  # создаем экран игры разрешением 1280х720px
clock = pg.time.Clock()
FPS = 60

# игровые сущности
player = pg.Rect(W - 20, H // 2, 10, 150)
opponent = pg.Rect(10,  H // 2, 10, 150)
ball = pg.Rect(W // 2 - 15, H // 2 - 15, 30, 30)

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
    pg.draw.aaline(screen, WHITE, [W // 2, 0], [W // 2, H])
    pg.draw.rect(screen, GREEN, player)
    pg.draw.rect(screen, GREEN, opponent)
    pg.draw.ellipse(screen, GREEN, ball)

    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
        p_speed -= 5
    elif keys[pg.K_DOWN]:
        p_speed += 5
    else:
        p_speed = 0

    pg.display.update()

    # логика игры
    ball_move(ball)
    player_motion(p_speed, player)
