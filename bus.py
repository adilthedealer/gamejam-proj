import pygame as pg
import time
import math

class Bus:
    def __init__(self, x, y, speed):
        self.image = pg.transform.scale(pg.image.load("images/Bus_green.png"), (150, 120))
        self.rect = self.image.get_rect().inflate(-50, -80)
        self.rect.topleft = (x, y)
        self.speed = speed
        self.stopped = False
        self.stop_coordinates = [(806, 398), (926, 476)]
        self.current_stop = 0
        self.last_stop_time = time.time()

    def move(self):
        if not self.stopped:
            distance_to_stop = math.sqrt(
                (self.rect.centerx - self.stop_coordinates[self.current_stop][0]) ** 2 +
                (self.rect.centery - self.stop_coordinates[self.current_stop][1]) ** 2
            )

            if distance_to_stop < 70 and self.speed < 0:
                self.stopped = True
                self.last_stop_time = time.time()

        elif time.time() - self.last_stop_time >= 30:
            self.stopped = False
            self.current_stop = (self.current_stop + 1) % len(self.stop_coordinates)

        if not self.stopped:
            self.rect.x += self.speed
            if self.rect.left > 1600 or self.rect.right < 0:
                self.speed = -self.speed
                self.image = pg.transform.flip(self.image, True, False)

    def draw(self, win, camera):
        win.blit(self.image, (self.rect.x - camera.rect.x, self.rect.y - camera.rect.y))