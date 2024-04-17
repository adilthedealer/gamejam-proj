import pygame
import random

pygame.init()

WHITE = (255, 255, 255)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("тест")

background = pygame.image.load("images/background.jpg")
background_width, background_height = background.get_size()

class Runner(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.run_images = [
            pygame.image.load("images/running_student1.png"),
            pygame.image.load("images/running_student2.png"),
        ]
        self.current_run_image = 0  # Index to track the current run image
        self.image = pygame.image.load("images/standing_student.png")
        self.original_image = self.image.copy()  # Original image for reference
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed = 2  # Decreased player speed
        self.running_tick = 0  # Tick counter to alternate between images
        self.run_delay = 10  # Delay to change run images

    def update(self):
        keys = pygame.key.get_pressed()

        # Running animation logic
        for key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
            if keys[key]:
                self.running_tick += 1
                if self.running_tick >= self.run_delay:
                    self.current_run_image = (self.current_run_image + 1) % len(self.run_images)
                    self.image = self.run_images[self.current_run_image]
                    self.running_tick = 0
                break

        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx = -self.speed
        elif keys[pygame.K_RIGHT]:
            dx = self.speed
        elif keys[pygame.K_UP]:
            dy = -self.speed
        elif keys[pygame.K_DOWN]:
            dy = self.speed

        self.rect.move_ip(dx, dy)  # Move the player

    def draw(self, surface):
        surface.blit(self.image, self.rect)


all_sprites = pygame.sprite.Group()
character = Runner()
all_sprites.add(character)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    character.update()

    # Calculate background position based on player's position
    bg_x = -(character.rect.centerx - SCREEN_WIDTH // 2)
    bg_y = -(character.rect.centery - SCREEN_HEIGHT // 2)

    screen.fill(WHITE)  # Fill screen with white color
    screen.blit(background, (bg_x, bg_y))

    all_sprites.draw(screen)
    character.draw(screen)

    pygame.display.flip()

pygame.quit()
