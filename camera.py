import pygame as pg

class Camera:
    def __init__(self, x, y):
        self.rect = pg.Rect(x, y, 500, 500)

    def move(self, vector):
        self.rect[0] += vector[0]
        self.rect[1] += vector[1]
