import pygame as pg
import sys
import random as rnd
from player import Player
from bus import Bus
from camera import Camera

pg.init()
win = pg.display.set_mode((500, 500))
background = pg.image.load("images/background.png").convert()

player = Player()
camera = Camera(0, 0)

buses = [Bus(0, 250, 3)]

while True:
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
    player.draw(win, camera)

    for bus in buses:
        bus.draw(win, camera)

    pg.display.flip()
    pg.time.wait(60)
