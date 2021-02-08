import pygame

pygame.init()

immobile = pygame.image.load("./sprites/idle.png")
marchedroite1 = pygame.image.load("./sprites/gauche1.png")
marchedroite2 = pygame.image.load("./sprites/gauche2.png")
marchegauche1 = pygame.image.load("./sprites/droite1.png")
marchegauche2 = pygame.image.load("./sprites/droite2.png")
marchedroite = [ marchedroite1, marchedroite2]
marchegauche = [marchegauche1, marchegauche2]

commandes = pygame.key.get_pressed()

class joueurxD(pygame.sprite.Group):

    def __init__(self, pos_x, pos_y, screen):
        super().__init__()
        self.image = immobile
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pose = 0
        self.enSaut = False
        self.jumpCount = 27
        self.screen = screen

    def deplace(self, vitesse):
        fond_a_decal = True
        if vitesse > 0:
            if self.pos_x <= 420:
                self.pos_x += vitesse
                fond_a_decal = False
            self.image = marchedroite[self.pose]
            self.pose += 1
            if(self.pose >= 2):
                self.pose = 0
        elif vitesse < 0:
            if self.pos_x >= 420:
                self.pos_x += vitesse
                fond_a_decal = False
            self.image = marchegauche[self.pose]
            self.pose += 1
            if(self.pose >= 2):
                self.pose = 0
        else:
            self.image = immobile

        return fond_a_decal

    def immobile(self, vitesse):
        if vitesse == 0:
            self.image = immobile
            self.pose = 0 

    def saut(self):
        if self.enSaut:
            if self.jumpCount >= -27:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.pos_y -= self.jumpCount**2*0.1*neg
                self.jumpCount -= 3
            else:
                self.enSaut = False
                self.jumpCount = 27
    
    def draw(self):
        self.screen.blit(self.image, (self.pos_x, self.pos_y))