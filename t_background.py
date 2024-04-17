import pygame as pg
import sys
import random as rnd

pg.init()
win = pg.display.set_mode((500, 500))
background = pg.image.load("images/background.png").convert()


class cam:
    def __init__(self, x, y):
        self.rect = pg.Rect(x, y, 500, 500)

    def move(self, vector):
        self.rect[0] += vector[0]
        self.rect[1] += vector[1]


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

    def draw(self):
        win.blit(self.image, (self.rect.x - camera.rect.x, self.rect.y - camera.rect.y))


class Bus:
    def __init__(self, x, y, speed):
        self.image = pg.image.load("images/bus.png").convert_alpha()
        self.rect = self.image.get_rect().inflate(-50, -50)
        self.rect.topleft = (x, y)
        self.speed = speed

    def move(self):
        self.rect.x += self.speed
        if self.rect.left > 500 or self.rect.right < 0:
            self.speed = -self.speed

    def draw(self):
        win.blit(self.image, (self.rect.x - camera.rect.x, self.rect.y - camera.rect.y))


player = Player()
camera = cam(0, 0)

buses = [Bus(0, 250, 3)]

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                buses.append(
                    Bus(rnd.randint(0, 400), rnd.randint(0, 400), rnd.choice([-3, 3]))
                )

    vector = [0, 0]

    kpressed = pg.key.get_pressed()
    if kpressed[pg.K_UP]:
        vector[1] -= 3
    elif kpressed[pg.K_DOWN]:
        vector[1] += 3

    if kpressed[pg.K_LEFT]:
        vector[0] -= 3
    elif kpressed[pg.K_RIGHT]:
        vector[0] += 3

    if vector != [0, 0]:
        player.move(vector)
        player.update()
        camera.move(vector)

    for bus in buses:
        bus.move()
        if bus.rect.colliderect(player.rect):
            print("Collision occurred!")
            pg.quit()
            sys.exit()

    win.fill((255, 255, 255))
    win.blit(background, (-camera.rect[0], -camera.rect[1]))
    player.draw()

    for bus in buses:
        bus.draw()

    pg.display.flip()
    pg.time.wait(30)
