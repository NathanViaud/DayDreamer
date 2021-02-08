import pygame

from joueurxD import joueurxD

from fond import *

pygame.init()

VITESSE_SAUT = 40
HAUTEUR_SAUT = 100

size = (1024,768)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("cours forest")

joue = True

jouecourse = False

jouesaut = False

course = pygame.mixer.Sound("./son/course.wav")
saut = pygame.mixer.Sound("./son/saut.wav")

joueur = joueurxD(1, 3, 600)

fond = fond(pygame.image.load("images/fond.png"))

all_sprites = pygame.sprite.Group()

all_sprites.add(joueur)



while joue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            joue = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                joue = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                joueur.immobile()
                course.stop()
                jouecourse = False
            if event.key == pygame.K_UP:
                jouesaut = False
    
    commandes = pygame.key.get_pressed()

    if commandes[pygame.K_LEFT]:
        joueur.deplaceGauche()
        if jouecourse == False:
            course.play(-1)
            jouecourse = True
        fond.gauche(5)
        while joueur.pos_y < 600:
                joueur.pos_y += VITESSE_SAUT
                print(joueur.pos_y)
                screen.fill((255,255,255))
                all_sprites.draw(screen)    
                screen.blit(fond.img, (fond.pos_x, 0))
                all_sprites.draw(screen)
                screen.blit(joueur.image, (joueur.pos_x, joueur.pos_y))
                pygame.time.wait(80)
                pygame.display.flip()
    if commandes[pygame.K_RIGHT]:
        joueur.deplaceDroite()
        if jouecourse == False:
            course.play(-1)
            jouecourse = True
        fond.droite(-5)
        while joueur.pos_y < 600:
            joueur.pos_y += VITESSE_SAUT
            print(joueur.pos_y)
            screen.fill((255,255,255))
            all_sprites.draw(screen)    
            screen.blit(fond.img, (fond.pos_x, 0))
            all_sprites.draw(screen)
            screen.blit(joueur.image, (joueur.pos_x, joueur.pos_y))
            pygame.time.wait(80)
            pygame.display.flip()
    if commandes[pygame.K_UP]:
        if jouesaut == False:
            saut.play()
            jouesaut = True
        while joueur.pos_y > 600 - HAUTEUR_SAUT:
            joueur.pos_y -= VITESSE_SAUT
            screen.fill((255,255,255))
            all_sprites.draw(screen)    
            screen.blit(fond.img, (fond.pos_x, 0))
            all_sprites.draw(screen)
            screen.blit(joueur.image, (joueur.pos_x, joueur.pos_y))
            pygame.time.wait(80)
            pygame.display.flip()
    
    while joueur.pos_y < 600:
        joueur.pos_y += VITESSE_SAUT
        print(joueur.pos_y)
        screen.fill((255,255,255))
        all_sprites.draw(screen)    
        screen.blit(fond.img, (fond.pos_x, 0))
        all_sprites.draw(screen)
        screen.blit(joueur.image, (joueur.pos_x, joueur.pos_y))
        pygame.time.wait(80)
        pygame.display.flip()


    screen.fill((255,255,255))
    all_sprites.draw(screen)    
    screen.blit(fond.img, (fond.pos_x, 0))
    all_sprites.draw(screen)
    screen.blit(joueur.image, (joueur.pos_x, joueur.pos_y))
    pygame.time.wait(80)
    pygame.display.flip()

pygame.quit()