import pygame
from fond import *

pygame.init()

screen = pygame.display.set_mode((1024, 768))
fond_img = pygame.image.load("images/fond.png")

fond = fond(fond_img)

continuer = True

screen.blit(fond.img, (0, 0))
pygame.display.flip()

while continuer:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                print(fond.pos_x)
                fond.Droite(10)
                screen.blit(fond.img, (fond.pos_x, 0))
                pygame.display.flip()
            elif event.key == pygame.K_q:
                print(fond.pos_x)
                fond.Gauche(-10)
                screen.blit(fond.img, (fond.pos_x, 0))
                pygame.display.flip()

pygame.quit()