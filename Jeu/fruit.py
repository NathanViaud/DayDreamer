import pygame

class fruit():
    def __init__(self, x, y, screen):
        img = pygame.image.load("sprites/items/fruit.png")
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
            img = pygame.image.load("sprites/items/fruit.png")  #fruit nuit
        else:
            img = pygame.image.load("sprites/items/fruit.png")  #fruit jour
        self.img = img
        self.update()