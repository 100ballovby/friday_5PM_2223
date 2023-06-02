import sys
import pygame as pg
from random import choice


def ball_start(obj):
    global speed_x, speed_y, ball_moving, score_time

    obj.center = (W // 2, H // 2)  # помещаю объект посередине
    cur_time = pg.time.get_ticks()  # фиксирует текущее время в игре

    if cur_time - score_time < 700:
        num_3 = my_font.render('3', True, GREEN)
        screen.blit(num_3, [W // 2, H // 2])
    elif 700 < cur_time - score_time < 1400:
        num_2 = my_font.render('2', True, GREEN)
        screen.blit(num_2, [W // 2, H // 2])
    elif 1400 < cur_time - score_time < 2100:
        num_1 = my_font.render('1', True, GREEN)
        screen.blit(num_1, [W // 2, H // 2])

    if cur_time - score_time < 2100:  # пока не прошло 3 секунды
        speed_x, speed_y = 0, 0  # мяч стоит на месте
    else:
        speed_x = 7 * choice([-1, 1])
        speed_y = 7 * choice([-1, 1])
        score_time = None  # отключаем подсчет времени


def ball_move(ball):
    global speed_x, speed_y, player_score, opponent_score, score_time
    ball.x += speed_x
    ball.y += speed_y

    if ball.top <= 0 or ball.bottom >= H:  # если мяч ударился об верхнюю или нижнюю границу экрана
        speed_y *= -1  # развернуть его в обратную сторону
        pg.mixer.Sound.play(pong_sound)
    elif ball.left <= 0:
        pg.mixer.Sound.play(score_sound)
        score_time = pg.time.get_ticks()
        player_score += 1  # засчитываем очки игроку
    elif ball.right >= W:
        pg.mixer.Sound.play(score_sound)
        score_time = pg.time.get_ticks()
        opponent_score += 1  # засчитываем очки оппоненту

    if ball.colliderect(player):
        pg.mixer.Sound.play(pong_sound)
        if abs(ball.right - player.left) < 10:
            speed_x *= -1
        elif abs(ball.bottom - player.top) < 10 or abs(ball.top - player.bottom) < 10:
            speed_x *= -1
    elif ball.colliderect(opponent):
        pg.mixer.Sound.play(pong_sound)
        if abs(ball.left - opponent.right) < 10:
            speed_x *= -1
        elif abs(ball.bottom - opponent.top) < 10 or abs(ball.top - opponent.bottom) < 10:
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
ball_img = pg.image.load('tennis.png').convert_alpha()
ball_img = pg.transform.scale(ball_img, (50, 50))

player_img = pg.image.load('paddle.jpg').convert()
opponent_img = pg.image.load('paddle.jpg').convert()

player = player_img.get_rect()
opponent = opponent_img.get_rect()
ball = ball_img.get_rect()
player.x, player.y = W - 30, H // 2

# переменные для игры
p_speed = 0
o_speed = 5
ball_moving = False
score_time = True
speed_x = 7 * choice([-1, 1])
speed_y = 7 * choice([-1, 1])
pg.mixer.init()
pong_sound = pg.mixer.Sound('hit.mp3')
score_sound = pg.mixer.Sound('lose.wav')
pong_sound.set_volume(0.2)
score_sound.set_volume(0.1)

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
    screen.blit(ball_img, ball)
    screen.blit(player_img, player)
    screen.blit(opponent_img, opponent)

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

    if score_time:  # если время начинает считаться
        ball_start(ball)  # делаем "рестарт"
    pg.display.update()

    # логика игры
    ball_move(ball)
    player_motion(p_speed, player)
    opponent_motion(o_speed, opponent, ball)
