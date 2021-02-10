import pygame

from plateforme import *
from fond import *
from world import *

img = pygame.image.load("sprites/idle.png")
marche1 = pygame.image.load("sprites/marche1.png")
marche2 = pygame.image.load("sprites/marche2.png")
img_reverse = pygame.transform.flip(img, True, False)
marche1_reverse = pygame.transform.flip(marche1, True, False)
marche2_reverse = pygame.transform.flip(marche2, True, False)
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

        self.images_r.append(marche1)
        self.images_r.append(img)
        self.images_r.append(marche2)

        self.images_l.append(marche1_reverse)
        self.images_l.append(img_reverse)
        self.images_l.append(marche2_reverse)

        self.direction = ""

        self.last_plateform = world.plateformes[0]

        self.mort = False

        self.dort = True

        self.fps = 0

        self.last_direction = ""

        self.cle = False

    def sleep(self):
        self.dort = not self.dort

    def update(self):
        w, h = pygame.display.get_surface().get_size()
        vx = 0
        dy = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False:
            self.vel_y = -6.75
            self.jumped = True
        if key[pygame.K_LEFT]:
            self.direction = "gauche"
            self.index += 1
            vx -= 2
            self.fps += 1
        if key[pygame.K_RIGHT]:
            self.direction = "droite"
            self.index += 1
            vx += 2
            self.fps += 1
        if not key[pygame.K_RIGHT] and not key[pygame.K_LEFT]:
            self.fps = 0
            if self.direction != "":
                self.last_direction = self.direction
            self.direction = ""

        self.vel_y += 0.1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        for plateforme in self.world.plateformes:
            if plateforme.rect.colliderect(self.rect.x+vx, self.rect.y, self.width, self.height):
                vx =0
                if plateforme.type == "porte":
                    if self.cle == True:
                        print("ouvrir porte")
                        plateforme.removePorte()
            if plateforme.rect.colliderect(self.rect.x, self.rect.y+dy, self.width, self.height):
                self.last_plateform = plateforme
                if self.vel_y < 0:
                    dy = plateforme.rect.bottom - self.rect.top
                    self.vel_y = 0
                elif self.vel_y > 0:
                    dy = plateforme.rect.top - self.rect.bottom
                    self.vel_y = 0
                if self.rect.bottom == plateforme.rect.top:
                    self.jumped = False
            if self.rect.bottom != self.last_plateform.rect.top:
                    self.jumped = True
                
        for fruit in self.world.fruits:
            if fruit.rect.colliderect(self.rect.x, self.rect.y, self.width, self.height):
                self.world.removeFruit(fruit)

        for ennemi in self.world.ennemis:
            if ennemi.rect.colliderect(self.rect.x, self.rect.y, self.width, self.height):
                self.mort = True

        for obstacle in self.world.obstacles:
            if obstacle.rect.colliderect(self.rect.x, self.rect.y, self.width, self.height):
                self.mort = True

        if self.world.cle.rect.colliderect(self.rect.x, self.rect.y, self.width, self.height):
            if self.world.nuit == True:
                self.world.cle.prendreCle()
                self.cle = True
                print(self.cle)

        if self.world.lit.rect.colliderect(self.rect.x, self.rect.y, self.width, self.height):
            if key[pygame.K_f]:
                pygame.time.wait(1500)
                self.world.sleep()

        if self.world.sortie.rect.colliderect(self.rect.x, self.rect.y, self.width, self.height):
            if self.world.nuit == False:
                print("gagné")
            
          
        if self.direction == "droite":
            if self.world.fond.pos_x <= -self.world.fond.taille + w:
                if self.rect.x <= w -30:
                    self.rect.x += vx
            elif self.rect.x <= w/2 -15:
                self.rect.x += vx
            else:
                self.world.deplacement(vx)
        elif self.direction == "gauche":
            if self.rect.x >= w/2:
                self.rect.x += vx
            elif self.world.fond.pos_x >= 0:
                if self.rect.x >= 0: 
                    self.rect.x += vx
            else:
                self.world.deplacement(vx)
        self.rect.y += dy
        if self.rect.bottom > 750:
            self.rect.bottom = 750
            dy = 550
            self.jumped = False
        self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect, 2)

  

    def deplaceAnimation(self):
        if self.index > 2:
            self.index = 0
        if self.fps % 30 == 0:
            if self.direction == "gauche":
                self.image = self.images_l[self.index]
            elif self.direction == "droite":
                self.image = self.images_r[self.index]
            else:
                if self.last_direction == "gauche":
                    self.image = img_reverse
                else:
                    self.image = img
        if self.fps > 30:
            self.fps = 0
        self.screen.blit(self.image, self.rect)