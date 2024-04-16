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

class Student(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/MainCharacterRightSide.png")
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

all_sprites = pygame.sprite.Group()
character = Student()
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