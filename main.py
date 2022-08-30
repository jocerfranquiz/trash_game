import pygame as pg

WIDTH, HEIGHT = 800, 600
FPS = 60
WIN = pg.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)

pg.display.set_caption("Trash Game")


def main():
    run = True
    while run:
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False

        WIN.fill(WHITE)

    pg.quit()


if __name__ == '__main__':
    main()
