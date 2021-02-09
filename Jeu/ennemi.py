import pygame

class ennemi():
    def __init__(self, x, y, screen):
        img = pygame.image.load("sprites/ennemis/e1.png")
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen = screen

    def update(self):
        self.screen.blit(self.img, self.rect)

    def droite(self, vitesse):
        self.rect.x -= vitesse
        self.update()
    
    def gauche(self, vitesse):
        self.rect.x += vitesse
        self.update()

    def moveE(self, vitesse, deb, fin):
        if self.rect.x > fin or self.rect.x < deb:
            vitesse = - vitesse
        self.rect.x += vitesse
        self.update()
            