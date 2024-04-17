import pygame as pg


class Bus:
    def __init__(self, x, y, speed):
        self.image = pg.image.load("images/bus.png").convert_alpha()
        self.rect = self.image.get_rect().inflate(-50, -50)
        self.rect.topleft = (x, y)
        self.speed = speed

    def move(self):
        self.rect.x += self.speed
        if self.rect.left > 1600 or self.rect.right < 0:
            self.speed = -self.speed

    def draw(self, win, camera):
        win.blit(self.image, (self.rect.x - camera.rect.x, self.rect.y - camera.rect.y))
