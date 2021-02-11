import pygame
import os
from button import *
import sys
sys.path.append(os.path.abspath(".."))
from Jeu import test_jump
from Jeu import *
from Jeu.test_jump import runGame
from Jeu.test_jump import *
from Jeu.Menu.leaderboard import runLeaderboard
from Jeu.Menu.leaderboard import *
from Jeu.Menu.menu import runMenu
from Jeu.Menu.menu import *

size = (1024,768)
screen = pygame.display.set_mode(size)

runMenu(screen)

pygame.quit()