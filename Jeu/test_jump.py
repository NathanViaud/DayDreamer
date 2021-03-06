import pygame
import os
from Jeu.fond import *
from Jeu.plateforme import *
from Jeu.player import *
from Jeu.world import *
from Jeu.fruit import *
from Jeu.ennemi import *
from Jeu.obstacles import *
from Jeu.lit import *
from Jeu.sortie import *
from Jeu.genLevel import *
from Jeu.score_rec import runScore

pygame.init()

music = pygame.mixer.Sound("sound/day_music.wav")
music.set_volume(0.05)

death_sound = pygame.mixer.Sound("sound/oof.wav")
death_sound.set_volume(0.5)

def runGame(screen):
    from Jeu.Menu.menu import runMenu
    from Jeu.Menu.leaderboard import runLeaderboard
    global genLevel

    pygame.display.set_caption("cours forest")

    genLevel = genLevel(screen,0)
    tuto = genLevel.loadLevel(0)
    niveau1 = genLevel.loadLevel(1)
    niveau2 = genLevel.loadLevel(2)
    niveau3 = genLevel.loadLevel(3)
    niveau4 = genLevel.loadLevel(4)


    joue = True

    enCourse = False

    enSaut = False
    mort = pygame.image.load("images/mort.png")

    # World tutoriel:
    tutorial = True

    black = (0,0,0)
    #texte a afficher
    font = pygame.font.Font(None, 40)
    bienvenu = font.render("Bienvenue dans DayDreaming !", True, black)
    mouvement_tuto = font.render("Utilisez les fleches directionnelles pour bouger", True, black)
    saut = font.render("Pour sauter utilisez la barre espace", True, black)
    font = pygame.font.Font(None, 30)
    fruits_message = font.render("Prenez les fruit pour augmenter votre score !", True, black)
    lit_message = font.render("Utilisez la touche F pour dormir dans le lit", True, black)
    cle_message = font.render("Prenez la cle pour ouvrir la porte", True, black)
    porte_message = font.render("Utilisez la porte pour finir le Tutoriel", True, black)
    font = pygame.font.Font(None, 40)
    enemies_messsage = font.render("Attention aux ennemis ! ", True, black)


    # Joueur:
    monde = True

    # Score
    score_font = pygame.font.Font(None, 30)

    niveaux = []
    niveaux.append(tuto)
    niveaux.append(niveau1)
    niveaux.append(niveau2)
    niveaux.append(niveau3)
    niveaux.append(niveau4)

    level = 0
    pts = 0
    cmpt_mort = 0
    tete_mort = pygame.image.load("sprites/compteur_mort.png")
    music.play(-1)

    

    while monde:
        if level != 0:
            tutorial = False
        joueur = player(3, 100, screen, niveaux[level], pts)
        
        joue = True
        joueur.victoire = False
        while joue:
            if niveaux[level].nuit == True:
                color = (255,255,255)
            else:
                color = (0,0,0)
            score = score_font.render("Score: "+str(joueur.score +pts), True, color)
            if level != 0:
                pygame.time.wait(1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    joue = False
                    monde = False
            for ennemi in niveaux[level].ennemis:
                ennemi.moveE()

            niveaux[level].update()
            joueur.deplaceAnimation()
            joueur.update()
            screen.blit(score, (10,10))
            screen.blit(tete_mort, (250,2))
            morts = score_font.render("x "+str(cmpt_mort), True, color)
            screen.blit(morts, (285,7))
            if joueur.cle == False:
                cle_pp = pygame.image.load('sprites/items/cle_pasprise.png')
                screen.blit(cle_pp, (150,5))
            else:
                cle_p = pygame.image.load('sprites/items/cle_prise.png')
                screen.blit(cle_p, (150,10))
            if tutorial == True:
                black = (0,0,0)
                white = (255,255,255)
                font = pygame.font.Font(None, 40)
                if niveaux[level].nuit == True:
                    bienvenu = font.render("Bienvenue dans DayDreaming !", True, white)
                    mouvement_tuto = font.render("Utilisez les fleches directionnelles pour bouger", True, white)
                    saut = font.render("Pour sauter utilisez la barre d'espace", True, white)
                    font = pygame.font.Font(None, 30)
                    fruits_message = font.render("Prenez les legumes pour augmenter votre score !", True, white)
                    lit_message = font.render("Utilisez la touche F pour dormir dans le lit", True, white)
                    cle_message = font.render("Prenez la cle pour ouvrir la porte", True, white)
                    porte_message = font.render("Utilisez la porte pour finir le Tutoriel", True, white)
                    font = pygame.font.Font(None, 40)
                    enemies_messsage = font.render("Attention aux ennemis !", True, white)
                else:
                    bienvenu = font.render("Bienvenue dans DayDreaming !", True, black)
                    mouvement_tuto = font.render("Utilisez les fleches directionnelles pour bouger", True, black)
                    saut = font.render("Pour sauter utilisez la barre d'espace", True, black)
                    font = pygame.font.Font(None, 30)
                    fruits_message = font.render("Prenez les fruits pour augmenter votre score !", True, black)
                    lit_message = font.render("Utilisez la touche F pour dormir dans le lit", True, black)
                    cle_message = font.render("Prenez la cle pour ouvrir la porte", True, black)
                    porte_message = font.render("Utilisez la porte pour finir le Tutoriel", True, black)
                    font = pygame.font.Font(None, 40)
                    enemies_messsage = font.render("Attention aux ennemis !", True, black)
                joueur.estTutoriel = True
                screen.blit(bienvenu, (niveaux[level].fond.pos_x+50,200))
                screen.blit(mouvement_tuto, (niveaux[level].fond.pos_x+50, 300))
                screen.blit(saut, (niveaux[level].fond.pos_x +1200,200))
                screen.blit(fruits_message, (niveaux[level].fond.pos_x+2900, 500))
                screen.blit(lit_message, (niveaux[level].fond.pos_x+3595,650))
                screen.blit(enemies_messsage, (niveaux[level].fond.pos_x+4250, 200))
                screen.blit(cle_message, (niveaux[level].fond.pos_x+5200,350))
                screen.blit(porte_message, (niveaux[level].fond.pos_x+5700, 500))
            else:
                joueur.estTutoriel = False
            pygame.display.update()
            
            if joueur.mort :
                music.stop()
                death_sound.play()
                if level != 0:
                    pts -= 10
                    cmpt_mort += 1

            while joueur.mort and joue:
                screen.blit(mort, (0,0,1024,768))
                pygame.display.update()                        
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        joue = False
                        monde = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            music.stop()
                            joue = False
                            monde = False
                            pseudo = runScore(screen, pts)
                            f = open('Menu/score.txt','a')
                            f.write(str(pseudo))
                            f.write(str('|'))
                            f.write(str(pts) + '\n')
                            f.close()
                            runLeaderboard(screen)
                        elif event.key == pygame.K_SPACE:
                            music.play(-1)
                            joue = False
                            joueur.mort = False
                            if level == 1:
                                joueur.score = 0
                            niveaux[level] = genLevel.loadLevel(level)
                            joueur = player(3, 600, screen, niveaux[level], pts)               
            if joueur.victoire == True:
                if level != 0:
                    pts += joueur.score                   
                joue = False
                level += 1
            if level != 0:
                pygame.time.wait(1)
        if level >= len(niveaux):
            music.stop()
            joue = False
            monde = False
            pseudo = runScore(screen, pts)
            f.write(str(pseudo))
            f.write(str('|'))
            f.write(str(pts) + '\n')
            f.close()
            runLeaderboard(screen)
    runMenu(screen)