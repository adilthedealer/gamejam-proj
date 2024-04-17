import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("тест")

# Загрузка изображения фона
background = pygame.image.load("images/background.jpg")

class Runner(pygame.sprite.Sprite):
    def init(self):
        super().init()
        self.run_images = [
            pygame.image.load("images/running_student1.png"),
            pygame.image.load("images/running_student2.png")
        ]
        self.current_run_image = 0  # Index to track the current run image
        self.image = pygame.image.load("images/standing_student.png")
        self.original_image = self.image.copy()  # Original image for reference
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed = 5
        self.running_tick = 0  # Tick counter to alternate between images
        self.run_delay = 10  # Delay to change run images
        self.angle = 0  # Initial angle of rotation

    def update(self):
        keys = pygame.key.get_pressed()
        
        # Running animation logic
        directions = {
            pygame.K_LEFT: (-self.speed, 0, -90),
            pygame.K_RIGHT: (self.speed, 0, 90),
            pygame.K_UP: (0, -self.speed, 0),
            pygame.K_DOWN: (0, self.speed, 180)
        }

        for key, (dx, dy, angle) in directions.items():
            if keys[key] and self.rect.move(dx, dy).colliderect(screen.get_rect()):
                self.rect.x += dx
                self.rect.y += dy
                if angle is not None:
                    self.angle = angle
                self.running_tick += 1
                if self.running_tick >= self.run_delay:
                    self.current_run_image = (self.current_run_image + 1) % len(self.run_images)
                    self.image = self.run_images[self.current_run_image]
                    self.running_tick = 0
                break  # Only allow one direction at a time
        
        # Rotate the image
        self.image = pygame.transform.rotate(self.original_image, self.angle)

all_sprites = pygame.sprite.Group()
character = Runner()
all_sprites.add(character)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отображение фона
    screen.blit(background, (0, 0))

    all_sprites.update()

    all_sprites.draw(screen)
    pygame.display.flip()

    pygame.time.Clock().tick(30)

pygame.quit()