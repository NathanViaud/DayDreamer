import pygame
import os
from button import *
import sys
sys.path.append(os.path.abspath(".."))
from Jeu import test_jump
from Jeu import *
from Jeu.test_jump import runGame
from Jeu.test_jump import *

def runLeaderboard(screen):
    from Jeu.Menu.menu import runMenu
    pygame.display.set_caption("DayDreaming - LeaderBoard")

    bg = pygame.image.load("images/leaderboard.png")

    button1 = button(0, 0, "Revenir au menu", True, screen)

    button1.rect.x = (screen.get_width() - button1.rect.width) /2-200
    button1.rect.y = 700
    button1.rect.height = 500
    button1.rect.width = 300


    buttons = [button1]
    loop = True

    joueurs = []

    f = open('Menu/score.txt', 'r')
    lines = f.readlines()
    for line in lines:
        l = line.split('|')
        nom = l[0]
        points = l[1]
        joueur = [nom, points]
        joueurs.append(joueur)

    leaderboard = []

    for i in range(0, 5):
        maxi = joueurs[i]
        for joueur in joueurs:
            if int(joueur[1]) > int(maxi[1]):
                maxi = joueur
        joueurs.remove(maxi)
        leaderboard.append(maxi)

    font = pygame.font.Font("font/font_menu.ttf", 40)
    white = (255, 255, 255)

    while loop:
        screen.blit(bg, (0,0))
        for i in range(len(leaderboard)):
            pts = str(leaderboard[i][1])
            score = font.render(str(leaderboard[i][0] + " : " + pts), True, white)
            screen.blit(score, (200, 175+i*100))
        for b in buttons:
            b.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                loop = False
        pygame.display.update()