import pygame
import os
from button import *
import sys
sys.path.append(os.path.abspath(".."))
from Jeu import test_jump
from Jeu import *
from Jeu.test_jump import runGame
from Jeu.test_jump import *

size = (1024, 768)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("DayDreaming - LeaderBoard")

bg = pygame.image.load("images/leaderboard.png")

button1 = button(0, 0, "Jouer", True, screen)
button2 = button(0, 0, "Quitter", False, screen)

button1.rect.x = (screen.get_width() - button1.rect.width) /2-200
button1.rect.y = 700
button1.rect.height = 500
button1.rect.width = 300

button2.rect.x = (screen.get_width() - button2.rect.width) /2+200
button2.rect.y = 700

buttons = [button1, button2]
loop = True

while loop:
    screen.blit(bg, (0,0))
    for b in buttons:
        b.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                loop == False
            if event.key == pygame.K_RIGHT:
                button1.active = False
                button2.active = True
            if event.key == pygame.K_LEFT:
                button1.active = True
                button2.active = False
            if event.key == pygame.K_RETURN:
                if button2.active:
                    loop = False
                if button1.active:
                    button1.change_text("Lancement de la partie")
                    button1.update()
                    button2.clear()
                    button1.update()
                    button2.update()
                    test_jump.runGame(screen)
                    loop = False
    pygame.display.update()
pygame.quit()

