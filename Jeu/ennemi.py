import pygame

class ennemi():
    def __init__(self, x, y, screen , deb, fin, vitesse):
        img = pygame.image.load("sprites/ennemis/e1.png")
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen = screen
        self.deb = deb
        self.fin = fin
        self.vitesse = vitesse

    def update(self):
        self.screen.blit(self.img, self.rect)

    def droite(self, vitesse):
        self.rect.x -= vitesse
        self.deb -= vitesse
        self.fin -= vitesse
        self.update()
    
    def gauche(self, vitesse):
        self.rect.x += vitesse
        self.deb += vitesse
        self.fin += vitesse
        self.update()

    def moveE(self):
        if self.rect.x >= self.fin or self.rect.x <= self.deb:
            self.vitesse = -self.vitesse
        self.rect.x += self.vitesse
        self.update()
            