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
        p_saut1 = plateforme(800, 500, screen, 100, 10, "plat")
        p_saut2 = plateforme(1050, 450, screen, 100, 10, "plat")
        p_saut3 = plateforme(800, 300, screen, 100, 10, "plat")
        p_saut4 = plateforme(1300, 250, screen, 100, 500, "plat")
        # parcours
        p_saut5 = plateforme(2100, 500, screen, 100, 10, "plat")
        p_saut6 = plateforme(2450, 420, screen, 80, 10, "plat")
        p_saut7 = plateforme(2800, 360, screen, 60, 10, "plat")
        p_saut8 = plateforme(3150, 280, screen, 40, 10, "plat")
        # fin parcours jour

        #-----------nuit---------------#
        p_saut9 = plateforme(4300, 500, screen, 100, 10, "plat")
        p_saut10 = plateforme(4650, 420, screen, 80, 10, "plat")
        p_saut11 = plateforme(5000, 360, screen, 60, 10, "plat")
        p_saut12 = plateforme(5350, 280, screen, 40, 10, "plat")
        p_saut13 = plateforme(5700, 280, screen, 20, 10, "plat")
        p_saut14 = plateforme(6030, 280, screen, 20, 10, "plat")
        p_saut15 = plateforme(6330, 280, screen, 10, 10, "plat")


        p_porte = plateforme(4000, 0, screen, 100,768, "porte")

        plateformes.append(sol)
        plateformes.append(p_saut1)
        plateformes.append(p_saut2)
        plateformes.append(p_saut3)
        plateformes.append(p_saut4)
        plateformes.append(p_saut5)
        plateformes.append(p_saut6)
        plateformes.append(p_saut7)
        plateformes.append(p_saut8)
        plateformes.append(p_saut9)
        plateformes.append(p_saut10)
        plateformes.append(p_saut11)
        plateformes.append(p_saut12)
        plateformes.append(p_saut13)
        plateformes.append(p_saut14)
        plateformes.append(p_saut15)

        plateformes.append(p_porte)

        # Fruits du niveau:
        f1 = fruit(840, 250, screen)
        f2 = fruit(3155, 230, screen)
        f3 = fruit(3155, 500, screen)

        fruits.append(f1)
        fruits.append(f2)
        fruits.append(f3)

        # Enemis:
        e1 = ennemi(1, 800, 650, screen, 799, 1200, 3, 350, 350, 3)
        e2 = ennemi(2, 7500, 300, screen, 7500, 7500, 4, 50, 680, 4)
        e3 = ennemi(2, 7000, 300, screen, 7000, 7000, 4, 50, 680, 4)
        e4 = ennemi(2, 7250, 300, screen, 7250, 7250, 4, 50, 680, 4)


        ennemis.append(e1)
        ennemis.append(e2)
        ennemis.append(e3)
        ennemis.append(e4)

        # Piques ( A changer)
        obstacle1 = obstacles(350, 690, screen)
        obstacle2 = obstacles(350, 640, screen)
        obstacle3 = obstacles(350, 368, screen)
        obstacle4 = obstacles(350, 318, screen)
        #debut triangle
        obstacle5 = obstacles(1400, 240, screen)
        obstacle6 = obstacles(1450, 290, screen)
        obstacle7 = obstacles(1500, 340, screen)
        obstacle8 = obstacles(1550, 390, screen)
        obstacle9 = obstacles(1600, 440, screen)
        obstacle10 = obstacles(1650, 590, screen)

        #fin triangle

        obstacle11 = obstacles(3150, 690, screen)
        obstacle12 = obstacles(3150, 640, screen)
        obstacle13 = obstacles(3150, 368, screen)
        obstacle14 = obstacles(3150, 318, screen)

        # debut
        obs.append(obstacle1)
        obs.append(obstacle2)
        obs.append(obstacle3)
        obs.append(obstacle4)

        # triangle
        obs.append(obstacle5)
        obs.append(obstacle6)
        obs.append(obstacle7)
        obs.append(obstacle8)
        obs.append(obstacle9)
        obs.append(obstacle10)

        # porte fin niveau jour
        obs.append(obstacle11)
        obs.append(obstacle12)
        obs.append(obstacle13)
        obs.append(obstacle14)


        #clé
        cle1 = cle(6330, 80, screen)

        #lit
        l1 = lit(3850, 690, screen)


        # Sortie
        sort = sortie(8000, 622, screen)

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
                    else:
                        joueur.mort = False
                        tuto = genTuto()
                        joueur = player(3, 600, screen, tuto)
pygame.quit()
