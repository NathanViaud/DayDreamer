import pygame

from joueurxD import joueurxD

from fond import *
from plateforme import *
from player import *
from world import *
from fruit import *
from ennemi import *

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

p1 = plateforme(250, 450, screen)
p2 = plateforme(750, 550, screen)

plateformes = [p1, p2]
fond = fond(pygame.image.load("images/fond.png"), screen)
f1 = fruit(800, 740, screen)
f2 = fruit(1700, 740, screen)
fruits = [f1, f2]

e1 = ennemi(700, 678, screen, 300, 900, 1)
ennemis =  [e1]
world = world(fond, plateformes, fruits, ennemis)

joueur = player(3, 600, screen, world)


deb = 300
fin = 1400

while joue:
    pygame.time.wait(1)
    screen.blit(fond.img, (fond.pos_x, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            joue = False
    world.update()
    e1.moveE()
    joueur.deplaceAnimation()
    joueur.update()
    pygame.display.update()
pygame.quit()