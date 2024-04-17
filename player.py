import pygame as pg

class Player:
    def __init__(self):
        self.run_images = [
            pg.image.load("images/running_student1.png").convert_alpha(),
            pg.image.load("images/running_student2.png").convert_alpha(),
        ]
        self.current_run_image = 0
        self.image = self.run_images[self.current_run_image]
        self.rect = self.image.get_rect().inflate(-50, -50)
        self.rect.center = (250, 250)

    def move(self, vector):
        self.rect.x += vector[0]
        self.rect.y += vector[1]

    def update(self):
        self.current_run_image = (self.current_run_image + 1) % len(self.run_images)
        self.image = self.run_images[self.current_run_image]

    def draw(self, win, camera):
        win.blit(self.image, (self.rect.x - camera.rect.x, self.rect.y - camera.rect.y))
