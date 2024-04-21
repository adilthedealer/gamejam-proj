import pygame
import subprocess, os
import time
import sys


def init_display():
    pygame.init()
    pygame.display.set_caption("Press Enter to Start")
    return pygame.display.set_mode((800, 600))


def load_assets():
    game_logo = pygame.image.load("images/name_2x.png").convert_alpha()
    font = pygame.font.Font("Pixel_font.ttf", 36)
    start_text = font.render("Press ENTER to Start", True, (255, 255, 255))
    return game_logo, start_text


def draw_text(screen, text, position):
    screen.blit(text, position)


def main():
    screen = init_display()
    game_logo, start_text = load_assets()

    logo_pos = (screen.get_width() // 2 - game_logo.get_width() // 2, 50)
    text_pos = (screen.get_width() // 2 - start_text.get_width() // 2, 400)

    running = True
    while running:
        screen.fill((0, 0, 0))

        screen.blit(game_logo, logo_pos)
        screen.blit(start_text, text_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    screen.blit(pygame.image.load("images/story/level1prologue.png"), (0, 0))
                    pygame.display.update()
                    time.sleep(3.5)
                    screen.blit(pygame.image.load("images/story/level1prologue2.png"), (-200, -200))
                    pygame.display.update()
                    time.sleep(2)
                    subprocess.run(["python", "main1.py"])
                    running = False
                    # pygame.quit()

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
