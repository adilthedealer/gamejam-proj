import pygame as pg
from pygame.locals import *

class PopupWindow:
    def __init__(self, position):
        self.font = pg.font.Font("Pixel_font.ttf", 24)
        self.window_color = (0, 0, 0, 150)  
        self.text_color = (255, 255, 255)
        
        self.message = "Will you help me, an old lady, grandson?"
        self.options = ["Yes", "No"]
        
        self.window_rect = pg.Rect(position, (500, 150))
        
        self.message_surface = self.font.render(self.message, True, self.text_color)
        self.message_rect = self.message_surface.get_rect(center=(self.window_rect.centerx, self.window_rect.centery - 20))
        
        self.option_rects = []
        for i, option in enumerate(self.options):
            text_surface = self.font.render(option, True, self.text_color)
            text_rect = text_surface.get_rect()
            text_rect.center = (self.window_rect.centerx + (i - 0.5) * 200, self.window_rect.centery + 20)
            self.option_rects.append(text_rect)

    def draw(self, screen):
        pg.draw.rect(screen, self.window_color, self.window_rect)
        
        screen.blit(self.message_surface, self.message_rect)
        
        for option, rect in zip(self.options, self.option_rects):
            screen.blit(self.font.render(option, True, self.text_color), rect)

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            for i, rect in enumerate(self.option_rects):
                if rect.collidepoint(event.pos):
                    return self.options[i]
        return None
