import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bus Runner")

background = pygame.image.load("images/background.png")


class Bus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/bus.png")
        self.rect = self.image.get_rect().inflate(-20, -40)
        self.rect.left = 0  # Start the bus from the left side
        self.rect.centery = SCREEN_HEIGHT // 2
        self.speed = 3

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > SCREEN_WIDTH:
            self.rect.right = (
                0  # Reset the bus to the left side when it reaches the right
            )


class Runner(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.run_images = [
            pygame.image.load("images/running_student1.png"),
            pygame.image.load("images/running_student2.png"),
        ]
        self.current_run_image = 0
        self.image = pygame.image.load("images/standing_student.png")
        self.original_image = self.image.copy()
        self.rect = self.image.get_rect().inflate(-20, -40)
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed = 5
        self.running_tick = 0
        self.run_delay = 10
        self.angle = 0

    def update(self):
        keys = pygame.key.get_pressed()

        dx, dy, angle = 0, 0, None

        if keys[pygame.K_LEFT]:
            dx -= self.speed
            angle = 90
        if keys[pygame.K_RIGHT]:
            dx += self.speed
            angle = -90
        if keys[pygame.K_UP]:
            dy -= self.speed
            angle = 0
        if keys[pygame.K_DOWN]:
            dy += self.speed
            angle = 180

        if dx != 0 and dy != 0:  # Diagonal movement
            dx *= 0.7071
            dy *= 0.7071

        if self.rect.move(dx, dy).colliderect(screen.get_rect()):
            self.rect.x += dx
            self.rect.y += dy

        # Update running animation
        self.running_tick += 1
        if self.running_tick >= self.run_delay:
            self.current_run_image = (self.current_run_image + 1) % len(self.run_images)
            self.image = self.run_images[self.current_run_image]
            self.running_tick = 0

        # Rotate the character image
        if angle is not None:
            self.image = pygame.transform.rotate(self.original_image, angle)


all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
character = Runner()
bus = Bus()
all_sprites.add(character)
all_sprites.add(bus)
enemy_sprites.add(bus)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.sprite.spritecollide(character, enemy_sprites, False):
        print("Game over!")
        running = False

    screen.blit(background, (0, 0))

    all_sprites.update()

    all_sprites.draw(screen)
    pygame.display.flip()

    pygame.time.Clock().tick(30)

pygame.quit()
