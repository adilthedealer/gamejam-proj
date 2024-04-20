import pygame as pg
import random as rnd

class Raindrop:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = rnd.randint(5, 15)

    def fall(self):
        self.y += self.speed
        if self.y > 500:  # Adjust this value according to your window size
            self.y = rnd.randint(-100, -10)
            self.x = rnd.randint(0, 500)  # Adjust this value according to your window size

    def draw(self, surface):
        pg.draw.line(surface, (255, 255, 255), (self.x, self.y), (self.x, self.y + 5), 2)
