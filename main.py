import pygame as pg
import os

WIDTH, HEIGHT = 800, 600
FPS = 60
WIN = pg.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_SPACESHIP_IMAGE = pg.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pg.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

RED_SPACESHIP_IMAGE = pg.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pg.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

pg.display.set_caption('Trash Game')


def draw_window():
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP,
             (WIDTH / 4 - YELLOW_SPACESHIP.get_width() / 4,
              HEIGHT / 4 - YELLOW_SPACESHIP.get_height() / 4)
             )
    WIN.blit(RED_SPACESHIP,
             (WIDTH * 3 / 4 - RED_SPACESHIP.get_width() * 3 / 4 ,
              HEIGHT * 3 / 4 - RED_SPACESHIP.get_height() * 3 / 4)
             )
    # pg.display.update()


def main():
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

        draw_window()

    pg.quit()


if __name__ == '__main__':
    main()
