import pygame

immobile = pygame.image.load("./sprites/idle.png")
marchedroite1 = pygame.image.load("./sprites/gauche1.png")
marchedroite2 = pygame.image.load("./sprites/gauche2.png")
marchegauche1 = pygame.image.load("./sprites/droite1.png")
marchegauche2 = pygame.image.load("./sprites/droite2.png")
marchedroite = [ marchedroite1, marchedroite2]
marchegauche = [marchegauche1, marchegauche2]


class joueurxD(pygame.sprite.Group):

    def __init__(self, joueur, pos_x, pos_y):
        super().__init__()
        self.image = immobile
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pose = 0

    def deplaceGauche(self):
        self.pos_x -= 5
        self.image = marchegauche[self.pose]
        self.pose += 1
        if(self.pose >= 2):
            self.pose = 0

    def deplaceDroite(self):
        self.pos_x += 5
        self.image = marchedroite[self.pose]
        self.pose += 1
        if(self.pose >= 2):
            self.pose = 0