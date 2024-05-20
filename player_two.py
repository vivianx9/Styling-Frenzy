import pygame


class PlayerTwo:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def health_bar(self, health):
        if health == 100:
            self.image = pygame.image.load("images/health bar/full.png")
        elif health == 75:
            self.image = pygame.image.load("images/health bar/one_hit.png")
        elif health == 50:
            self.image = pygame.image.load("images/health bar/half.png")
        elif health == 25:
            self.image = pygame.image.load("images/health bar/three_hits.png")
        elif health == 0:
            self.image = pygame.image.load("images/health bar/zero.png")
        self.image = pygame.transform.scale(self.image, (300, 140))