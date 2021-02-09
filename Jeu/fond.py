import pygame

class fond:
    def __init__(self, img, screen):
        self.img = img
        self.pos_x= 0
        self.screen = screen

    def update(self):
        self.screen.blit(self.img, (self.pos_x, 0))

    def droite(self, vitesse):
        self.pos_x -=  vitesse
        self.update()

    def gauche(self, vitesse):
        self.pos_x +=  vitesse
        self.update()