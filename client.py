import pygame as pg
from network import Network

WIDTH = 800
HEIGHT = 800

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Belot Multiplayer by bahkobg')


class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.velocity = 1
        self.rect = pg.Rect(x, y, width, height)

    def draw(self, surface):
        pg.draw.rect(surface, self.color, self.rect)

    def move(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            self.rect.x -= self.velocity
        elif keys[pg.K_RIGHT]:
            self.rect.x += self.velocity
        elif keys[pg.K_DOWN]:
            self.rect.y += self.velocity
        elif keys[pg.K_UP]:
            self.rect.y -= self.velocity


def main():
    n = Network()
    start_pos = n.getPos()
    p1 = Player(50, 50, 100, 100, (0, 255, 0))
    running = True
    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
                pg.quit()
        screen.fill((255, 255, 255))
        p1.move()
        p1.draw(screen)

        pg.display.update()


if __name__ == '__main__':
    main()
