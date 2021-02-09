import pygame

from plateforme import *
from fond import *
from world import *

img = pygame.image.load("sprites/idle.png")
class player():
    def __init__(self, x ,y, screen, world):
        self.screen = screen
        self.world = world
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.fond = fond

        self.images_r = []
        self.images_l = []
        self.index = 0

        self.images_l.append(img)
        self.images_l.append(pygame.image.load("sprites/droite1.png"))
        self.images_l.append(img)
        self.images_l.append(pygame.image.load("sprites/droite2.png"))

        self.images_r.append(img)
        self.images_r.append(pygame.image.load("sprites/gauche1.png"))
        self.images_r.append(img)
        self.images_r.append(pygame.image.load("sprites/gauche2.png"))

        self.direction = ""

    def update(self):
        
        w, h = pygame.display.get_surface().get_size()
        vx = 0
        dy = 0
        d1x = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False:
            self.vel_y = -10
            self.jumped = True
        if key[pygame.K_LEFT]:
            self.direction = "gauche"
            self.index += 1
            vx -= 2
        if key[pygame.K_RIGHT]:
            self.direction = "droite"
            self.index += 1
            vx += 2

        self.vel_y += 0.1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        for plateforme in self.world.plateformes:
            if plateforme.rect.colliderect(self.rect.x+vx, self.rect.y, self.width, self.height):
                vx =0
            if plateforme.rect.colliderect(self.rect.x, self.rect.y+dy, self.width, self.height):
                if self.vel_y < 0:
                    dy = plateforme.rect.bottom - self.rect.top
                    self.vel_y = 0
                elif self.vel_y > 0:
                    dy = plateforme.rect.top - self.rect.bottom
                    self.vel_y = 0
                self.jumped = False
                
        for fruit in self.world.fruits:
            if fruit.rect.colliderect(self.rect.x, self.rect.y, self.width, self.height):
                self.world.removeFruit(fruit)

        for ennemi in self.world.ennemis:
            if ennemi.rect.colliderect(self.rect.x, self.rect.y, self.width, self.height):
                print("touché")
                
        if self.rect.x > w/2 and self.direction == "droite" or self.rect.x < w/2 and self.direction == "gauche" :
            self.world.deplacement(vx)
        else:
            self.rect.x += vx
        self.rect.y += dy

        if self.rect.bottom > self.screen.get_height():
            self.rect.bottom = self.screen.get_height()
            dy = 550
            self.jumped = False

        self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect, 2)


    def deplaceAnimation(self):
        if self.index > 3:
            self.index = 0
        if self.direction == "gauche":
            self.image = self.images_l[self.index]
        elif self.direction == "droite":
            self.image = self.images_r[self.index]
        else:
            self.image = img
        self.screen.blit(self.image, self.rect)