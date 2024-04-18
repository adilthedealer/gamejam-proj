import pygame as pg
import time

class TrafficLight:
    def __init__(self, screen, green_interval=15, yellow_interval=3, red_interval=20):
        self.screen = screen
        self.green = pg.image.load("images/lights/green_light.png")
        self.red = pg.image.load("images/lights/red_light.png")
        self.yellow = pg.image.load("images/lights/yellow_light.png")

        self.lights = [self.green, self.yellow, self.red, self.yellow]
        self.current_light_index = 0

        self.green_interval = green_interval
        self.yellow_interval = yellow_interval
        self.red_interval = red_interval

        self.last_green_time = time.time()
        self.last_yellow_time = time.time()
        self.last_red_time = time.time()

    def update(self):
        current_time = time.time()

        if self.current_light_index == 0 and current_time - self.last_green_time >= self.green_interval:
            self.current_light_index = 1
            self.last_yellow_time = current_time
        elif self.current_light_index == 1 and current_time - self.last_yellow_time >= self.yellow_interval:
            self.current_light_index = 2
            self.last_red_time = current_time
        elif self.current_light_index == 2 and current_time - self.last_red_time >= self.red_interval:
            self.current_light_index = 3
            self.last_yellow_time = current_time
        elif self.current_light_index == 3 and current_time - self.last_yellow_time >= self.yellow_interval:
            self.current_light_index = 0
            self.last_green_time = current_time

    def draw(self, background, x, y):
        current_light = self.lights[self.current_light_index]
        light_width, light_height = current_light.get_size()
        background.blit(current_light, (x - light_width // 2, y - light_height // 2))  # Center the light