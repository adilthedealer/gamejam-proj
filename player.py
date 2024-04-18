import pygame as pg

class Player:
    def __init__(self):
        img1 = pg.image.load("images/mc_run.png").convert_alpha()
        fix1 = pg.transform.scale(img1, (35, 35))
        img2 = pg.image.load("images/mc_run2.png").convert_alpha()
        fix2 = pg.transform.scale(img2, (35, 35))
        img = pg.image.load("images/mc_stand.png").convert_alpha()
        fix = pg.transform.scale(img, (35, 35))
        self.run_images = [
            # pg.image.load("images/running_student1.png").convert_alpha(),
            # pg.image.load("images/running_student2.png").convert_alpha(),
            fix1,
            fix,
            fix2
        ]
        self.current_run_image = 0
        self.image = self.run_images[self.current_run_image]
        self.rect = self.image.get_rect().inflate(-50, -50)
        self.rect.center = (1600, 1800)



    def move(self, vector):
        # if vector[1] > 0:
        #     self.run_images = [
        #         pg.image.load("images/mcback/mc_runback_1.png").convert_alpha(),
        #         pg.image.load("images/mcback/mc_runback_2.png").convert_alpha()
        #     ]
        #     self.current_run_image = 0
        #     self.image = self.run_images[self.current_run_image]
        # else:
        # self.run_images = [
        #     pg.image.load("images/running_student1.png").convert_alpha(),
        #     pg.image.load("images/running_student2.png").convert_alpha()
        # ]
        # self.current_run_image = 0
        # self.image = self.run_images[self.current_run_image]
        self.rect.x += vector[0]
        self.rect.y += vector[1]

    def update(self):
        self.current_run_image = (self.current_run_image + 1) % len(self.run_images)
        self.image = self.run_images[self.current_run_image]

    def draw(self, win, camera):
        win.blit(self.image, (self.rect.x - camera.rect.x, self.rect.y - camera.rect.y))