import pygame as pg

class Luzha:
    def __init__(self, x, y):
        self.image = pg.image.load("images/circlewater.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.radius = self.rect.width // 2  # Calculate radius of circle
        self.hitbox_radius = self.radius - 5  # Adjust for a slightly smaller hitbox

        # Adjust hitbox position
        self.hitbox_offset_x = -30
        self.hitbox_offset_y = -30

    def move(self):
        pass

    def draw(self, win, camera):
        win.blit(self.image, (self.rect.x - camera.rect.x, self.rect.y - camera.rect.y))

    def get_hitbox(self):
        # Returns the circular hitbox of the object
        return pg.Rect(self.rect.centerx - self.hitbox_radius + self.hitbox_offset_x, 
                       self.rect.centery - self.hitbox_radius + self.hitbox_offset_y,
                       self.hitbox_radius * 2, self.hitbox_radius * 2)
