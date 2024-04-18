import pygame as pg
import time
import math


class Bus:
    def __init__(self, x, y, speed):
        self.image = pg.transform.scale(pg.image.load("images/Bus_green.png"), (150, 120))
        self.rect = self.image.get_rect().inflate(-50, -80)
        self.rect.topleft = (x, y)
        self.speed = speed
        self.stopped = False  # Флаг, указывающий, остановлен ли автобус
        self.stop_coordinates = [(806, 398), (926, 476)]  # Координаты остановок
        self.current_stop = 0  # Индекс текущей остановки
        self.last_stop_time = time.time()  # Последнее время остановки

    def move(self):
        distance_to_stop = math.sqrt(
            (self.rect.centerx - self.stop_coordinates[self.current_stop][0]) ** 2 +
            (self.rect.centery - self.stop_coordinates[self.current_stop][1]) ** 2
        )

        if distance_to_stop < 10:  # Если расстояние до остановки меньше 10 пикселей
            self.stopped = True  # Останавливаем автобус
            if time.time() - self.last_stop_time >= 30:  # Если прошло 30 секунд с последней остановки
                self.current_stop = (self.current_stop + 1) % len(self.stop_coordinates)  # Переходим к следующей остановке
                self.last_stop_time = time.time()  # Запоминаем время текущей остановки
                self.stopped = False  # Начинаем движение

        if not self.stopped:  # Если не остановлены
            self.rect.x += self.speed
            if self.rect.left > 1600 or self.rect.right < 0:
                self.speed = -self.speed
                self.image = pg.transform.flip(self.image, True, False)

    def draw(self, win, camera):
        win.blit(self.image, (self.rect.x - camera.rect.x, self.rect.y - camera.rect.y))