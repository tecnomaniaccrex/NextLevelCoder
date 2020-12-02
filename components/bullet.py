import pygame
from UTILS.constants import (
    RED,
    SCREEN_HEIGHT,
    SCREEN_WIDTH

)
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -5


    def update(self):
        self.rect.y += self.speedy


        if self.rect.bottom < 0:
            self.kill()