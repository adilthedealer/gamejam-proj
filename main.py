import pygame as pg
import sys
import random as rnd
from player import Player
from bus import Bus
from camera import Camera

pg.init()
win = pg.display.set_mode((500, 500))
background = pg.image.load("images/background.png").convert()

# Adjust the initial position of the player to the center of the window
initial_player_x = 250
initial_player_y = 250

player = Player()
player_rect = pg.Rect(initial_player_x, initial_player_y, player.image.get_width(), player.image.get_height())

# Adjust the initial position of the camera to the lower right corner
initial_camera_x = background.get_width() - 500
initial_camera_y = background.get_height() - 500

camera = Camera(
    initial_camera_x, initial_camera_y, background.get_width(), background.get_height(), player_rect
)

buses = [Bus(0, 500, 8)]

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
    camera.move(vector)

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
            print("Game over!")
            pg.quit()
            sys.exit()

    win.fill((255, 255, 255))
    win.blit(background, (-camera.rect[0], -camera.rect[1]))
    player.draw(win, camera)

    for bus in buses:
        bus.draw(win, camera)

    pg.display.flip()
    pg.time.wait(30)