import pygame as pg
import random

class NPCLeft:
    def __init__(self, x, y, speed, n):
        try:
            # Load NPC sprites for rightward movement
            self.run_images_right = [
                pg.transform.flip(pg.transform.scale(pg.image.load("images/npcside/npc" + n + "_side_stand.png").convert_alpha(), (35, 35)), True, False),
                pg.transform.flip(pg.transform.scale(pg.image.load("images/npcside/npc" + n + "_side1.png").convert_alpha(), (35, 35)), True, False),
                pg.transform.flip(pg.transform.scale(pg.image.load("images/npcside/npc" + n + "_side2.png").convert_alpha(), (35, 35)), True, False)
            ]
        except pg.error as e:
            print("Error loading images:", e)
            raise SystemExit

        self.current_run_images = self.run_images_right  # NPC always moves right
        self.current_run_index = 0
        self.image = self.current_run_images[self.current_run_index]

        self.rect = self.image.get_rect().inflate(-50, -50)
        self.rect.center = (x, y)  # Initial NPC position

        # self.allowed_rects = [
        #     pg.Rect(1599, 1799, 103, 48),
        #     pg.Rect(1698, 1531, 86, 469),
        #     pg.Rect(863, 1452, 922, 79),
        #     pg.Rect(863, 888, 76, 568),
        #     pg.Rect(142, 886, 796, 80),
        #     pg.Rect(141, 419, 72, 467),
        #     pg.Rect(212, 419, 960, 67)
        # ]

        self.speed = speed  # Movement speed

    def move(self):
        new_rect = self.rect.copy() 
        new_rect.x -= self.speed  
        self.rect = new_rect
        # if any(new_rect.colliderect(rect) for rect in self.allowed_rects):
        #     self.rect = new_rect

    def update(self):
        self.current_run_index = (self.current_run_index + 1) % len(self.current_run_images)
        self.image = self.current_run_images[self.current_run_index]

    def draw(self, win, camera):
        win.blit(self.image, (self.rect.x - camera.rect.x, self.rect.y - camera.rect.y))
