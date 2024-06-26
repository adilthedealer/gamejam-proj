import pygame as pg
import time
import math

class Bus:
    def __init__(self, x, y, speed):
        self.image = pg.transform.scale(pg.image.load("images/Bus_green.png"), (150, 120))
        self.rect = self.image.get_rect().inflate(-150, -150)
        self.rect.topleft = (x, y)
        self.speed = speed
        self.stopped = True
        self.ticks = 0

    def distance_to_stop(self, player):
        return math.sqrt(
            (self.rect.centerx - player.rect.x) ** 2 +
            (self.rect.centery - player.rect.y) ** 2
        )

    def move(self, player):
    # Вычисляем расстояние до текущей остановки
        dist = self.distance_to_stop(player)

        if self.stopped and self.speed > 0 and dist < 100:
            self.stopped = False
            self.ticks = pg.time.get_ticks()
        elif self.stopped and self.speed < 0 and dist < 100:
            raise SystemExit

        if not self.stopped:
            self.rect.x -= self.speed
            if self.rect.left > 1600:
                self.rect.right = 200
    
    def draw(self, win, camera):
        win.blit(self.image, (self.rect.x - camera.rect.x, self.rect.y - camera.rect.y))
