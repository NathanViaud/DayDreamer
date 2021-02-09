import pygame

class fond:
    def __init__(self, img, screen, taille):
        self.img = img
        self.pos_x= 0
        self.screen = screen
        self.taille = taille


    def update(self):
        self.screen.blit(self.img, (self.pos_x, 0))

    def deplacement(self, vitesse):
        self.pos_x += vitesse
        self.update()

    def droite(self, vitesse):
        self.pos_x -=  vitesse
        self.update()

    def gauche(self, vitesse):
        self.pos_x +=  vitesse
        self.update()