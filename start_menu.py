import pygame
from pygame.locals import *

def load_assets():
    game_name = pygame.image.load('images\name_2x.png')
    game_width = game_name.get_width()
    font = pygame.font.Font("Pixel_font.ttf", 72)
    start_text = font.render("Start", True, (255, 255, 255))
    exit_text = font.render("Exit", True, (255, 255, 255))
    return game_name, game_width, font, start_text, exit_text

def draw_text(screen, text, position, color):
    screen.blit(text, position, color)

def main():
    # Init pygame
    pygame.init()

    # Set width and height
    W = 1000
    H = 800

    # Create game window
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Bus Runner")

    # Set framerate
    clock = pygame.time.Clock()
    fps = 60

    game_name, game_width, font, start_text, exit_text = load_assets()

    # Text positions
    start_text_pos = (W // 2 - start_text.get_width() // 2, H // 2 - start_text.get_height() // 2)
    exit_text_pos = (W // 2 - exit_text.get_width() // 2, H // 2 - exit_text.get_height() // 2 + start_text.get_height())

    # Text rects
    start_text_rect = start_text.get_rect(topleft=start_text_pos)
    exit_text_rect = exit_text.get_rect(topleft=exit_text_pos)

    run = True
    while run:
        # Clear the screen
        screen.fill((0, 0, 0))
        
        # Calculate position to center the image
        name_x = (W - game_width) // 2
        name_y = 0
        
        # Blit the image
        screen.blit(game_name, (name_x, name_y))
        
        # Set fps
        clock.tick(fps)
        
        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    if exit_text_rect.collidepoint(event.pos):
                        run = False  # Close the game when "Exit" text is clicked

        # Get mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Check if mouse is hovering over start text
        if start_text_rect.collidepoint(mouse_pos):
            draw_text(screen, font.render("Start", True, (255, 255, 0)), start_text_pos, None)  # Yellow when hovered
        else:
            draw_text(screen, start_text, start_text_pos, None)  # White when not hovered

        # Check if mouse is hovering over exit text
        if exit_text_rect.collidepoint(mouse_pos):
            draw_text(screen, font.render("Exit", True, (255, 255, 0)), exit_text_pos, None)  # Yellow when hovered
        else:
            draw_text(screen, exit_text, exit_text_pos, None)  # White when not hovered

        # Update the display
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
