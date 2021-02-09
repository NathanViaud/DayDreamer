import pygame

from player import *
from fond import *
from plateforme import *
from cle import *

class world():
    def __init__(self, fond, plateformes, fruits, ennemis, obstacles, cle, lit):
        self.plateformes = plateformes
        self.fond = fond
        self.fruits = fruits
        self.ennemis = ennemis
        self.obstacles = obstacles
        self.cle = cle
        self.lit = lit

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
        self.cle.deplacement(vitesse)
        self.lit.deplacement(vitesse)

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
        self.cle.update()
        self.lit.update()

    def removeFruit(self, fruit):
        for f in self.fruits:
            if f == fruit:
                self.fruits.remove(fruit)
        self.update()

    def removeCle(self):
        self.cle = 0
