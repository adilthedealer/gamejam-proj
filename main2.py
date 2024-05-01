import pygame as pg
import sys
import time
import subprocess
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
from kapli import Raindrop

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

def create_raindrops(num_raindrops):
    raindrops = []
    for _ in range(num_raindrops):
        x = rnd.randint(0, 500)  # Adjust this value according to your window size
        y = rnd.randint(-100, -10)
        raindrops.append(Raindrop(x, y))
    return raindrops

def draw_raindrops(raindrops, surface):
    for raindrop in raindrops:
        raindrop.draw(surface)

def update_raindrops(raindrops):
    for raindrop in raindrops:
        raindrop.fall()

def main2():
    pg.init()
    pg.mixer.init()
    win = pg.display.set_mode((500, 500))
    pg.display.set_caption("Level 2")
    background = pg.image.load("images/BGrain.png").convert()
    gameover = pg.image.load("images/wasted.png")

    background_music = pg.mixer.Sound("sounds/rain.mp3")
    background_music.play(-1)
    steps = pg.mixer.Sound("sounds/steps.mp3")
    steps.play(-1)
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

    npc = [NPC(900, 1500, 4, ""), NPC(150, 900, 1, "")]
    npcdown = [NPCDown(1750, 1540, 4, "3"), NPCDown(871, 916, 0.5, "2")]
    npcleft = [NPCLeft(1770, 1499, 2.3, "2"), NPCLeft(1150, 433, 0.5, "")]
    luke = [Luke(1700, 1700), Luke(1730, 1470), Luke(950, 1450)]
    luzha = [Luzha(1500, 1450), Luzha(1430, 1485), Luzha(860, 1485)]

    raindrops = create_raindrops(100)  # Adjust the number of raindrops as needed

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
                    is_paused = True

        if is_paused:
            draw_pause_menu(win)
            pg.display.flip()
            continue

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

        for npcl in npcleft:
            npcl.move()
            npcl.update()

        for luk in luke:
            luk.move()

        for luzh in luke:
            luzh.move()

        for tr in trafficlight:
            tr.update()

        for bus in buses:
            bus.move(player)
            if bus.rect.colliderect(player.rect):
                background_music.stop()
                steps.stop()
                crash = pg.mixer.Sound("sounds/crash.mp3")
                crash.play()
                scream = pg.mixer.Sound("sounds/scream.mp3")
                scream.play()
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
            elif not bus.stopped:
                steps.stop()
                buss = pg.mixer.Sound("sounds/bus.mp3")
                think = pg.mixer.Sound("sounds/thinking.mp3")
                buss.play(maxtime=2500)
                current_time = bus.ticks
                dx = pg.time.get_ticks() - current_time
                if dx >= 6000:
                    background_music.stop()
                    think.play()
                    win.blit(
                        pg.image.load("images/story/level2epilogue.png"),
                        (
                            (win.get_width() - gameover.get_width()) // 2,
                            (win.get_height() - gameover.get_height()) // 2,
                        ),
                    )
                    time.sleep(5)
                    pg.display.update()
                    win.blit(
                        pg.image.load("images/levels/level3.png"),
                        (
                            (win.get_width() - gameover.get_width()) // 2,
                            (win.get_height() - gameover.get_height()) // 2,
                        ),
                    )
                    time.sleep(14)
                    pg.display.update()
                    think.stop()
                    subprocess.run(["python", "main3.py"])
                    pg.quit()

        for car in upper_cars:
            car.move(trafficlight[0])
            if car.rect.colliderect(player.rect):
                background_music.stop()
                steps.stop()
                crash = pg.mixer.Sound("sounds/crash.mp3")
                crash.play()
                scream = pg.mixer.Sound("sounds/scream.mp3")
                scream.play()
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

        for car in lower_cars:
            car.move(trafficlight[1])
            if car.rect.colliderect(player.rect):
                background_music.stop()
                steps.stop()
                crash = pg.mixer.Sound("sounds/crash.mp3")
                crash.play()
                scream = pg.mixer.Sound("sounds/scream.mp3")
                scream.play()
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
                background_music.stop()
                steps.stop()
                scream = pg.mixer.Sound("sounds/scream.mp3")
                scream.play()
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
                background_music.stop()
                steps.stop()
                puddl = pg.mixer.Sound("sounds/puddle.mp3")
                puddl.play()
                background_music.play(-1)
                steps.play(-1)
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

        # Draw Luzha objects first
        for luz in luzha:
            luz.draw(win, camera)


        # Draw other game elements
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


        for npcl in npcleft:
            npcl.draw(win, camera)

        for lk in luke:
            lk.draw(win, camera)
        
        # Draw player after Luzha objects
        player.draw(win, camera)

        for tr in trafficlight:
            tr.draw(background, 225, 450)
            tr.draw(background, 225, 850)

        update_raindrops(raindrops)
        draw_raindrops(raindrops, win)

        pg.display.flip()
        pg.time.wait(30)


main2()