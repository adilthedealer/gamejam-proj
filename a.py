import pygame as pg
import time

# Initialize Pygame
pg.init()

# Set up the screen
screen_width = 500
screen_height = 500
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Traffic Light Simulation")

# Load images
background = pg.image.load("images/newbg.png").convert()
green = pg.image.load("images/lights/green_light.png")
red = pg.image.load("images/lights/red_light.png")
yellow = pg.image.load("images/lights/yellow_light.png")

# Create a list of images
lights = [green, yellow, red, yellow]
current_light_index = 0

# Timing variables for each color
green_interval = 2  # Initial interval for green light (5 seconds)
yellow_interval = 1  # Initial interval for yellow light (2 seconds)
red_interval = 2  # Initial interval for red light (4 seconds)

# Time tracking variables for each color
last_green_time = time.time()
last_yellow_time = time.time()
last_red_time = time.time()

# Main loop
running = True
while running:
    # Handle events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            # Speed up or slow down interval with arrow keys
            if event.key == pg.K_g:  # Adjust green light interval
                green_interval = max(1, green_interval - 1)
            elif event.key == pg.K_y:  # Adjust yellow light interval
                yellow_interval = max(1, yellow_interval - 1)
            elif event.key == pg.K_r:  # Adjust red light interval
                red_interval = max(1, red_interval - 1)
            elif event.key == pg.K_h:  # Increase green light interval
                green_interval += 1
            elif event.key == pg.K_u:  # Increase yellow light interval
                yellow_interval += 1
            elif event.key == pg.K_j:  # Increase red light interval
                red_interval += 1

    # Check if it's time to change the light
    current_time = time.time()
    if current_light_index == 0 and current_time - last_green_time >= green_interval:
        current_light_index = 1  # Change to yellow
        last_yellow_time = current_time
    elif current_light_index == 1 and current_time - last_yellow_time >= yellow_interval:
        current_light_index = 2  # Change to red
        last_red_time = current_time
    elif current_light_index == 2 and current_time - last_red_time >= red_interval:
        current_light_index = 3  # Change to yellow
        last_yellow_time = current_time
    elif current_light_index == 3 and current_time - last_yellow_time >= yellow_interval:
        current_light_index = 0  # Change to green
        last_green_time = current_time

    # Draw background
    screen.blit(background, (0, 0))

    # Draw current light
    current_light = lights[current_light_index]
    light_width, light_height = current_light.get_size()
    screen.blit(current_light, ((screen_width - light_width) // 2, (screen_height - light_height) // 2))  # Center the light

    # Update the display
    pg.display.flip()

    # Cap the frame rate
    pg.time.Clock().tick(60)

# Quit Pygame
pg.quit()
