import pygame


class Mario:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/mario.png")
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = .5

    def move_direction(self, direction):
        if direction == "right":
            self.x = self.x + self.delta
        if direction == "left":
            self.x = self.x - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def health_bar(self, health):
        if health == 100:
            self.health_image = pygame.image.load("images/health bar/full.png")
        elif health == 75:
            self.health_image = pygame.image.load("images/health bar/one_hit.png")
        elif health == 50:
            self.health_image = pygame.image.load("images/health bar/half.png")
        elif health == 25:
            self.health_image = pygame.image.load("images/health bar/three_hits.png")
        elif health == 0:
            self.health_image = pygame.image.load("images/health bar/zero.png")
