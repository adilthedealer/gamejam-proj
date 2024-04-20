import pygame as pg
import sys
from player import Player
from camera import Camera


def main3():
    pg.init()
    win = pg.display.set_mode((500, 500))
    background = pg.image.load("images/BG3.png").convert()

    # Adjust the initial position of the player
    initial_player_x = 250
    initial_player_y = 250

    player = Player()
    player.rect.center = (initial_player_x, initial_player_y)

    # Adjust the initial position of the camera
    initial_camera_x = 0
    initial_camera_y = 0

    camera = Camera(
        initial_camera_x,
        initial_camera_y,
        background.get_width(),
        background.get_height(),
        player.rect,
    )

    clock = pg.time.Clock()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

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
            player.move(vector)  # Pass the vector to the move method
            player.update()
            camera.move(vector)


        win.fill((255, 255, 255))
        win.blit(background, (-camera.rect.x, -camera.rect.y))
        player.draw(win, camera)

        pg.display.flip()
        clock.tick(30)


main3()
