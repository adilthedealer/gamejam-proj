import pygame
import random as rnd

class Lower_car:
    def __init__(self, x, y, color):
        self.image = pygame.image.load("images/cars/" + color + "_car.png")
        self.speed = rnd.randint(10, 14)
        self.rect = self.image.get_rect().inflate(-50, -50)
        self.rect.topleft = (x, y)
        self.stopped = False  # Added attribute to track if the car is stopped
        
    def move(self, traffic_light):
        # if traffic_light.current_light_index == 2:  # If the current light is red
        #     self.stopped = True  # Stop the car
        # else:
        #     self.stopped = False  # Otherwise, the car can move

        if not self.stopped:  # If the car is not stopped
            self.rect.x += self.speed
            if self.rect.left > 2000 or self.rect.right < 300:
                self.speed = -self.speed
                self.image = pygame.transform.flip(self.image, True, False)
        
    def draw(self, win, camera):
        win.blit(self.image, (self.rect.x - camera.rect.x, self.rect.y - camera.rect.y))
