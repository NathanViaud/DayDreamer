import pygame
import os
print("initialisé")
from pygame.locals import *
import pygame.transform
import sys
pygame.init()




def boucleprincipale():


    #------------------------------------ Chargement des sons ------------------------------------#
    from Algorithme_fichier_de_niveau_action import confirmation
    from Algorithme_fichier_de_niveau_action import document
    from Algorithme_fichier_de_niveau_action import cle
    from Algorithme_fichier_de_niveau_action import discours1
    from Algorithme_fichier_de_niveau_action import perdu
    from Algorithme_fichier_de_niveau_action import gagne
    from Algorithme_fichier_de_niveau_action import tir
    import Algorithme_fichier_de_niveau_action
    from Algorithme_fichier_de_niveau_action import niveau
    niveauActuel = niveau
    from Algorithme_fichier_de_niveau_action import spawnX_enm_lvl1, spawnY_enm_lvl1
    pygame.mixer.init()
    discours1.set_volume(0.025)
    #------------------------------------Définition de la vitesse du perso (en pixels)------------------------------------#
    clock=pygame.time.Clock()
    SPEED = 20
    SPEED2 = 7

    #------------------------------------Ouverture de la fenêtre Pygame------------------------------------#

    fenetre = pygame.display.set_mode((1280, 720))
    pygame.mouse.set_visible(0)


    #------------------------------------Chargement et collage du fond------------------------------------#
    if niveau == 0 and confirmation == True:
        discours1.stop()
        gagne.play(loops=-1)
        fond = pygame.image.load("data/image/background/fin.png").convert()
        fenetre.blit(fond, (0,0))
    elif niveau == 0 and confirmation == False:
        discours1.stop()
        tir.play()
        perdu.play(loops=-1)
        fond = pygame.image.load("data/image/background/mort.png")
        fenetre.blit(fond, (0,0))
    if niveau == 1:
        discours1.stop()
        perdu.stop()
        gagne.stop()
        fond = pygame.image.load("data/image/background/niveau1.png").convert()
        fenetre.blit(fond, (0,0))

    if niveau == 2:
        fond = pygame.image.load("data/image/background/niveau2.png").convert()
        fenetre.blit(fond, (0,0))
        discours1.play()
    if niveau == 3:
        fond = pygame.image.load("data/image/background/niveau3.png")
        fenetre.blit(fond, (0,0))

    if niveau == 4:
        fond = pygame.image.load("data/image/background/niveau4.png")
        fenetre.blit(fond, (0,0))

    if niveau == 5:
        fond = pygame.image.load("data/image/background/niveau5.png")
        fenetre.blit(fond, (0,0))

    #------------------------------------chargement des sprites du perso-----------------------------------------#

    marchedroite1 = pygame.image.load("data/image/perso/d1.png")
    marchedroite2 = pygame.image.load("data/image/perso/d2.png")
    marchegauche1 = pygame.image.load("data/image/perso/g1.png")
    marchegauche2 = pygame.image.load("data/image/perso/g2.png")
    marcheimmod = pygame.image.load("data/image/perso/IMP.png")
    marcheimmog = pygame.image.load("data/image/perso/IMP2.png")
    marchedroite=[marcheimmod,marchedroite1,marcheimmod,marchedroite2]
    marchegauche=[marcheimmog,marchegauche1,marcheimmog,marchegauche2]


    #------------------------------------chargement des sprites de l'ennemi-----------------------------------------#

    marchedroite1_enm = pygame.image.load("data/image/enm/d1.png")
    marchedroite2_enm = pygame.image.load("data/image/enm/d2.png")
    marchegauche1_enm = pygame.image.load("data/image/enm/g1.png")
    marchegauche2_enm = pygame.image.load("data/image/enm/g2.png")
    marcheimmod_enm = pygame.image.load("data/image/enm/IMP.png")
    marcheimmog_enm = pygame.image.load("data/image/enm/IMP2.png")
    marchedroite_enm=[marcheimmod_enm,marchedroite1_enm,marcheimmod_enm,marchedroite2_enm]
    marchegauche_enm=[marcheimmog_enm,marchegauche1_enm,marcheimmog_enm,marchegauche2_enm]


    #------------------------------------Spawn------------------------------------#

    from Algorithme_fichier_de_niveau_action import spawnX,spawnY


    #------------------------------------Création d'une classe pour le perso------------------------------------#

    class Perso(object) :
        """Personnage""" #Définir les bases du perso (image, position,...)
        def __init__(self, fenetre) :
            self.fenetre = fenetre
            self.image = marchedroite[0]
            self.pos = self.image.get_rect(center=(spawnX,spawnY))
            self.fenetre.blit(self.image, (0,0))
            self.face=0
    # Définition des déplacements (avec les animations)
        def deplacement(self, direction) :
            "permet de bouger le perso"
            if direction == "droite" :
                self.image = marchedroite[0]
                self.pos = self.pos.move(SPEED,0) #Déplacement à droite
                self.face=(self.face+1)%4         #Changement d'image pour le perso (animations)
                self.image=marchedroite[0+self.face]
            elif direction == "gauche" :
                self.image = marchegauche[0]
                self.pos = self.pos.move(-SPEED,0)
                self.face=(self.face+1)%4
                self.image=marchegauche[0+self.face]
            elif direction == "haut" :
                self.pos = self.pos.move(0,-SPEED)
            elif direction == "bas" :
                self.pos = self.pos.move(0,SPEED)


    perso = Perso(fenetre)


    #------------------------------------Création d'une classe pour l'ennemi------------------------------------#

    class Enm(object) :
        """Ennemi""" #Définir les bases de l'ennemi (image, position,...)
        def __init__(self, fenetre) :
            self.fenetre = fenetre
            self.image_enm = marchedroite_enm[0]
            self.pos_enm = self.image_enm.get_rect(center=(spawnX_enm_lvl1,spawnY_enm_lvl1))
            self.fenetre.blit(self.image_enm, (0,0))
            self.face_enm=0
    # Définition des déplacements (avec les animations)
        def deplacement_enm(self, direction_enm) :
            "permet de bouger l'ennemi"
            if direction_enm == "droite" :
                self.image_enm = marchedroite_enm[0]
                self.pos_enm = self.pos_enm.move(SPEED2,0) #Déplacement à droite
                self.face_enm=(self.face_enm+1)%4         #Changement d'image pour le perso (animations)
                self.image_enm=marchedroite_enm[0+self.face_enm]
            elif direction_enm == "gauche" :
                self.image_enm = marchegauche_enm[0]
                self.pos_enm = self.pos_enm.move(-SPEED2,0)
                self.face_enm=(self.face_enm+1)%4
                self.image_enm=marchegauche_enm[0+self.face_enm]
            elif direction_enm == "haut" :
                self.pos_enm = self.pos_enm.move(0,-SPEED2)
            elif direction_enm == "bas" :
                self.pos_enm = self.pos_enm.move(0,SPEED2)

    class Doc(pygame.sprite.Sprite):
        """les documents"""
        def __init__(self):
            pygame.sprite.Sprite.__init__(self) #call Sprite initializer
            self.image = pygame.image.load("data/image/entities/doc.png")
            self.rect = self.image.get_rect(center=(643,407))





    doc = Doc()
    allsprites = pygame.sprite.RenderPlain(doc)
    enm = Enm(fenetre)
    n_pas = 0
    n_pas2 = 0


    def deplacementlvl1():
        if n_pas>=0 and n_pas<160:
            enm.deplacement_enm("gauche")
        if n_pas>=160 and n_pas<=320:
            enm.deplacement_enm("droite")


    #------------------------------------Collsions et Interactions------------------------------------#

    import Algorithme_fichier_de_niveau
    from Algorithme_fichier_de_niveau import n
    from Algorithme_fichier_de_niveau import n2
    from Algorithme_fichier_de_niveau import listeCollision
    from Algorithme_fichier_de_niveau import listeCollisionAction
    import Algorithme_fichier_de_niveau_action
    from Algorithme_fichier_de_niveau_action import niveau
    mescollisions = []
    mesCollisionsAction = []
    x = -4
    i = 0
    while i< n/4:
        x = x + 4
        mescollisions.append(pygame.Rect(listeCollision[x],listeCollision[x+1],listeCollision[x+2],listeCollision[x+3]))
        i = i+1

    x = -4
    i = 0
    while i< n2/4:
        x = x + 4
        mesCollisionsAction.append(pygame.Rect(listeCollisionAction[x],listeCollisionAction[x+1],listeCollisionAction[x+2],listeCollisionAction[x+3]))
        i = i+1


    #------------------------------------Rafraîchissement de l'écran------------------------------------#

    pygame.display.flip()
    continuer = 1

    #------------------------------------Boucle Principale----------------------------------------------#

    while continuer :
        liste_key = pygame.key.get_pressed()

        if liste_key[K_UP] : #Si on appuie sur "haut"
            next_pos = perso.pos.move(0,-SPEED) #Le perso bougera vers le haut...
            Algorithme_fichier_de_niveau_action.collisionAction(next_pos,mesCollisionsAction) #Si perso à cote de la boite définie
            if next_pos.collidelist(mescollisions) == -1 : #Gestion des collisions
                perso.deplacement("haut") #Si y'a pas, il bougera vers le ô
            else: print("collision") #Sinon il ne se déplacera pas

        if liste_key[K_DOWN] : #De même que ci-dessus
            next_pos = perso.pos.move(0,+SPEED)
            Algorithme_fichier_de_niveau_action.collisionAction(next_pos,mesCollisionsAction)
            if next_pos.collidelist(mescollisions) == -1 :
                perso.deplacement("bas")
            else: print("collision")

        if liste_key[K_RIGHT] : #Idem
            next_pos = perso.pos.move(+SPEED,0)
            Algorithme_fichier_de_niveau_action.collisionAction(next_pos,mesCollisionsAction)
            if next_pos.collidelist(mescollisions) == -1 :
                perso.deplacement("droite")
            else: print("collision")

        if liste_key[K_LEFT] : #Pareil
            next_pos = perso.pos.move(-SPEED,0)
            Algorithme_fichier_de_niveau_action.collisionAction(next_pos,mesCollisionsAction)
            if next_pos.collidelist(mescollisions) == -1 :
                perso.deplacement("gauche")
            else: print("collision")

        if liste_key[K_ESCAPE] :
            pygame.quit()
            sys.exit()

        if niveau == 3:
            deplacementlvl1()
            Algorithme_fichier_de_niveau_action.collisionEnnemi(perso.pos, mesCollisionsAction, n_pas)

        if niveau == 0:
            if liste_key[K_SPACE]:
                Algorithme_fichier_de_niveau_action.retry()
            if liste_key[K_ESCAPE]:
                pygame.quit()
                sys.exit()

        pygame.time.wait(8) #Besoin pour pas que le perso aille trop vite
        clock.tick(8)
        fenetre.blit(fond, (0,0))
        try:                                             #
                fenetre.blit(fond, (0,0))
                fenetre.blit(perso.image, perso.pos)
                                                             # Rafraichissement
                if niveau == 3 and document == False:        #
                    fenetre.blit(enm.image_enm, enm.pos_enm)
                if niveau == 5 and document == False:
                    allsprites.update()
                    allsprites.draw(fenetre)
                    from Algorithme_fichier_de_niveau_action import document
                if niveau == 5 and document == True:
                    allsprites.clear(fenetre,fond)
                    allsprites.update()
                pygame.display.flip()                        #
                pygame.display.update()                      #
                if niveau == 3:
                    fenetre.blit(enm.image_enm, enm.pos_enm)

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
        except:
                continuer = 0
        if document == False and niveau == 3:
            n_pas = n_pas + 1
            if n_pas == 320:
                    n_pas = 0

            n_pas2 = n_pas2 + 1
            if n_pas2 == 24:
                    n_pas2 = 0
        from Algorithme_fichier_de_niveau_action import niveau
        if niveau != niveauActuel:
            continuer = 0
    #------------------------------------------------------------------------------------------------------------#