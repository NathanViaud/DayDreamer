import pygame

from player import *
from fond import *
from plateforme import *

class world():
    def __init__(self, fond, plateformes, fruits, ennemis, obstacles):
        self.plateformes = plateformes
        self.fond = fond
        self.fruits = fruits
        self.ennemis = ennemis
        self.obstacles = obstacles

    def deplacement(self, vitesse):
        vitesse = -vitesse
        self.fond.deplacement(vitesse)
        for plateforme in self.plateformes:
            plateforme.deplacement(vitesse)
        for fruit in self.fruits:
            fruit.deplacement(vitesse)
        for ennemi in self.ennemis:
            ennemi.deplacement(vitesse)
        for obstacle in self.obstacles:
            obstacle.deplacement(vitesse)


    def droite(self, vitesse):
        self.fond.droite(vitesse)
        for plateforme in self.plateformes:
            plateforme.droite(vitesse)
        for fruit in self.fruits:
            fruit.droite(vitesse)
        for ennemi in self.ennemis:
            ennemi.droite(vitesse)
        for obstacle in self.obstacles:
            obstacle.deplacement(vitesse)

    def gauche(self, vitesse):
        self.fond.gauche(vitesse)
        for plateforme in self.plateformes:
            plateforme.gauche(vitesse)
        for fruit in self.fruits:
            fruit.gauche(vitesse)
        for ennemi in self.ennemis:
            ennemi.gauche(vitesse)
        for obstacle in self.obstacles:
            obstacle.deplacement(vitesse)

    def update(self):
        self.fond.update()
        for plateforme in self.plateformes:
            plateforme.update()
        for fruit in self.fruits:
            fruit.update()
        for ennemi in self.ennemis:
            ennemi.update()
        for obstacle in self.obstacles:
            obstacle.update()

    def removeFruit(self, fruit):
        for f in self.fruits:
            if f == fruit:
                self.fruits.remove(fruit)
        self.update()
