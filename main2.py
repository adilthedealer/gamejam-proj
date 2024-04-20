import pygame as pg
import sys
import time
import random as rnd
from player import Player
from bus import Bus
from camera import Camera
from upper_car import Upper_car
from lower_car import Lower_car
from trafficlight import TrafficLight
from npc import NPC
from npcdown import NPCDown
from npcup import NPCUp
from npcleft import NPCLeft
from grandma import Grandma
from luke import Luke
from luzha import Luzha


def main():
    pg.init()
    win = pg.display.set_mode((500, 500))
    background = pg.image.load("images/BGrain.png").convert()
    gameover = pg.image.load("images/wasted.png")

    # Adjust the initial position of the player to the center of the window
    initial_player_x = 250
    initial_player_y = 250

    player = Player()
    player_rect = pg.Rect(
        initial_player_x,
        initial_player_y,
        player.image.get_width(),
        player.image.get_height(),
    )

    # Adjust the initial position of the camera to the lower right corner
    initial_camera_x = background.get_width() - 500
    initial_camera_y = background.get_height() - 500

    camera = Camera(
        initial_camera_x,
        initial_camera_y,
        background.get_width(),
        background.get_height(),
        player_rect,
    )

    buses = [Bus(806, 398, 8)]
    lower_cars = [Lower_car(400, 1200, "blue")]
    upper_cars = [
        Upper_car(0, 530, "yellow"),
        Upper_car(1500, 620, "red"),
        Upper_car(1600, 720, "blue"),
    ]
    trafficlight = [TrafficLight(background), TrafficLight(background)]

    # Создайте объект NPC
    npc = [NPC(900, 1500, 4, ""), NPC(150, 900, 1, "")]
    npcdown = [NPCDown(1750, 1540, 4, "3"), NPCDown(871, 916, 0.5, "2")]
    npcup = [NPCUp(900, 1600, 1.5, "3")]
    npcleft = [NPCLeft(1770, 1499, 2.3, "2"), NPCLeft(1150, 433, 0.5, "")]
    luke = [Luke(1700, 1700), Luke(1730, 1470), Luke(950, 1450)]
    luzha = [Luzha(1500, 1450), Luzha(1430, 1485), Luzha(860, 1485)]
    

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    buses.append(
                        Bus(
                            rnd.randint(0, 400),
                            rnd.randint(0, 400),
                            rnd.choice([-3, 3]),
                        )
                    )

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
            player.move(vector)
            player.update()
            camera.move(vector)

        for np in npc:
            np.move()
            np.update()

        for npcd in npcdown:
            npcd.move()
            npcd.update()

        for npcu in npcup:
            npcu.move()
            npcu.update()

        for npcl in npcleft:
            npcl.move()
            npcl.update()

        for luk in luke:
            luk.move()

        for luzh in luke:
            luzh.move()

        for tr in trafficlight:
            tr.update()

        # движение автобуса и реакция игрока на хитбокс
        for bus in buses:
            bus.move(player)
            if bus.rect.colliderect(player.rect):
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

        # движение машины и реакция игрока на хитбокс (верхняя улица)
        for car in upper_cars:
            car.move(trafficlight[0])  # Передаём объект светофора в метод move
            if car.rect.colliderect(player.rect):
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

        # движение машины и реакция игрока на хитбокс (нижняя улица)
        for car in lower_cars:
            car.move(trafficlight[1])  # Передаём объект светофора в метод move
            if car.rect.colliderect(player.rect):
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


        for luk in luke:
            if luk.rect.colliderect(player.rect):
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

        for luzh in luzha:
            if luzh.rect.colliderect(player.rect):
                vector[1] += 1
                vector[1] -= 1
                vector[0] += 1
                vector[0] -= 1
                player.move(vector)
                player.update()
                camera.move(vector)
                pg.time.wait(60)

                    

        win.fill((255, 255, 255))
        win.blit(background, (-camera.rect[0], -camera.rect[1]))
        player.draw(win, camera)

        for bus in buses:
            bus.draw(win, camera)

        for car in upper_cars:
            car.draw(win, camera)

        for car in lower_cars:
            car.draw(win, camera)

        for np in npc:
            np.draw(win, camera)

        for npcd in npcdown:
            npcd.draw(win, camera)

        for npcu in npcup:
            npcu.draw(win, camera)

        for npcl in npcleft:
            npcl.draw(win, camera)

        for lk in luke:
            lk.draw(win, camera)

        for luz in luzha:
            luz.draw(win, camera)

        for tr in trafficlight:
            tr.draw(background, 225, 450)
            tr.draw(background, 225, 850)

        pg.display.flip()
        pg.time.wait(30)


main()