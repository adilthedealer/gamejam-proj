import pygame as pg
import sys
import time
from camera import Camera
from player1 import Player1
from bus import Bus


def main3():
    pg.init()
    pg.mixer.init()
    win = pg.display.set_mode((500, 500))
    pg.display.set_caption("Level 3")
    background = pg.image.load("images/BG3.png").convert_alpha()
    gameover = pg.image.load("images/story/level3story.png")
    
    background_music = pg.mixer.Sound("sounds/birds.mp3")
    background_music.play(-1)
    steps = pg.mixer.Sound("sounds/steps.mp3")
    steps.play(-1)

    player = Player1(50, 1072)
    player.rect.center = (player.rect.centerx, player.rect.centery)

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

    # buses = [Bus(868, 382, 8)]
    clock = pg.time.Clock()

    travel_allowed = True
    while travel_allowed:
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

            # Update camera position to center on the player
            camera.rect.center = player.rect.center
            camera.move([0, 0])

        if player.distance_traveled >= 2500000:
            think = pg.mixer.Sound("sounds/thinking.mp3")
            background_music.stop()
            steps.stop()
            think.play()
            win.blit(
                gameover,
                (
                    (win.get_width() - gameover.get_width()) // 2,
                    (win.get_height() - gameover.get_height()) // 2,
                ),
            )
            pg.display.update()
            time.sleep(10)
            win.blit(
                pg.image.load("images/story/level3epilogue.png"),
                (
                    0, 0
                ),
            )
            pg.display.update()
            time.sleep(10)
            win.blit(
                pg.image.load("images/story/level3epilogue2.png"),
                (
                    0, 0
                ),
            )
            pg.display.update()
            time.sleep(10)
            win.blit(
                pg.image.load("images/story/level3epilogue3.png"),
                (
                    0, 0
                ),
            )
            pg.display.update()
            time.sleep(10)
            think.stop()
            pg.quit()
            sys.exit()

        win.fill((255, 255, 255))
        win.blit(background, (-camera.rect.x, -camera.rect.y))
        player.draw(win, camera)

        pg.display.flip()
        clock.tick(30)


main3()
