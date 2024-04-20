import pygame as pg

class MCGrandma:
    def __init__(self, x, y, speed):
        self.images = [
            pg.transform.scale(pg.image.load("images/mc_grandma/mc_babka_front1.png").convert_alpha(), (35, 35)),
            pg.transform.scale(pg.image.load("images/mc_grandma/mc_babka_front_stand.png").convert_alpha(), (35, 35)),
            pg.transform.scale(pg.image.load("images/mc_grandma/mc_babka_front2.png").convert_alpha(), (35, 35))
        ]
        self.current_run_index = 0
        self.image = self.images[self.current_run_index]
        self.rect = self.image.get_rect().inflate(-50, -50)
        self.rect.center = (x, y)
        self.allowed_rects = [pg.Rect(141, 419, 72, 467)]
        self.speed = speed

    def move(self, vector):
        self.rect.x += vector[0]
        self.rect.y += vector[1]

    def update(self):
        self.current_run_index = (self.current_run_index + 1) % len(self.images)
        self.image = self.images[self.current_run_index]

    def draw(self, win, camera):
        win.blit(self.image, (self.rect.x - camera.rect.x, self.rect.y - camera.rect.y))

    

