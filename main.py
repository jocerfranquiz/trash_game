import pygame as pg
import os

WIDTH, HEIGHT = 800, 600
FPS = 60
VELOCITY = 5
WIN = pg.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 50, 40
BORDER = pg.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)  # Rect(left, top, width, height)
BULLET_VELOCITY = 7
MAX_BULLETS = 5

YELLOW_HIT = pg.USEREVENT + 1
RED_HIT = pg.USEREVENT + 2

YELLOW_SPACESHIP_IMAGE = pg.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pg.transform.rotate(
    pg.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pg.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pg.transform.rotate(
    pg.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), -90)

SPACE = pg.transform.scale(pg.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

pg.display.set_caption('Trash Game')


def draw_window(red, yellow, yellow_bullets=None, red_bullets=None):
    WIN.blit(SPACE, (0, 0))
    pg.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in yellow_bullets:
        pg.draw.rect(WIN, YELLOW, bullet)
    for bullet in red_bullets:
        pg.draw.rect(WIN, RED, bullet)


def yellow_move(keys_pressed, yellow):
    if keys_pressed[pg.K_a] and yellow.x - VELOCITY > 0:
        yellow.x -= VELOCITY
    if keys_pressed[pg.K_d] and yellow.x + VELOCITY + yellow.width < BORDER.x:
        yellow.x += VELOCITY
    if keys_pressed[pg.K_w] and yellow.y - VELOCITY > 0:
        yellow.y -= VELOCITY
    if keys_pressed[pg.K_s] and yellow.y + VELOCITY + yellow.height < HEIGHT - 10:
        yellow.y += VELOCITY


def red_move(keys_pressed, red):
    if keys_pressed[pg.K_LEFT] and red.x - VELOCITY > BORDER.x:
        red.x -= VELOCITY
    if keys_pressed[pg.K_RIGHT] and red.x + VELOCITY + red.width < WIDTH:
        red.x += VELOCITY
    if keys_pressed[pg.K_UP] and red.y - VELOCITY > 0:
        red.y -= VELOCITY
    if keys_pressed[pg.K_DOWN] and red.y + VELOCITY + red.height < HEIGHT - 10:
        red.y += VELOCITY


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VELOCITY
        if red.colliderect(bullet):
            yellow_bullets.remove(bullet)
            pg.event.post(pg.event.Event(RED_HIT, {}))
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VELOCITY
        if yellow.colliderect(bullet):
            red_bullets.remove(bullet)
            pg.event.post(pg.event.Event(YELLOW_HIT, {}))
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def main():
    yellow = pg.Rect(WIDTH / 4, HEIGHT / 2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red = pg.Rect(WIDTH * 3 / 4, HEIGHT / 2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    yellow_bullets = []
    red_bullets = []

    clock = pg.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False
                if event.key == pg.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pg.Rect(yellow.x + yellow.width // 2, yellow.y + yellow.height // 2, 10, 5)
                    yellow_bullets.append(bullet)
                if event.key == pg.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pg.Rect(red.x + red.width // 2, red.y + red.height // 2, 10, 5)
                    red_bullets.append(bullet)

        keys_pressed = pg.key.get_pressed()
        yellow_move(keys_pressed, yellow)
        red_move(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(red, yellow, yellow_bullets, red_bullets)

    pg.quit()


if __name__ == '__main__':
    main()
