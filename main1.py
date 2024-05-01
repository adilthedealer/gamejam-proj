import pygame as pg
import sys
import time
import random as rnd
import subprocess
from gr_minigame import gr_minigame
from pygame.locals import *
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



class PopupWindow:
    def __init__(self, position):
        self.font = pg.font.Font("Pixel_font.ttf", 24)
        self.window_color = (0, 0, 0, 150)
        self.text_color = (255, 255, 255)

        self.message = "Will you help me, an old lady, grandson?"
        self.options = ["Yes", "No"]

        self.window_rect = pg.Rect(position, (500, 150))

        self.message_surface = self.font.render(self.message, True, self.text_color)
        self.message_rect = self.message_surface.get_rect(center=(self.window_rect.centerx, self.window_rect.centery - 20))

        self.option_rects = []
        self.option_texts = []
        for i, option in enumerate(self.options):
            text_surface = self.font.render(option, True, self.text_color)
            text_rect = text_surface.get_rect()
            text_rect.center = (self.window_rect.centerx + (i - 0.5) * 200, self.window_rect.centery + 20)
            self.option_texts.append(text_surface)
            self.option_rects.append(text_rect)

        # Initialize yes and no rectangles
        self.yes_rect = self.option_rects[0]
        self.no_rect = self.option_rects[1]

    def draw(self, screen):
        pg.draw.rect(screen, self.window_color, self.window_rect)

        screen.blit(self.message_surface, self.message_rect)

        for text, rect in zip(self.option_texts, self.option_rects):
            screen.blit(text, rect)

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            for i, rect in enumerate(self.option_rects):
                if rect.collidepoint(mouse_pos):
                    return self.options[i]
        return None
    

def draw_pause_menu(win):
    # Draw a transparent green overlay
    overlay = pg.Surface((500, 500), pg.SRCALPHA)
    overlay.fill((0, 255, 0, 128))  # Transparent green color
    win.blit(overlay, (0, 0))

    # Draw pause menu options
    font = pg.font.SysFont("Pixel_font.ttf", 30)
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
    pg.display.set_caption("Level 1")
    background = pg.image.load("images/BG2.png").convert()
    gameover = pg.image.load("images/wasted.png")

    background_music = pg.mixer.Sound("sounds/bgmusic.mp3")
    background_music.play(-1) 
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

    buses = [Bus(806, 398, 20)]
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
    # Timer event type
    TIMER_EVENT = pg.USEREVENT + 1

    # Set the timer for 3 seconds (3000 milliseconds)

    is_paused = False
    popup = None

    while True:
        for event in pg.event.get():
            if event.type == MOUSEBUTTONDOWN:
                # Get mouse position
                mouse_pos = pg.mouse.get_pos()

                # Check if mouse position collides with "Yes" option rectangle
                if popup.yes_rect.collidepoint(mouse_pos):
                    choice = "Yes"
                # Check if mouse position collides with "No" option rectangle
                elif popup.no_rect.collidepoint(mouse_pos):
                    choice = "No"

                # If a choice is made, perform corresponding action
                if choice:
                    if choice == "Yes":
                        minigame_result = gr_minigame(win)
                        if minigame_result:
                            background_music.stop()
                            thx = pg.mixer.Sound("sounds/thank_u.wav")
                            thx.play()
                            background_music.play(-1)
                            gra.clear()
                            player.reset_position()
                            camera.rect.center = player.rect.center
                            popup = None
                    elif choice == "No":
                        gra.clear()
                        camera.rect.center = player.rect.center
                        popup = None
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == TIMER_EVENT:
                break
            elif event.type == pg.KEYDOWN:
                # if event.key == pg.K_SPACE:
                #     buses.append(
                #         Bus(
                #             rnd.randint(0, 400),
                #             rnd.randint(0, 400),
                #             rnd.choice([-3, 3]),
                #         )
                #     )
                if event.key == pg.K_ESCAPE:
                    # Toggle pause
                    is_paused = not is_paused
            for grandma in gra:
                if grandma.rect.colliderect(player.rect) and popup is None:
                    popup = PopupWindow((0, 100))

            # Handle popup events
            if popup:
                popup.draw(win)
                choice = None

                for event in pg.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        choice = popup.handle_event(event)
                        if choice:
                            if choice == "Yes":
                                minigame_result = gr_minigame(win)
                                if minigame_result:
                                    gra.clear()
                                    player.reset_position()
                                    camera.rect.center = player.rect.center
                                    popup = None
                                    break  # Exit the event loop
                            elif choice == "No":
                                gra.clear()
                                camera.rect.center = player.rect.center
                                popup = None  # Reset popup after choice
                                break  # Exit the event loop

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
                background_music.stop()
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
                background_music.stop()
                buss = pg.mixer.Sound("sounds/bus.mp3")
                buss.play(maxtime=2500)
                think = pg.mixer.Sound("sounds/thinking.mp3")
                current_time = bus.ticks
                dx = pg.time.get_ticks() - current_time
                if dx >= 6000:
                    think.play()
                    win.blit(
                        pg.image.load("images/story/level1epilogue1.png"),
                        (
                            (win.get_width() - gameover.get_width()) // 2,
                            (win.get_height() - gameover.get_height()) // 2,
                        ),
                    )
                    time.sleep(5)
                    pg.display.update()
                    win.blit(
                        pg.image.load("images/levels/level2.png"),
                        (
                            (win.get_width() - gameover.get_width()) // 2,
                            (win.get_height() - gameover.get_height()) // 2,
                        ),
                    )
                    time.sleep(14)
                    pg.display.update()
                    think.stop()
                    subprocess.run(["python", "main2.py"])
                    pg.quit()

        # Move upper cars and check collision with player
        for car in upper_cars:
            car.move(trafficlight[0])
            if car.rect.colliderect(player.rect):
                background_music.stop()
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

        # Move lower cars and check collision with player
        for car in lower_cars:
            car.move(trafficlight[1])
            if car.rect.colliderect(player.rect):
                background_music.stop()
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

        # Check for collision with grandma
        for grandma in gra:
            if grandma.rect.colliderect(player.rect) and popup is None:
                popup = PopupWindow((0, 100))



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

                # Handle popup events
        if popup:
            popup.draw(win)
            choice = None

            for event in pg.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    choice = popup.handle_event(event)
                    if choice:
                        if choice == "Yes":
                            minigame_result = gr_minigame(win)
                            if minigame_result:
                                background_music.stop()
                                thx = pg.mixer.Sound("sounds/thank_u.wav")
                                thx.play()
                                background_music.play(-1)
                                gra.clear()
                                player.reset_position()
                                camera.rect.center = player.rect.center
                                popup = None
                        elif choice == "No":
                            gra.clear()
                            camera.rect.center = player.rect.center
                            popup = None  # Reset popup after choice

        pg.display.flip()
        pg.time.wait(30)


main1()
