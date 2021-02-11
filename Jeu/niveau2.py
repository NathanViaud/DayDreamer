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
        p_saut2 = plateforme(650, 350, screen, 100, 10, "plat")
        p_saut3 = plateforme(800, 300, screen, 100, 10, "plat")
        p_saut4 = plateforme(950, 250, screen, 100, 10, "plat")
        p_saut5 = plateforme(1300, 280, screen, 100, 10, "plat")
        p_saut6 = plateforme(2300, 500, screen, 140, 10, "plat")
        p_saut7 = plateforme(2500, 200, screen, 100, 10, "plat")
        p_saut8 = plateforme(2600, 300, screen, 100, 10, "plat")
        p_saut9 = plateforme(3050, 450, screen, 100, 10, "plat")
        p_saut10 = plateforme(3200, 200, screen, 100, 10, "plat")
        p_saut11 = plateforme(3650, 500, screen, 100, 10, "plat")
        p_saut12 = plateforme(3850, 250, screen, 100, 10, "plat")
        ###################################
        p_saut13 = plateforme(5750, 575, screen, 100, 10, "plat")
        p_saut14 = plateforme(5950, 500, screen, 100, 10, "plat")
        p_saut15 = plateforme(6150, 425, screen, 100, 10, "plat")
        p_saut16 = plateforme(6350, 350, screen, 100, 10, "plat")
        p_saut17 = plateforme(6550, 275, screen, 1000, 10, "plat")

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
        ############################
        plateformes.append(p_saut13)
        plateformes.append(p_saut14)
        plateformes.append(p_saut15)
        plateformes.append(p_saut16)
        plateformes.append(p_saut17)

        plateformes.append(p_porte)

        # Fruits du niveau:
        f1 = fruit(840, 250, screen)
        f2 = fruit(1630, 545, screen)
        f3 = fruit(1630, 375, screen)
        f4 = fruit(2000, 430, screen)
        f5 = fruit(2540, 100, screen)
        f6 = fruit(3240, 150, screen)

        fruits.append(f1)
        fruits.append(f2)
        fruits.append(f3)
        fruits.append(f4)
        fruits.append(f5)
        fruits.append(f6)

        # Enemis:
        e1 = ennemi(2, 2000, 500, screen, 2000, 2000, 1, 350, 680, 1.75)
        e2 = ennemi(1, 4800, 650, screen, 4799, 5050, 1, 350, 350, 0.5)
        e3 = ennemi(2, 7000, 300, screen, 7000, 7000, 4, 50, 680, 4)


        ennemis.append(e1)
        ennemis.append(e2)
        ennemis.append(e3)

        # Piques ( A changer)
        obstacle1 = obstacles(350, 690, screen)
        obstacle2 = obstacles(350, 630, screen)
        obstacle3 = obstacles(350, 570, screen)
        obstacle4 = obstacles(1530, 360, screen)
        obstacle5 = obstacles(1700, 360, screen)
        obstacle6 = obstacles(1530, 440, screen)
        obstacle7 = obstacles(1700, 440, screen)
        obstacle8 = obstacles(1530, 520, screen)
        obstacle9 = obstacles(1700, 520, screen)
        obstacle10 = obstacles(1530, 680, screen)
        obstacle12 = obstacles(1530, 600, screen)
        obstacle13 = obstacles(1700, 600, screen)
        obstacle14 = obstacles(2800, 680, screen)
        obstacle15 = obstacles(2800, 600, screen)
        obstacle16 = obstacles(2800, 520, screen)
        obstacle17 = obstacles(2800, 440, screen)
        obstacle18 = obstacles(2800, 360, screen)
        ##########
        obstacle19 = obstacles(5500, 620, screen)
        obstacle20 = obstacles(5500, 680, screen)
        obstacle21 = obstacles(5750, 680, screen)
        obstacle22 = obstacles(5830, 680, screen)
        obstacle23 = obstacles(5910, 680, screen)
        obstacle24 = obstacles(5990, 680, screen)
        obstacle25 = obstacles(6070, 680, screen)
        obstacle26 = obstacles(6150, 680, screen)
        obstacle27 = obstacles(6230, 680, screen)
        obstacle28 = obstacles(6310, 680, screen)
        obstacle29 = obstacles(6390, 680, screen)
        obstacle30 = obstacles(6470, 680, screen)
        obstacle31 = obstacles(6550, 680, screen)
        obstacle32 = obstacles(6630, 680, screen)
        obstacle33 = obstacles(6710, 680, screen)



        obs.append(obstacle1)
        obs.append(obstacle2)
        obs.append(obstacle3)
        obs.append(obstacle4)
        obs.append(obstacle5)
        obs.append(obstacle6)
        obs.append(obstacle7)
        obs.append(obstacle8)
        obs.append(obstacle9)
        obs.append(obstacle10)
        obs.append(obstacle12)
        obs.append(obstacle13)
        obs.append(obstacle14)
        obs.append(obstacle15)
        obs.append(obstacle16)
        obs.append(obstacle17)
        obs.append(obstacle18)
        ######################
        obs.append(obstacle19)
        obs.append(obstacle20)
        obs.append(obstacle21)
        obs.append(obstacle22)
        obs.append(obstacle23)
        obs.append(obstacle24)
        obs.append(obstacle25)
        obs.append(obstacle26)
        obs.append(obstacle27)
        obs.append(obstacle28)
        obs.append(obstacle29)
        obs.append(obstacle30)
        obs.append(obstacle31)
        obs.append(obstacle32)
        obs.append(obstacle33)


        #clé
        cle1 = cle(6800, 700, screen)

        #lit
        l1 = lit(3850, 240, screen)


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
