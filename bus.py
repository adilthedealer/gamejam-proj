import pygame as pg


class Bus:
    def __init__(self, x, y, speed):
        self.image = pg.transform.scale(pg.image.load("images/Bus_green.png"), (150, 120))
        self.rect = self.image.get_rect().inflate(-50, -80)
        self.rect.topleft = (x, y)
        self.speed = speed

    def move(self):
        self.rect.x += self.speed
        if self.rect.left > 1600 or self.rect.right < 0:
            self.speed = -self.speed
            self.image = pg.transform.flip(self.image, True, False)

    def draw(self, win, camera):
        win.blit(self.image, (self.rect.x - camera.rect.x, self.rect.y - camera.rect.y))
