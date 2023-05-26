import sys
import pygame as pg
from random import choice


def ball_start(obj):
    global speed_x, speed_y

    obj.center = (W // 2, H // 2)  # помещаю объект посередине
    speed_x *= choice([-1, 1])
    speed_y *= choice([-1, 1])


def ball_move(ball):
    global speed_x, speed_y, player_score, opponent_score
    ball.x += speed_x
    ball.y += speed_y

    if ball.top <= 0 or ball.bottom >= H:  # если мяч ударился об верхнюю или нижнюю границу экрана
        speed_y *= -1  # развернуть его в обратную сторону
    elif ball.left <= 0:
        ball_start(ball)
        player_score += 1  # засчитываем очки игроку
    elif ball.right >= W:
        ball_start(ball)
        opponent_score += 1  # засчитываем очки оппоненту
    elif ball.colliderect(player) or ball.colliderect(opponent):
        speed_x *= -1
        
        
def player_motion(speed, pl):
    pl.y += speed 
    
    if pl.top <= 0:  # если мы ушли за верхнюю границу экрана
        pl.top = 0  # останавливаем платформу там 
    elif pl.bottom >= H:
        pl.bottom = H


def opponent_motion(speed, op, ball):
    if op.top < ball.y:
        op.y += speed
    elif op.bottom > ball.y:
        op.y -= speed

    if op.top <= 0:
        op.top = 0
    elif op.bottom >= H:
        op.bottom = H


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
o_speed = 5
ball_moving = False
speed_x = 7 * choice([-1, 1])
speed_y = 7 * choice([-1, 1])

# scores
player_score = 0
opponent_score = 0
pg.font.init()
my_font = pg.font.SysFont('comicsans', 64)

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

    player_score_text = my_font.render(f'{player_score}', True, GREEN)  # добавляем текст на экран
    screen.blit(player_score_text, [W // 2 + 50, H // 2.5])

    opponent_score_text = my_font.render(f'{opponent_score}', True, GREEN)  # добавляем текст на экран
    screen.blit(opponent_score_text, [W // 2 - 90, H // 2.5])

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
    opponent_motion(o_speed, opponent, ball)
