import pygame

class Upper_car:
    def __init__(self, x, y, color):
        self.image = pygame.image.load("images/cars/" + color + "_car.png")
        self.speed = 8
        self.rect = self.image.get_rect().inflate(-50, -50)
        self.rect.topleft = (x, y)
        
    def move(self):
        self.rect.x += self.speed
        if self.rect.left > 1600 or self.rect.right < 0:
            self.speed = -self.speed
            self.image = pygame.transform.flip(self.image, True, False)
        
    def draw(self, win, camera):
        win.blit(self.image, (self.rect.x - camera.rect.x, self.rect.y - camera.rect.y))
