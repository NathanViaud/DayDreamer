# Créé par Abel LAROUSSI, le 10/04/2016 en Python 3.2
import pygame
import os
from pygame.locals import *
import pygame.transform
import sys
global niveau
liste_key = pygame.key.get_pressed()
pygame.init()
cle = pygame.mixer.Sound("data/sound/cle.wav")
discours1 = pygame.mixer.Sound("data/sound/discour1.wav")
perdu = pygame.mixer.Sound("data/sound/Mort.wav")
gagne = pygame.mixer.Sound("data/sound/Victoire.wav")
tir = pygame.mixer.Sound("data/sound/Coup.wav")
ding = pygame.mixer.Sound("data/sound/ding.wav")
ding.set_volume(0.25)
niveau = 1
spawnX = 105
spawnY = 497
global spawnX_enm_lvl1
global spawnY_enm_lvl1
spawnX_enm_lvl1 = 1200
spawnY_enm_lvl1 = 405
import Algorithme_fichier_de_niveau
Algorithme_fichier_de_niveau.charger(niveau)
global document, confirmation
document = False
confirmation = False

def mort():
    global niveau, spawnX, spawnY
    niveau = 0
    print("GAME OVER")
    import Algorithme_fichier_de_niveau
    Algorithme_fichier_de_niveau.charger(niveau)
    spawnX = 6000
    spawnY = 6000
    import Coeur
    Coeur.continuer = 0
    Coeur.boucleprincipale()

def retry():
    global niveau, spawnX, spawnY
    niveau = 1
    print("Retry")
    import Algorithme_fichier_de_niveau
    Algorithme_fichier_de_niveau.charger(niveau)
    spawnX = 105
    spawnY = 497
    import Coeur
    Coeur.continuer = 0
    Coeur.boucleprincipale()
    global confirmation, document
    confirmation = False
    document = False

def collisionAction(nextPos,liste):
    global document
    global niveau, spawnX, spawnY
    if (nextPos.collidelist(liste) == 0) and (niveau == 1):    #sortie du niveau 1 vers niveau 2
        try:
            cle.play()
        except:
            pygame.quit()
        niveau = 2
        print("1 vers 2")
        import Algorithme_fichier_de_niveau
        Algorithme_fichier_de_niveau.charger(niveau)
        spawnX = 52
        spawnY = 365
        import Coeur
        Coeur.continuer = 0
        Coeur.boucleprincipale()

    if (nextPos.collidelist(liste) == 1) and (niveau == 1) and (document == True):    #detection de la zone cryptage
        print("déclenche cryptage")
        import cesar_crypt

    elif (nextPos.collidelist(liste) == 0) and(niveau == 2):    #sortie du niveau 2 vers niveau 1
        try:
            cle.play()
        except:
            pygame.quit()
        niveau = 1
        print("2 vers 1")
        import Algorithme_fichier_de_niveau
        Algorithme_fichier_de_niveau.charger(niveau)
        spawnX = 1224
        spawnY = 452
        import Coeur
        Coeur.continuer = 0
        Coeur.boucleprincipale()

    elif (nextPos.collidelist(liste) == 1) and(niveau == 2):    #sortie du niveau 2 vers niveau 3
        try:
            print("")
        except:
            pygame.quit()
        niveau = 3
        print("2 vers 3")
        import Algorithme_fichier_de_niveau
        Algorithme_fichier_de_niveau.charger(niveau)
        spawnX = 47
        spawnY = 395
        import Coeur
        Coeur.continuer = 0
        Coeur.boucleprincipale()

    elif (nextPos.collidelist(liste) == 0) and(niveau == 3):    #sortie du niveau 3 vers niveau 2
        try:
            print("")
        except:
            pygame.quit()
        niveau = 2
        print("3 vers 2")
        import Algorithme_fichier_de_niveau
        Algorithme_fichier_de_niveau.charger(niveau)
        spawnX = 1190
        spawnY = 346
        import Coeur
        Coeur.continuer = 0
        Coeur.boucleprincipale()


    elif (nextPos.collidelist(liste) == 1) and(niveau == 3):    #sorie du niveau 3 vers niveau 4
        try:
            print("")
        except:
            pygame.quit()
        niveau = 4
        print("3 vers 4")
        import Algorithme_fichier_de_niveau
        Algorithme_fichier_de_niveau.charger(niveau)
        spawnX = 40
        spawnY = 395
        import Coeur
        Coeur.continuer = 0
        Coeur.boucleprincipale()


    elif (nextPos.collidelist(liste) == 0) and(niveau == 4):    #sorie du niveau 4 vers niveau 3
        try:
            print("")
        except:
            pygame.quit()
        niveau = 3
        print("4 vers 3")
        import Algorithme_fichier_de_niveau
        Algorithme_fichier_de_niveau.charger(niveau)
        spawnX = 1221
        spawnY = 392
        import Coeur
        Coeur.continuer = 0
        Coeur.boucleprincipale()



    elif (nextPos.collidelist(liste) == 1) and(niveau == 4):    #sorie du niveau 4 vers niveau 5
        try:
            print("")
        except:
            pygame.quit()
        niveau = 5
        print("4 vers 5")
        import Algorithme_fichier_de_niveau
        Algorithme_fichier_de_niveau.charger(niveau)
        spawnX = 548
        spawnY = 594
        import Coeur
        Coeur.continuer = 0
        Coeur.boucleprincipale()



    elif (nextPos.collidelist(liste) == 0) and(niveau == 5):    #sorie du niveau 5 vers niveau 4
        try:
            print("")
        except:
            pygame.quit()
        niveau = 4
        print("sortie tente")
        import Algorithme_fichier_de_niveau
        Algorithme_fichier_de_niveau.charger(niveau)
        spawnX = 450
        spawnY = 162
        import Coeur
        Coeur.continuer = 0
        Coeur.boucleprincipale()

    elif (nextPos.collidelist(liste) == 1) and(niveau == 5) and (document == False):    #ramassage des documents
        ding.play()
        print("documents ramasses")
        document = True
        import Coeur




def collisionEnnemi(position,liste,n_pas):
    print (n_pas)
    if (position.collidelist(liste) == 2) and (niveau == 3) and (n_pas>45) and (n_pas<80):    #detection de l'ennemi
        print("repéré1")
        mort()
    if (position.collidelist(liste) == 3) and (niveau == 3) and (n_pas>80) and (n_pas<160):
        print("repéré2")
        mort()
    if (position.collidelist(liste) == 4) and (niveau == 3) and (n_pas>160) and (n_pas<200):
        print("repéré3")
        mort()
    if (position.collidelist(liste) == 5) and (niveau == 3) and (n_pas>200) and (n_pas<250):
        print("repéré4")
        mort()
    if (position.collidelist(liste) == 6) and (niveau == 3) and (n_pas>250) and (n_pas<310):
        print("repéré5")
        mort()
    if (position.collidelist(liste) == 7) and (niveau == 3) and (n_pas>310) and (n_pas<320):
        print("repéré6")
        mort()

