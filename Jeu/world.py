import pygame

from player import *
from fond import *
from plateforme import *

class world():
    def __init__(self, fond, plateformes, fruits, ennemis):
        self.plateformes = plateformes
        self.fond = fond
        self.fruits = fruits
        self.ennemis = ennemis

    def deplacement(self, vitesse):
        vitesse = -vitesse
        self.fond.deplacement(vitesse)
        for plateforme in self.plateformes:
            plateforme.deplacement(vitesse)
        for fruit in self.fruits:
            fruit.deplacement(vitesse)
        for ennemi in self.ennemis:
            ennemi.deplacement(vitesse)


    def droite(self, vitesse):
        self.fond.droite(vitesse)
        for plateforme in self.plateformes:
            plateforme.droite(vitesse)
        for fruit in self.fruits:
            fruit.droite(vitesse)
        for ennemi in self.ennemis:
            ennemi.droite(vitesse)

    def gauche(self, vitesse):
        self.fond.gauche(vitesse)
        for plateforme in self.plateformes:
            plateforme.gauche(vitesse)
        for fruit in self.fruits:
            fruit.gauche(vitesse)
        for ennemi in self.ennemis:
            ennemi.gauche(vitesse)

    def update(self):
        self.fond.update()
        for plateforme in self.plateformes:
            plateforme.update()
        for fruit in self.fruits:
            fruit.update()
        for ennemi in self.ennemis:
            ennemi.update()

    def removeFruit(self, fruit):
        for f in self.fruits:
            if f == fruit:
                self.fruits.remove(fruit)
        self.update()
