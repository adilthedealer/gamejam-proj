import pygame as pg

class Camera:
    def __init__(self, x, y, bg_width, bg_height, player_rect):
        self.rect = pg.Rect(x, y, 500, 500)
        self.bg_width = bg_width
        self.bg_height = bg_height
        self.player_rect = player_rect

    def move(self, vector):
        # Calculate the new position of the camera
        new_x = self.rect[0] + vector[0]
        new_y = self.rect[1] + vector[1]

        # Check the boundaries to ensure the camera stays within the background's size
        if new_x < 0:
            new_x = 0
        elif new_x > self.bg_width - self.rect.width:
            new_x = self.bg_width - self.rect.width

        if new_y < 0:
            new_y = 0
        elif new_y > self.bg_height - self.rect.height:
            new_y = self.bg_height - self.rect.height

        # Calculate the offset of the camera movement
        offset_x = new_x - self.rect.x
        offset_y = new_y - self.rect.y

        # Update the camera's position
        self.rect.topleft = (new_x, new_y)

        # Adjust player's position to keep it centered
        self.player_rect.move_ip(offset_x, offset_y)
