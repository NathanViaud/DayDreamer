import pygame
from pygame import locals as const


class raquette:
    def __init__(self, nbJoueur, pos_y, vitesse):
        self.nbJoueur = nbJoueur
        self.pos_y = pos_y
        self.vitesse = vitesse
        if nbJoueur == 1:
            self.img = pygame.image.load("images/raquette1.png")
            self.pos_x = 0
        elif nbJoueur == 2:
            self.img = pygame.image.load("images/raquette2.png")
            self.pos_x = 630
    def mouvR(self):
        self.pos_y += self.vitesse
    def setVitesse(self, vitesse):
        self.vitesse = vitesse
    def stop(self):
        self.vitesse = 0
    def reset(self, pos):
        self.pos_y = pos
