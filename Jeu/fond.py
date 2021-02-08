import pygame

class fond:
    def __init__(self, img):
        self.img = img
        self.pos_x= 0

    def droite(self, vitesse):
        self.pos_x +=  vitesse

    def gauche(self, vitesse):
        self.pos_x +=  vitesse