import pygame
import random

class fruit():
    #x,y : position
    def __init__(self, x, y, screen):
        num = random.randint(1,3)
        img = pygame.image.load(f"sprites/items/fruit{num}.png")
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen = screen
        self.nuit = False

    def deplacement(self, vitesse):
        self.rect.x += vitesse
        self.update()

    def update(self):
        self.screen.blit(self.img, self.rect)

    def sleep(self):
        self.nuit = not self.nuit
        if self.nuit == True:
            num = random.randint(1,3)
            img = pygame.image.load(f"sprites/items/leg{num}.png")  #fruit nuit
        else:
            num = random.randint(1,3)
            img = pygame.image.load(f"sprites/items/fruit{num}.png")  #fruit jour
        self.img = img
        self.update()