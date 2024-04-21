import pygame as pg
import sys
import time
import random as rnd
import subprocess
from gr_minigame import gr_minigame
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


def draw_pause_menu(win):
    # Draw a transparent green overlay
    overlay = pg.Surface((500, 500), pg.SRCALPHA)
    overlay.fill((0, 255, 0, 128))  # Transparent green color
    win.blit(overlay, (0, 0))

    # Draw pause menu options
    font = pg.font.SysFont(None, 30)
    text_continue = font.render("Continue", True, (255, 255, 255))
    text_settings = font.render("Settings", True, (255, 255, 255))
    text_exit = font.render("Exit", True, (255, 255, 255))

    win.blit(text_continue, (200, 200))
    win.blit(text_settings, (200, 250))
    win.blit(text_exit, (200, 300))

def main1():
    pg.init()
    pg.mixer.init()
    win = pg.display.set_mode((500, 500))
    background = pg.image.load("images/BG2.png").convert()
    gameover = pg.image.load("images/wasted.png")
    pg.mixer.Sound("sounds/bgmusic.mp3").play(-1)
    # pg.mixer.Sound("sounds/bgmusic.mp3").set_volume(0.2)  


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

    # Create NPC objects
    npc = [NPC(900, 1500, 4, ""), NPC(150, 900, 1, "")]
    npcdown = [NPCDown(1750, 1540, 4, "3"), NPCDown(871, 916, 0.5, "2")]
    npcup = [NPCUp(900, 1600, 1.5, "3")]
    npcleft = [NPCLeft(1770, 1499, 2.3, "2"), NPCLeft(1150, 433, 0.5, "")]
    gra = [Grandma(154, 400)]
    # mc_grandma = MCGrandma(154, 400, 3)

    is_paused = False

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
                elif event.key == pg.K_ESCAPE:
                    # Toggle pause
                    is_paused = not is_paused

        if is_paused:
            draw_pause_menu(win)
            pg.display.flip()
            continue

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

        for grandma in gra:
            grandma.move()

        for tr in trafficlight:
            tr.update()

        # Move buses and check collision with player
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
            elif bus.distance_to_stop(player) <= 65:
                win.blit(
                    pg.image.load("images/levels/level2.png"),
                    (
                        (win.get_width() - gameover.get_width()) // 2,
                        (win.get_height() - gameover.get_height()) // 2,
                    ),
                )
                pg.display.update()
                time.sleep(2)
                subprocess.run(["python", "main2.py"])
                pg.quit()

        # Move upper cars and check collision with player
        for car in upper_cars:
            car.move(trafficlight[0])
            if car.rect.colliderect(player.rect):
                pg.mixer.music.stop()
                pg.mixer.Sound("sounds/crash.mp3").play()
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

        # Move lower cars and check collision with player
        for car in lower_cars:
            car.move(trafficlight[1])
            if car.rect.colliderect(player.rect):
                pg.mixer.music.stop()
                pg.mixer.Sound("sounds/crash.mp3").play()
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

        # Check collision with grandma (mini-game)
        for grandma in gra:
            if grandma.rect.colliderect(player.rect):
                gr_minigame()
                gra.clear()
                player.reset_position()
                camera.rect.center = player.rect.center

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

        for gr in gra:
            gr.draw(win, camera)

        for tr in trafficlight:
            tr.draw(background, 225, 450)
            tr.draw(background, 225, 850)

        pg.display.flip()
        pg.time.wait(30)


main1()
