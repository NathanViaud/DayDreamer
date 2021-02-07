import pygame
from random import randint

class Balle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

        self.vitesse = [randint(4,8), randint(-8,8)]

    def update(self):
        self.rect.x += self.vitesse[0]
        self.rect.y += self.vitesse[1]

    def rebond(self):
        self.vitesse[0] = -self.vitesse[0]
        self.vitesse[1] = randint(-8,8)