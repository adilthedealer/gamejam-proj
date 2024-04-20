import pygame as pg

class Luzha:
    def __init__(self, x, y):
        self.image = pg.image.load("images/circlewater.png")
        self.rect = self.image.get_rect().inflate(-40, -20)
        self.rect.topleft = (x, y)

    def move(self):
        pass

    def draw(self, win, camera):
        win.blit(self.image, (self.rect.x - camera.rect.x, self.rect.y - camera.rect.y))
        
