import pygame

class PlayerOne:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def health_bar(self, health):
        if health == 100:
            self.image = pygame.image.load("images/health/full.png")
        elif health == 75:
            self.image = pygame.image.load("images/health/one_hit.png")
        elif health == 50:
            self.image = pygame.image.load("images/health/half.png")
        elif health == 25:
            self.image = pygame.image.load("images/health/three_hits.png")
        elif health == 0:
            self.image = pygame.image.load("images/health/zero.png")
        self.image = pygame.transform.scale(self.image, (300, 140))