import pygame

burger = [pygame.image.load("sprites/ennemis/burger_bas.png"), pygame.image.load("sprites/ennemis/burger_mid.png"), pygame.image.load("sprites/ennemis/burger_haut.png"), pygame.image.load("sprites/ennemis/burger_mid.png")]

class ennemi():
    #type : 1 = au sol 2 = volant
    #x,y : position de base du perso
    #screen : ecran actuel
    #xd,xf : position x de debut, position x de fin (egale si pas de deplacement en x) | xd < xf
    #vitesse : vitesse en x
    #yd, yf : position en y de debut, position en y de fin (egale si pas de deplacement en y)  | yd < yf
    #vitesse_y : vitesse en y
    def __init__(self, type, x, y, screen , xd, xf, vitesse, yd, yf, vitesse_y):
        self.type = type
        self.img = burger[0]
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen = screen
        self.xd = xd
        self.xf = xf
        self.vitesse = vitesse
        self.yd = yd
        self.yf = yf
        self.vitesse_y = vitesse_y
        self.frame = 0
        self.fps = 30


    def update(self):
        self.animation()
        self.screen.blit(self.img, self.rect)

    def deplacement(self, vitesse):
        self.rect.x += vitesse
        self.xd += vitesse
        self.xf += vitesse
        self.update()

    def moveE(self):
        if self.xd != self.xf:
            if self.rect.x >= self.xf or self.rect.x <= self.xd:
                self.vitesse = -self.vitesse
            self.rect.x += self.vitesse
        if self.yf != self.yd:
            if self.rect.y >= self.yf or self.rect.y <= self.yd:
                self.vitesse_y = -self.vitesse_y
            self.rect.y += self.vitesse_y
        self.update()
        print(self.frame)

    def animation(self):
        if self.frame > 3:
            self.frame = 0
        if self.fps % 30 == 0:
            self.img = burger[self.frame]
            self.frame += 1
        if self.fps > 30:
            self.fps = 0
        self.fps += 1