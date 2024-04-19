import pygame as pg
import random

class NPC:
    def __init__(self):
        try:
            # Forward movement (movement to the top)
            self.fix1 = pg.transform.scale(pg.image.load("images/npcside/npc_side_stand.png").convert_alpha(), (35, 35))
            self.fix2 = pg.transform.scale(pg.image.load("images/npcside/npc_side1.png").convert_alpha(), (35, 35))
            self.fix = pg.transform.scale(pg.image.load("images/npcside/npc_side2.png").convert_alpha(), (35, 35))

            # Backward movement
            self.fixb1 = pg.transform.scale(pg.image.load("images/npcback/npc_back_stand.png").convert_alpha(), (35, 35))
            self.fixb2 = pg.transform.scale(pg.image.load("images/npcback/npc_back1.png").convert_alpha(), (35, 35))
            self.fixb = pg.transform.scale(pg.image.load("images/npcback/npc_back2.png").convert_alpha(), (35, 35))

            # Right movement
            self.fixr1 = pg.transform.scale(pg.image.load("images/npcside/npc_side_stand.png").convert_alpha(), (35, 35))
            self.fixr2 = pg.transform.scale(pg.image.load("images/npcside/npc_side1.png").convert_alpha(), (35, 35))
            self.fixr = pg.transform.scale(pg.image.load("images/npcside/npc_side2.png").convert_alpha(), (35, 35))
        except pg.error as e:
            print("Error loading images:", e)
            raise SystemExit

        self.run_images = [self.fix1, self.fix, self.fix2]
        self.run_images_back = [self.fixb1, self.fixb, self.fixb2]
        self.run_images_right = [self.fixr1, self.fixr, self.fixr2]
        self.run_images_left = [pg.transform.flip(self.fixr1, True, False), pg.transform.flip(self.fixr, True, False), pg.transform.flip(self.fixr2, True, False)]
        self.current_run_image = 0
        self.image = self.run_images[self.current_run_image]

        self.rect = self.image.get_rect().inflate(-50, -50)
        self.rect.center = (1600, 1800)  # Начальная позиция NPC

        # Рамки, в которых NPC может двигаться
        self.allowed_rects = [
            pg.Rect(1599, 1799, 103, 48),
            pg.Rect(1698, 1531, 86, 469),
            pg.Rect(863, 1452, 922, 79),
            pg.Rect(863, 888, 76, 568),
            pg.Rect(142, 886, 796, 80),
            pg.Rect(141, 419, 72, 467),
            pg.Rect(212, 419, 960, 67)
        ]

        self.speed = 2  # Скорость движения NPC

    def move(self):
        # Выбираем случайное направление для движения NPC
        direction = random.choice(["up", "down", "left", "right"])
        new_rect = self.rect.move(0, 0)  # Начальное значение нового прямоугольника

        # Проверяем, что новая позиция находится внутри разрешенных рамок
        while True:
            if direction == "up":
                new_rect.y -= self.speed
            elif direction == "down":
                new_rect.y += self.speed
            elif direction == "left":
                new_rect.x -= self.speed
            elif direction == "right":
                new_rect.x += self.speed

            if any(new_rect.colliderect(rect) for rect in self.allowed_rects):
                break

            # Если новая позиция выходит за пределы рамок, выбираем новое направление
            direction = random.choice(["up", "down", "left", "right"])

        # Обновляем позицию NPC
        self.rect = new_rect

    def update(self):
        self.current_run_image = (self.current_run_image + 1) % len(self.run_images)
        self.image = self.run_images[self.current_run_image]

    def draw(self, win, camera):
        win.blit(self.image, (self.rect.x - camera.rect.x, self.rect.y - camera.rect.y))
