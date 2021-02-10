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

plateformes = []
fruits = []
ennemis = []
obs = []

def genTuto():
        from ennemi import ennemi
        plateformes.clear()
        fruits.clear()
        ennemis.clear()
        obs.clear()
        # Sol du terrain
        sol = plateforme(0, 750, screen, 8196, 18, "sol")
        p_saut1 = plateforme(1300, 600, screen, 100, 150, "plat")
        p_saut2 = plateforme(1400, 450, screen, 200, 1000, "plat")
        p_saut3 = plateforme(1820, 200, screen, 100, 10, "plat")
        p_saut4 = plateforme(2400,700, screen, 50, 50, "plat")
        p_saut5 = plateforme(2785,700, screen, 50, 50, "plat")
        p_saut6 = plateforme(1640, 600, screen, 100, 150, "plat")
        p_saut7 = plateforme(2578, 500, screen, 70, 10, "plat")
        p_sautfruit2 = plateforme(3200, 430, screen, 100, 10, "plat")
        p_sautfruit3 = plateforme(3400, 250, screen, 100, 10, "plat")
        p_sautfruit4 = plateforme(2790, 220, screen, 100, 10, "plat")
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
        plateformes.append(p_saut6)
        plateformes.append(p_saut7)
        plateformes.append(p_sautfruit2)
        plateformes.append(p_sautfruit3)
        plateformes.append(p_sautfruit4)
        plateformes.append(p_porte)
        # plateformes.append(p_cle1)
        # plateformes.append(p_cle2)
        # plateformes.append(p_cle3)
        # plateformes.append(p_cle4)

        # Fruits du niveau:
        f2 = fruit(3235, 380, screen)
        f3 = fruit(3435, 200, screen)
        f4 = fruit(1605, 700, screen)
        f5 = fruit(2600, 100, screen)
        f6 = fruit(2820, 180, screen)
        f7 = fruit(1850, 160, screen)
        fruits.append(f2)
        fruits.append(f3)
        fruits.append(f4)
        fruits.append(f5)
        fruits.append(f6)
        fruits.append(f7)
        # Enemis:
        e1 = ennemi(2, 4470, 500, screen, 4470, 4470, 1, 200, 650, 2)
        e2 = ennemi(2, 4670, 500, screen, 4570, 4570, 1, 200, 600, 3)
        e3 = ennemi(2, 4870, 500, screen, 4570, 4570, 1, 200, 600, 4)

        # e2 = ennemi(1, 4800, 350, screen, 4799, 5050, 2, 350, 350, 1)
        ennemis.append(e1)
        ennemis.append(e2)
        ennemis.append(e3)

        # Piques ( A changer)
        obstacle1 = obstacles(2460, 690, screen)
        obstacle2 = obstacles(2524, 690, screen)
        obstacle3 = obstacles(2588, 690, screen)
        obstacle4 = obstacles(1450, 400, screen)
        obstacle5 = obstacles(2652, 690, screen)
        obstacle6 = obstacles(2716, 690, screen)
        obs.append(obstacle1)
        obs.append(obstacle2)
        obs.append(obstacle3)
        obs.append(obstacle4)
        obs.append(obstacle5)
        obs.append(obstacle6)

        #clé
        cle1 = cle(5280, 700, screen)

        #lit
        l1 = lit(3800, 700, screen)

        # Sortie
        sort = sortie(5750, 622, screen)

        fond.reset()

        return world(fond, plateformes, fruits, ennemis, obs, cle1, l1, sort)

VITESSE_SAUT = 40
HAUTEUR_SAUT = 100

size = (1024,768)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("cours forest")

joue = True

enCourse = False

enSaut = False
mort = pygame.image.load("images/mort.png")
course = pygame.mixer.Sound("./son/course.wav")
saut = pygame.mixer.Sound("./son/saut.wav")
fond = fond(screen, 8196)

#p_saut1 = plateforme(450, 450, screen)
#p_saut2 = plateforme(750, 550, screen)

# plateformes = []
#
# plateformes.append(p_saut1)
# plateformes.append(p_saut2)
#
# f1 = fruit(800, 740, screen)
# f2 = fruit(1700, 740, screen)
# fruits = [f1, f2]
#
# e1 = ennemi(1, 700, 678, screen, 300, 900, 1)
# e2 = ennemi(2, 1500, 350, screen, 1000, 1900, 1)
#
# ennemis =  [e1, e2]
# world = world(fond, plateformes, fruits, ennemis)
#
# joueur = player(3, 600, screen, world)


# World tutoriel:
tutorial = True

white = (255,255,255)
#texte a afficher
font = pygame.font.Font(None, 50)
mouvement_tuto = font.render("Utilisez les fleches directionnelles pour bouger", True, white)
saut = font.render("Pour sauter utilisez la barre espace", True, white)
fruits_message = font.render("Prenez les fruit pour augmenter votre score !", True, white)


tuto = genTuto()
# Joueur:
joueur = player(3, 600, screen, tuto)

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
            screen.blit(mouvement_tuto, (fond.pos_x+50, 200))
            screen.blit(saut, (fond.pos_x +1200,200))
            screen.blit(fruits_message, (fond.pos_x+2500, 200))
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
pygame.quit()
