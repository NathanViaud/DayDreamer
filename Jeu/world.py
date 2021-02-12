import pygame

from Jeu.player import *
from Jeu.fond import *
from Jeu.plateforme import *
from Jeu.cle import *

black = (0,0,0)
white = (255,255,255)

font = pygame.font.Font(None, 40)
bienvenu = font.render("Bienvenue dans DayDreaming !", True, black)
mouvement_tuto = font.render("Utilisez les fleches directionnelles pour bouger", True, black)
saut = font.render("Pour sauter utilisez la barre espace", True, black)
font = pygame.font.Font(None, 30)
fruits_message = font.render("Prenez les fruit pour augmenter votre score !", True, black)
lit_message = font.render("Utilisez la touche F pour dormir dans le lit", True, black)
cle_message = font.render("Prenez la cle pour ouvrir la porte", True, black)
porte_message = font.render("Utilisez la porte pour finir le Tutoriel", True, black)
font = pygame.font.Font(None, 40)
enemies_messsage = font.render("Attention aux ennemis ! ", True, black)

class world():
    def __init__(self, fond, plateformes, fruits, ennemis, obstacles, cle, lit, sortie):
        self.fond = fond
        self.plateformes = plateformes
        self.fond = fond
        self.fruits = fruits
        self.ennemis = ennemis
        self.obstacles = obstacles
        self.cle = cle
        self.lit = lit
        self.sortie = sortie
        self.nuit = False

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
        self.sortie.deplacement(vitesse)
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
        self.sortie.update()

    def removeFruit(self, fruit):
        for f in self.fruits:
            if f == fruit:
                self.fruits.remove(fruit)
        self.update()

    def sleep(self):
        self.nuit = not self.nuit
        self.fond.sleep()
        for fruit in self.fruits:
           fruit.sleep()
        for plateforme in self.plateformes:
            plateforme.sleep()
        self.cle.sleep()

    def removePorte(self, player):
        for plateforme in self.plateformes:
            if plateforme.type == "porte":
                for i in range(0,pygame.display.get_surface().get_height()):
                        plateforme.rect.y += 1
                        self.update()
                        player.screen.blit(player.image, player.rect)
                        if player.estTutoriel:
                            player.screen.blit(bienvenu, (self.fond.pos_x+50,200))
                            player.screen.blit(mouvement_tuto, (self.fond.pos_x+50, 300))
                            player.screen.blit(saut, (self.fond.pos_x +1200,200))
                            player.screen.blit(fruits_message, (self.fond.pos_x+2900, 500))
                            player.screen.blit(lit_message, (self.fond.pos_x+3595,650))
                            player.screen.blit(enemies_messsage, (self.fond.pos_x+4250, 200))
                            player.screen.blit(cle_message, (self.fond.pos_x+5200,350))
                            player.screen.blit(porte_message, (self.fond.pos_x+5700, 500))
                        pygame.display.update()
                        pygame.time.wait(1)

    def getPorte(self):
        for plateforme in self.plateformes:
            if plateforme.type == "Porte":
                return plateforme