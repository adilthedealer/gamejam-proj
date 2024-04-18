import pygame as pg

class Player:
    def __init__(self, initial_pos=(1600, 1800)):
        try:
            # Forward movement (movement to the top)
            self.fix1 = pg.transform.scale(pg.image.load("images/mc_run.png").convert_alpha(), (35, 35))
            self.fix2 = pg.transform.scale(pg.image.load("images/mc_run2.png").convert_alpha(), (35, 35))
            self.fix = pg.transform.scale(pg.image.load("images/mc_stand.png").convert_alpha(), (35, 35))

            # Backward movement
            self.fixb1 = pg.transform.scale(pg.image.load("images/mcback/mc_runback_1.png").convert_alpha(), (35, 35))
            self.fixb2 = pg.transform.scale(pg.image.load("images/mcback/mc_runback_2.png").convert_alpha(), (35, 35))
            self.fixb = pg.transform.scale(pg.image.load("images/mcback/mc_look_back.png").convert_alpha(), (35, 35))

            # Right movement
            self.fixr1 = pg.transform.scale(pg.image.load("images/mcside/mc_runside1.png").convert_alpha(), (35, 35))
            self.fixr2 = pg.transform.scale(pg.image.load("images/mcside/mc_runside2.png").convert_alpha(), (35, 35))
            self.fixr = pg.transform.scale(pg.image.load("images/mcside/mc_standside.png").convert_alpha(), (35, 35))
        except pg.error as e:
            print("Error loading images:", e)
            raise SystemExit

        self.run_images = [self.fix1, self.fix, self.fix2]
        self.run_images_back = [self.fixb1, self.fixb, self.fixb2]
        self.run_images_right = [self.fixr1, self.fixr, self.fixr2]
        self.current_run_image = 0
        self.image = self.run_images[self.current_run_image]

        self.rect = self.image.get_rect().inflate(-50, -50)
        self.rect.center = initial_pos

    def move(self, vector):
        if vector[0] > 0:
            self.run_images = self.run_images_right
        elif vector[1] < 0:  # Check if moving upwards
            self.run_images = [self.fix1, self.fix, self.fix2]  # Use images for movement to the top
        else:
            self.run_images = self.run_images

        self.rect.x += vector[0]
        self.rect.y += vector[1]

    def update(self):
        self.current_run_image = (self.current_run_image + 1) % len(self.run_images)
        self.image = self.run_images[self.current_run_image]

    def draw(self, win, camera):
        win.blit(self.image, (self.rect.x - camera.rect.x, self.rect.y - camera.rect.y))
