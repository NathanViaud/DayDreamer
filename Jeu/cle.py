import pygame

class cle():
    def __init__(self, x , y, screen) :
        img = pygame.image.load("sprites/items/cle.png")
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen = screen
        self.prise = False

    def deplacement(self, vitesse):
        self.rect.x += vitesse
        self.update()

    def update(self):
        self.screen.blit(self.img, self.rect)

    def prendreCle(self):
        self.prise= True
        transparent = (0, 0, 0, 0)
        self.img.fill(transparent)

