import pygame as pg

WIDTH, HEIGHT = 800, 600
FPS = 60
WIN = pg.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)

pg.display.set_caption("Trash Game")


def draw_window():
    WIN.fill(WHITE)
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
