import pygame as pg
import sys
import time
from camera import Camera
from player import Player
from upper_car import Upper_car
from mc_grandma import MCGrandma
from trafficlight import TrafficLight

def gr_minigame():
    pg.init()
    win = pg.display.set_mode((500, 500))
    background = pg.image.load("images/BG2.png").convert()
    gameover = pg.image.load("images/wasted.png")

    # Adjust the initial position of the player to the center of the window
    initial_player_x = 250
    initial_player_y = 250

    mcgrandma = MCGrandma(154, 400)

    initial_camera_x = 0
    initial_camera_y = 0

    camera = Camera(
        initial_camera_x,
        initial_camera_y,
        background.get_width(),
        background.get_height(),
        mcgrandma.rect,
    )

    upper_cars = [
        Upper_car(0, 530, "yellow"),
        Upper_car(1500, 620, "red"),
        Upper_car(1600, 720, "blue"),
    ]

    trafficlight = [TrafficLight(background), TrafficLight(background)]

    exit_minigame = False

    while not exit_minigame:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        for tr in trafficlight:
            tr.update()
        
        vector = [0, 0]
        camera.move(vector)

        kpressed = pg.key.get_pressed()
        if kpressed[pg.K_UP]:
            vector[1] -= 2
        elif kpressed[pg.K_DOWN]:
            vector[1] += 2

        if kpressed[pg.K_LEFT]:
            vector[0] -= 2
        elif kpressed[pg.K_RIGHT]:
            vector[0] += 2

        if vector != [0, 0]:
            camera.move(vector)
            mcgrandma.move(vector)
            mcgrandma.update()
        

        win.fill((255, 255, 255))
        win.blit(background, (-camera.rect[0], -camera.rect[1]))
        mcgrandma.draw(win, camera)

        if mcgrandma.rect.y >= 884:
            exit_minigame = True


        # движение машины и реакция игрока на хитбокс (верхняя улица)
        for car in upper_cars:
            car.move(trafficlight[0])  # Передаём объект светофора в метод move
            if car.rect.colliderect(mcgrandma.rect):
                win.blit(
                    gameover,
                    (
                        (win.get_width() - gameover.get_width()) // 2,
                        (win.get_height() - gameover.get_height()) // 2,
                    ),
                )
                pg.display.update()
                time.sleep(4)
                pg.quit()
                sys.exit()

        for tr in trafficlight:
            tr.draw(background, 225, 450)
            tr.draw(background, 225, 850)

        for car in upper_cars:
            car.draw(win, camera)

        pg.display.flip()
        pg.time.wait(30)