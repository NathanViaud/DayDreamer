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

def runMenu(screen):
    pygame.display.set_caption("DayDreaming - Menu")

    bgs = [pygame.image.load("images/menu/menu1.png"), pygame.image.load("images/menu/menu2.png"), pygame.image.load("images/menu/menu3.png"), pygame.image.load("images/menu/menu4.png")]

    bg = pygame.image.load("images/menu/menu4.png")
    bg_alpha = pygame.image.load("images/menu/menu4_alpha.png")

    button1 = button(0, 0, "Jouer", True, screen)

    button2 = button(0, 0, "Quitter", False, screen)

    button3 = button(0, 0, "LeaderBoard", False, screen)

    button1.rect.x = (screen.get_width() - button1.rect.width) / 2
    button1.rect.y = (screen.get_height() - button1.rect.height) / 2 - 30

    button2.rect.x = (screen.get_width() - button2.rect.width) / 2 
    button2.rect.y = (screen.get_height() - button2.rect.height + 500) / 2 - 150

    button3.rect.x = screen.get_width() - button3.rect.width - 5
    button3.rect.y = screen.get_height() - button3.rect.height - 10

    buttons = [button1, button2, button3]

    def reveille():
        fonduSurface = pygame.Surface(pygame.display.get_window_size())
        fonduSurface.fill((0,0,0))
        pygame.display.update()
        for alpha in range(0, 510):
            fonduSurface.set_alpha(255 - alpha/2)
            image = bgs[0]
            screen.blit(image, (0,0))
            screen.blit(fonduSurface, (0,0))
            pygame.display.update()

    loop = True
    pause = True
    index = 0
    fondu = True
    while loop:
        if fondu:
            reveille()
            fondu = False
        else:
            if not pause:
                screen.blit(bg, (0,0))
                for b in buttons:
                    b.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        loop = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            loop = False
                        if event.key == pygame.K_DOWN and button1.active:
                            button1.active = False
                            button2.active = True
                            button3.active = False
                        elif event.key == pygame.K_UP and button2.active:
                            button1.active = True
                            button2.active = False
                            button3.active = False
                        elif event.key == pygame.K_DOWN and button2.active:
                            button1.active = False
                            button2.active = False
                            button3.active = True
                        elif event.key == pygame.K_UP and button3.active:
                            button1.active = False
                            button2.active = True
                            button3.active = False
                        if event.key == pygame.K_RETURN:
                            if button3.active:
                                runLeaderboard(screen)
                                loop = False
                            if button2.active:
                                loop = False
                            elif button1.active:
                                button1.change_text("Lancement de la partie")
                                button1.update()
                                button2.clear()
                                button1.update()
                                button2.update()
                                pygame.display.update()
                                pygame.time.wait(1000)
                                test_jump.runGame(screen)
                                loop = False
            else:
                screen.blit(bgs[index], (0,0))
                index += 1
                pygame.display.update()
                pygame.time.wait(500)
                if index > 3:
                    pause = False
        pygame.display.update()