import pygame

class Kirby:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/Kirby.png")
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 1
        if self.x < 100:
            self.x = 100
        if self.x > 800:
            self.x = 800

    def move_direction(self, direction):
        if direction == "right":
            self.x = self.x + self.delta
        if direction == "left":
            self.x = self.x - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def ability(self, ability):
        if ability == "block":
            self.block = True

