import pygame

class lit():
    #x,y : position
    def __init__(self, x, y, screen) :
        img = pygame.image.load("sprites/items/lit.png")
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen = screen

    def deplacement(self, vitesse):
        self.rect.x += vitesse
        self.update()

    def update(self):
        self.screen.blit(self.img, self.rect)