import pygame

from joueurxD import joueurxD

from fond import *
from plateforme import *

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

joueur = joueurxD(3, 600, screen)

fond = fond(pygame.image.load("images/fond.png"))

all_sprites = pygame.sprite.Group()

all_sprites.add(joueur)

vitesse = 0

while joue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            joue = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                joue = False
            if event.key == pygame.K_UP:
                joueur.enSaut = True
            if event.key == pygame.K_LEFT:
                vitesse = -5
            if event.key == pygame.K_RIGHT:
                vitesse = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                vitesse = 0
            elif event.key == pygame.K_RIGHT:
                vitesse = 0

    joueur.deplace(vitesse)
    all_sprites.draw(screen)
    screen.blit(fond.img, (fond.pos_x, 0))
    pygame.time.wait(60)
    joueur.draw()
    joueur.saut()
    joueur.immobile(vitesse)
    pygame.display.flip()
pygame.quit()