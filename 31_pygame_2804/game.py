import sys
import pygame as pg
import random

from pygame import display

pg.init()  # инициализируем pygame
win_width = 400
win_height = 400
screen = pg.display.set_mode((win_width, win_height))  # создаем экран игры разрешением 1280х720px
pg.display.set_caption('My first PyGame Game')

black = (0, 0, 0)
white = (255, 255, 255)

# размеры и координаты игрока
player_size = win_width * 0.2
player_x = win_width // 2
player_y = win_height - player_size

# скорость перемещения игрока
player_speed = 5

# препятствия
obstacle_size = win_width * 0.05
obstacle_x = random.randint(0, int(win_width - obstacle_size))
obstacle_y = 0
obstacle_speed = 5

# очки
score = 0

# шрифт
pg.font.init()  # чтобы работало отображение текста в игре
font = pg.font.SysFont('Arial', 25)  # устанавливаем настройки текста (щрифт Arial, размер 25)


def draw_player():
    pg.draw.rect(screen, white, [player_x, player_y, player_size, player_size])


def draw_obstacle():
    pg.draw.rect(screen, white, [obstacle_x, obstacle_y, obstacle_size, obstacle_size])


def move_player():
    global player_x  # глобальная переменная (значение этой переменной можно поменять из любого места в программе)
    keys = pg.key.get_pressed()  # возвращает массив нажатых и не нажатых кнопок
    if keys[pg.K_LEFT]:  # если на месте кнопки влево True
        player_x -= player_speed
    elif keys[pg.K_RIGHT]:  # если на месте кнопки вправо True
        player_x += player_speed


def move_obstacle():
    global obstacle_x, obstacle_y, score
    obstacle_y += obstacle_speed
    if obstacle_y > win_height:  # если координата у препятствия будет больше высоты экрана
        obstacle_y = 0
        obstacle_x = random.randint(0, int(win_width - obstacle_size))
        score += 1


def display_score(score):
    score_text = font.render('Score: ' + str(score), True, white)
    screen.blit(score_text, [0, 0])


def collision_detection(p_x, p_y, o_x, o_y, p_size, o_size):
    if (p_x >= o_x and p_x < o_x + o_size) or (o_x >= p_x and o_x < p_x + p_size):
        if (p_y >= o_y and p_y < o_y + o_size) or (o_y >= p_y and o_y < p_y + p_size):
            return True
    return False


game_over = False
clock = pg.time.Clock()
while not game_over:  # цикл игры
    for event in pg.event.get():  # обработчик событий pygame
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fill(black)  # зальем экран черным
    draw_player()  # отображаем игрока
    draw_obstacle()  # отображаем препятствие
    move_player()  # двигаем игрока
    move_obstacle()  # двигаем препятствие
    display_score(score)  # отобразить количество очков на экране

    if collision_detection(player_x, player_y, obstacle_x, obstacle_y, player_size, obstacle_size):
        game_over = True
        print(f'Your score is {score}')

    pg.display.update()
    clock.tick(60)
