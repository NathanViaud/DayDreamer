import pygame

from joueurxD import joueurxD

from fond import *
from plateforme import *
from player import *

pygame.init()

VITESSE_SAUT = 40
HAUTEUR_SAUT = 100

size = (1024,768)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("cours forest")

joue = True

enCourse = False

enSaut = False

course = pygame.mixer.Sound("./son/course.wav")
saut = pygame.mixer.Sound("./son/saut.wav")

p1 = plateforme(500, 450, screen)
p2 = plateforme(750, 550, screen)

plateformes = [p1, p2]
fond = fond(pygame.image.load("images/fond.png"), screen)


joueur = player(3, 600, screen, plateformes, fond)


while joue:
    screen.blit(fond.img, (fond.pos_x, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            joue = False
    joueur.update()
    for i in plateformes:
        i.update()
    pygame.display.update()
pygame.quit()