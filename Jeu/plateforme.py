import pygame

class plateforme:
    def __init__(self, pos):
        self.dimension_x = 100
        self.dimension_y = 10
        self.img = pygame.image.load("sprites/plateforme/p1.png")
        self.pos_x, self.pos_y = pos
    def droite(self, vitesse):
        self.pos_x -=  vitesse

    def gauche(self, vitesse):
        self.pos_x +=  vitesse