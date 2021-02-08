import pygame

class fond:
    def __init__(self, img):
        self.img = img
        self.pos_x= 0

    def Droite(self, vitesse):
        self.pos_x +=  vitesse

    def Gauche(self, vitesse):
        self.pos_x +=  vitesse