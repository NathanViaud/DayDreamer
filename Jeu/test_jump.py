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

pygame.init()


def genTuto():
    from fond import fond
    from ennemi import ennemi
    fond = fond(screen, 6250)
    # Sol du terrain
    plateformes = []
    sol = plateforme(0, 750, screen, 8196, 18, "sol")
    p_saut1 = plateforme(1300, 600, screen, 100, 10, "plat")
    p_saut2 = plateforme(1600, 450, screen, 100, 10, "plat")
    p_saut3 = plateforme(1900, 600, screen, 100, 10, "plat")
    p_saut4 = plateforme(2400,700, screen, 50, 50, "plat")
    p_saut5 = plateforme(2662,700, screen, 50, 50, "plat")
    p_sautfruit1 = plateforme(3000, 600, screen, 100, 10, "plat")
    p_sautfruit2 = plateforme(3200, 450, screen, 100, 10, "plat")
    p_sautfruit3 = plateforme(3400, 250, screen, 100, 10, "plat")
    p_porte = plateforme(4000, 0, screen, 100,768, "porte")
    p_cle1 = plateforme(4250, 600, screen, 100, 10, "plat")
    p_cle2 = plateforme(4600, 450, screen, 100, 10, "plat")
    p_cle3 = plateforme(4800, 450, screen, 300, 10, "plat")
    p_cle4 = plateforme(5250,450, screen, 100, 10, "plat")
    plateformes.append(sol)
    plateformes.append(p_saut1)
    plateformes.append(p_saut2)
    plateformes.append(p_saut3)
    plateformes.append(p_saut4)
    plateformes.append(p_saut5)
    plateformes.append(p_sautfruit1)
    plateformes.append(p_sautfruit2)
    plateformes.append(p_sautfruit3)
    plateformes.append(p_porte)
    plateformes.append(p_cle1)
    plateformes.append(p_cle2)
    plateformes.append(p_cle3)
    plateformes.append(p_cle4)

    # Fruits du niveau:
    fruits = []
    f1 = fruit(3035, 555, screen)
    f2 = fruit(3235, 400, screen)
    f3 = fruit(3435, 200, screen)
    fruits.append(f1)
    fruits.append(f2)
    fruits.append(f3)

    # Enemis:
    e1 = ennemi(2, 4470, 500, screen, 4470, 4470, 1, 300, 650, 2)
    e2 = ennemi(1, 4800, 350, screen, 4799, 5050, 2, 350, 350, 1)
    ennemis = []
    ennemis.append(e1)
    ennemis.append(e2)

    # Piques ( A changer)
    obstacle1 = obstacles(2460, 690, screen)
    obstacle2 = obstacles(2524, 690, screen)
    obstacle3 = obstacles(2588, 690, screen)
    obs = []
    obs.append(obstacle1)
    obs.append(obstacle2)
    obs.append(obstacle3)

    #clé
    cle1 = cle(5280, 400, screen)

    #lit
    l1 = lit(3800, 735, screen)

    # Sortie
    sort = sortie(5750, 622, screen)

    fond.reset()

    return world(fond, plateformes, fruits, ennemis, obs, cle1, l1, sort)

VITESSE_SAUT = 40
HAUTEUR_SAUT = 100

size = (1024,768)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("cours forest")

tuto = genTuto()

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
bienvenu = font.render("Bienvenue a DayDreaming !", True, black)
mouvement_tuto = font.render("Utilisez les fleches directionnelles pour bouger", True, black)
saut = font.render("Pour sauter utilisez la barre espace", True, black)
font = pygame.font.Font(None, 30)
fruits_message = font.render("Prenez les fruit pour augmenter votre score !", True, black)
lit_message = font.render("Utilizes la touche F pour dormir dans le lit", True, black)
cle_message = font.render("Prenez la clé pour ouvrir la porte", True, black)
porte_message = font.render("Utilisez la porte pour finir le Tutoriel", True, black)
font = pygame.font.Font(None, 40)
enemies_messsage = font.render("Attention aux enemies ! ", True, black)

# Joueur:
joueur = player(3, 100, screen, tuto)

monde = True

while monde:

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
        pygame.time.wait(1)
pygame.quit()