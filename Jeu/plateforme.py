import pygame

class plateforme():
    def __init__(self, pos):
        self.dimension_x = 100
        self.dimension_y = 10
        self.pos_x, self.pos_y = pos
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.dimension_x, self.dimension_y)
    def droite(self, vitesse):
        self.rect.x -=  vitesse

    def gauche(self, vitesse):
        self.rect.x +=  vitesse