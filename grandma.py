import pygame as pg

class Grandma:
    def __init__(self, x, y):
        self.image = pg.image.load("images/grandmaa.png")
        self.rect = self.image.get_rect().inflate(-50, -50)
        self.rect.topleft = (x, y)

    def move(self):
        pass

    def draw(self, win, camera):
        win.blit(self.image, (self.rect.x - camera.rect.x, self.rect.y - camera.rect.y))
        
