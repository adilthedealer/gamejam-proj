import pygame as pg

class Player1:
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
        self.run_images_left = [pg.transform.flip(self.fixr1, True, False), pg.transform.flip(self.fixr, True, False), pg.transform.flip(self.fixr2, True, False)]
        self.current_run_image = 0
        self.image = self.run_images[self.current_run_image]

        self.rect = self.image.get_rect().inflate(-50, -50)
        self.rect.center = initial_pos

        # координаты тротуара ниже ...
        self.allowed_rects = [
            pg.Rect(0, 1005, 2000, 155),
            pg.Rect(0, 252, 2000, 155),
            pg.Rect(493, 0, 155, 1575),
            pg.Rect(1306, 0, 155, 1575)
        ]
    
    def move(self, vector):
    # Calculate the new position
        new_rect = self.rect.move(vector)

        # Check if the new position is within any allowed rectangle
        for rect in self.allowed_rects:
            if new_rect.colliderect(rect):
                if vector[0] > 0:
                    self.run_images = self.run_images_right
                elif vector[0] < 0:
                    self.run_images = self.run_images_left
                elif vector[1] < 0:  # Check if moving upwards
                    self.run_images = [self.fix1, self.fix, self.fix2]
                elif vector[1] > 0:
                    self.run_images = self.run_images_back

                self.rect.x += vector[0]
                self.rect.y += vector[1]
                break



    def update(self):
        self.current_run_image = (self.current_run_image + 1) % len(self.run_images)
        self.image = self.run_images[self.current_run_image]

    def draw(self, win, camera):
        win.blit(self.image, (self.rect.x - camera.rect.x, self.rect.y - camera.rect.y))

    def reset_position(self):
        self.rect.center = (171, 904)
