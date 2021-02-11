import pygame

from Jeu.plateforme import *
from Jeu.fond import *
from Jeu.world import *

img = pygame.image.load("sprites/idle.png")
marche1 = pygame.image.load("sprites/marche1.png")
marche2 = pygame.image.load("sprites/marche2.png")
img_reverse = pygame.transform.flip(img, True, False)
marche1_reverse = pygame.transform.flip(marche1, True, False)
marche2_reverse = pygame.transform.flip(marche2, True, False)
jump = pygame.image.load("sprites/jump.png")
jump_reverse = pygame.transform.flip(jump, True, False)
black = (0,0,0)
white = (255,255,255)

lit_dodo = [pygame.image.load("sprites/items/anim_dodo1.png"), pygame.image.load("sprites/items/anim_dodo2.png"), pygame.image.load("sprites/items/anim_dodo3.png"), pygame.image.load("sprites/items/anim_dodo4.png"), pygame.image.load("sprites/items/anim_dodo5.png"), pygame.image.load("sprites/items/anim_dodo6.png")]

font = pygame.font.Font(None, 40)
bienvenu = font.render("Bienvenue dans DayDreaming !", True, black)
mouvement_tuto = font.render("Utilisez les fleches directionnelles pour bouger", True, black)
saut = font.render("Pour sauter utilisez la barre espace", True, black)
font = pygame.font.Font(None, 30)
fruits_message = font.render("Prenez les fruit pour augmenter votre score !", True, black)
lit_message = font.render("Utilisez la touche F pour dormir dans le lit", True, black)
cle_message = font.render("Prenez la clé pour ouvrir la porte", True, black)
porte_message = font.render("Utilisez la porte pour finir le Tutoriel", True, black)
font = pygame.font.Font(None, 40)
enemies_messsage = font.render("Attention aux ennemis ! ", True, black)

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
        self.images_r.append(img)

        self.images_l.append(marche1_reverse)
        self.images_l.append(img_reverse)
        self.images_l.append(marche2_reverse)
        self.images_l.append(img_reverse)

        self.direction = ""

        self.last_plateform = world.plateformes[0]

        self.mort = False

        self.dort = True

        self.fps = 0

        self.last_direction = ""

        self.cle = False
        self.victoire = False

        self.estTutoriel = False

        self.score = 0
        self.score_fruit = 50
        self.score_fin = 100

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
                if self.cle:
                    if plateforme.type == "porte":
                        self.world.removePorte(self)
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
                self.score += self.score_fruit
                

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

        if self.world.lit.rect.colliderect(self.rect.x, self.rect.y, self.width, self.height):
            if key[pygame.K_f]:
                self.endort()
                self.world.sleep()
                self.reveille()

        if self.world.sortie.rect.colliderect(self.rect.x, self.rect.y, self.width, self.height):
            if self.world.nuit == False:
                self.victoire = True
                self.score += self.score_fin
        else:
            self.victoire = False    
          
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
        #pygame.draw.rect(self.screen, (0, 0, 0), self.rect, 2)

  

    def deplaceAnimation(self):
        if self.jumped:
            if self.direction == "droite":
                self.image = jump
            elif self.direction == "gauche":
                self.image = jump_reverse
            else:
                if self.last_direction == "droite":
                    self.image = jump
                elif self.last_direction == "gauche":
                    self.image = jump_reverse
                else:
                    self.image = jump
        else:
            if self.index > 3:
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

    def endort(self):
        for i in range (0,6):
            self.world.update()
            self.image = lit_dodo[i]
            if self.estTutoriel:
                self.screen.blit(bienvenu, (self.world.fond.pos_x+50,200))
                self.screen.blit(mouvement_tuto, (self.world.fond.pos_x+50, 300))
                self.screen.blit(saut, (self.world.fond.pos_x +1200,200))
                self.screen.blit(fruits_message, (self.world.fond.pos_x+2900, 500))
                self.screen.blit(lit_message, (self.world.fond.pos_x+3595,650))
                self.screen.blit(enemies_messsage, (self.world.fond.pos_x+4250, 200))
                self.screen.blit(cle_message, (self.world.fond.pos_x+5200,350))
                self.screen.blit(porte_message, (self.world.fond.pos_x+5700, 500))
            self.screen.blit(self.image, (self.world.lit.rect.x, pygame.display.get_surface().get_height() - (pygame.display.get_surface().get_height() - self.world.lit.rect.y + (self.image.get_rect().height - self.world.lit.rect.height))))
            pygame.display.update()
            pygame.time.wait(500)
        fondu_noir = False
        fonduSurface = pygame.Surface(pygame.display.get_window_size())
        alph = 0

        fonduSurface.fill((0,0,0))
        fonduSurface.set_alpha(alph)
        while not fondu_noir:
            alph += 0.5
            fonduSurface.set_alpha(alph)
            self.world.update()
            if self.estTutoriel:
                self.screen.blit(bienvenu, (self.world.fond.pos_x+50,200))
                self.screen.blit(mouvement_tuto, (self.world.fond.pos_x+50, 300))
                self.screen.blit(saut, (self.world.fond.pos_x +1200,200))
                self.screen.blit(fruits_message, (self.world.fond.pos_x+2900, 500))
                self.screen.blit(lit_message, (self.world.fond.pos_x+3595,650))
                self.screen.blit(enemies_messsage, (self.world.fond.pos_x+4250, 200))
                self.screen.blit(cle_message, (self.world.fond.pos_x+5200,350))
                self.screen.blit(porte_message, (self.world.fond.pos_x+5700, 500))
            self.image = lit_dodo[5]
            self.screen.blit(self.image, (self.world.lit.rect.x, pygame.display.get_surface().get_height() - (pygame.display.get_surface().get_height() - self.world.lit.rect.y + (self.image.get_rect().height - self.world.lit.rect.height))))
            self.screen.blit(fonduSurface, (0,0))
            pygame.display.update()
            if alph >= 255:
                fondu_noir = True


    def reveille(self):
        fonduSurface = pygame.Surface(pygame.display.get_window_size())
        fonduSurface.fill((0,0,0))
        self.world.update()
        pygame.display.update()
        for alpha in range(0, 510):
            fonduSurface.set_alpha((510 - alpha)/2)
            self.world.update()
            self.screen.blit(self.screen, (0,0))
            self.image = img
            self.screen.blit(self.image, self.rect)
            if self.estTutoriel:
                self.screen.blit(bienvenu, (self.world.fond.pos_x+50,200))
                self.screen.blit(mouvement_tuto, (self.world.fond.pos_x+50, 300))
                self.screen.blit(saut, (self.world.fond.pos_x +1200,200))
                self.screen.blit(fruits_message, (self.world.fond.pos_x+2900, 500))
                self.screen.blit(lit_message, (self.world.fond.pos_x+3595,650))
                self.screen.blit(enemies_messsage, (self.world.fond.pos_x+4250, 200))
                self.screen.blit(cle_message, (self.world.fond.pos_x+5200,350))
                self.screen.blit(porte_message, (self.world.fond.pos_x+5700, 500))
            self.screen.blit(fonduSurface, (0,0))
            pygame.display.update()

