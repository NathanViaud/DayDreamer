import pygame

class fond:
    # taille : taille en x du niveau
    def __init__(self, screen, taille):
        img = pygame.image.load("images/fond_j.jpg")
        self.img = img
        self.pos_x= 0
        self.screen = screen
        self.taille = taille
        self.nuit = False


    def update(self):
        self.screen.blit(self.img, (self.pos_x, 0))

    def deplacement(self, vitesse):
        self.pos_x += vitesse
        self.update()

    def reset(self):
        self.pos_x = 0

    def sleep(self):
        self.nuit = not self.nuit
        if self.nuit == True:
            img = pygame.image.load("images/fond.jpg")  #fond nuit
        else:
            img = pygame.image.load("images/fond_j.jpg")
        self.img = img
        self.update()