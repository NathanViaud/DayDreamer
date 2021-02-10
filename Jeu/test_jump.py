import pygame
import os

from joueurxD import joueurxD

from fond import *
from plateforme import *
from player import *
from world import *
from fruit import *
from ennemi import *
from obstacles import *
from lit import *
from sortie import *
from genLevel import *
pygame.init()




VITESSE_SAUT = 40
HAUTEUR_SAUT = 100

size = (1024,768)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("cours forest")

genLevel = genLevel(screen,0)
tuto = genLevel.loadLevel(0)
niveau1 = genLevel.loadLevel(1)


joue = True

enCourse = False

enSaut = False
mort = pygame.image.load("images/mort.png")
course = pygame.mixer.Sound("./son/course.wav")
saut = pygame.mixer.Sound("./son/saut.wav")

# World tutoriel:
tutorial = True

black = (0,0,0)
#texte a afficher
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

# Joueur:
joueur = player(3, 100, screen, tuto)

monde = True




niveaux = []
niveaux.append(tuto)
niveaux.append(niveau1)

while monde:
    for niveau in niveaux:
        while joue:
            pygame.time.wait(1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    joue = False
                    monde = False
            tuto.update()
            for ennemi in tuto.ennemis:
                ennemi.moveE()

            joueur.deplaceAnimation()
            joueur.update()
            if tutorial == True:
                screen.blit(bienvenu, (tuto.fond.pos_x+50,200))
                screen.blit(mouvement_tuto, (tuto.fond.pos_x+50, 300))
                screen.blit(saut, (tuto.fond.pos_x +1200,200))
                screen.blit(fruits_message, (tuto.fond.pos_x+2900, 500))
                screen.blit(lit_message, (tuto.fond.pos_x+3595,650))
                screen.blit(enemies_messsage, (tuto.fond.pos_x+4250, 200))
                screen.blit(cle_message, (tuto.fond.pos_x+5200,350))
                screen.blit(porte_message, (tuto.fond.pos_x+5700, 500))
            pygame.display.update()

            while joueur.mort and joue:
                screen.blit(mort, (0,0,1024,768))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        joue = False
                        monde = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            joue = False
                            monde = False
                        elif event.key == pygame.K_SPACE:
                            joueur.mort = False
                            tuto = genTuto()
                            joueur = player(3, 600, screen, tuto)
            if joueur.victoire == True:
                joue = False
                monde = False
            pygame.time.wait(1)
    print("fini")
pygame.quit()