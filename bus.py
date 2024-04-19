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
        # Вычисляем расстояние до текущей остановки
        distance_to_stop = math.sqrt(
            (self.rect.centerx - self.stop_coordinates[self.current_stop][0]) ** 2 +
            (self.rect.centery - self.stop_coordinates[self.current_stop][1]) ** 2
        )

        # Если автобус движется слева направо и достиг координат остановки
        if not self.stopped and self.speed > 0 and distance_to_stop < 100:
            self.stopped = True # Останавливаем автобус
            self.last_stop_time = time.time()  # Запоминаем время остановки

        # Если прошло 30 секунд с момента последней остановки
        elif self.stopped and time.time() - self.last_stop_time >= 30:
            self.stopped = False  # Снова запускаем движение
            self.current_stop = (self.current_stop + 1) % len(self.stop_coordinates)  # Переходим к следующей остановке

        # Если автобус не остановлен, продолжаем движение
        if not self.stopped:
            self.rect.x += self.speed

            # Если автобус достиг правого края, перемещаем его в левый край
            if self.rect.left > 1600:
                self.rect.right = 0

    def draw(self, win, camera):
        win.blit(self.image, (self.rect.x - camera.rect.x, self.rect.y - camera.rect.y))
