import pygame
from pygame import locals as const
from raquette import *
from balle import *

def main():
    print("Appuyez sur n'importe quelle touche pour lancer la partie ! ")
    pygame.init()

    ecran = pygame.display.set_mode((640, 480))
    fond = pygame.image.load("images/fond.png")
    sDebut = pygame.mixer.Sound("Sons/Bruit_7.wav")

    continuer = True
    ecran.blit(fond, (0,0))
    pygame.display.flip()

    while continuer:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
                pygame.quit()
            elif event.type == pygame.KEYUP:
                pygame.mixer.Sound.play(sDebut)
                jeu()


def jeu():

    pygame.mixer.init()
    ecran = pygame.display.set_mode((640,480))
    fond = pygame.image.load("images/jeu.png")

    w, h = pygame.display.get_surface().get_size()

    raquette1 = raquette(1,h/2 -50,0)
    raquette2 = raquette(2,h/2 -50,0)
    pos = (w/2,h/2)
    balle = balletest(pos)

    sMilieu = pygame.mixer.Sound("Sons/Bruit_1.wav")
    sBarre = pygame.mixer.Sound("Sons/Bruit_5.wav")
    


    continuer = False
    end = True

    ecran.blit(fond, (0,0))

    s1 = 0
    s2 = 0
    while end:
        balle.reset(pos)
        raquette1.reset(h/2 -50)
        raquette2.reset(h/2 -50)
        ecran.blit(fond, (0, 0))
        ecran.blit(raquette1.img,(raquette1.pos_x, raquette1.pos_y))
        ecran.blit(raquette2.img,(raquette2.pos_x, raquette2.pos_y))
        pygame.draw.circle(ecran, (0,255,0), (balle.pos_x, balle.pos_y), 5)
        sj1 = pygame.image.load("images/"+str(s1)+".png")
        sj2 = pygame.image.load("images/"+str(s2)+".png")
        ecran.blit (sj1, (w/4, 0))
        ecran.blit (sj2, (3*w/4, 0))
        if s1 == 3:
            fin(2,sj1, sj2)
        elif s2 == 3:
            fin(1, sj1, sj2)
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    continuer = True
        pygame.display.flip()
        while continuer:
            ecran.blit(fond, (0, 0))
            ecran.blit(raquette1.img,(raquette1.pos_x, raquette1.pos_y))
            ecran.blit(raquette2.img,(raquette2.pos_x, raquette2.pos_y))
            pygame.draw.circle(ecran, (0,255,0), (balle.pos_x, balle.pos_y), 5)
            if balle.pos_x == w/2 or balle.pos_x == w/2 +1:
                pygame.mixer.Sound.play(sMilieu)
            if raquette1.pos_y <= 0 or raquette1.pos_y >= 380:
                raquette1.stop()
            if raquette2.pos_y <= 0 or raquette2.pos_y >= 380:
                raquette2.stop()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    continuer = False
                    end = False
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z:
                        if raquette1.pos_y != 0:
                            raquette1.setVitesse(-5)
                    elif event.key == pygame.K_s:
                        if raquette1.pos_y != 380:
                            raquette1.setVitesse(5)
                    elif event.key == pygame.K_UP:
                        if raquette2.pos_y != 0:
                            raquette2.setVitesse(-5)
                    elif event.key == pygame.K_DOWN:
                        if raquette2.pos_y != 380:
                            raquette2.setVitesse(5)
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_z or event.key == pygame.K_s:
                        raquette1.stop()
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                        raquette2.stop()
            if balle.pos_y >= h-5 or balle.pos_y <= 5:
                balle.my()
            elif balle.pos_x <= 10 and balle.pos_y >= raquette1.pos_y and balle.pos_y <= raquette1.pos_y +100:
                balle.mx()
                pygame.mixer.Sound.play(sBarre)
            elif balle.pos_x >= 630 and balle.pos_y >= raquette2.pos_y and balle.pos_y <= raquette2.pos_y +100:
                balle.mx()
                pygame.mixer.Sound.play(sBarre)
            elif balle.pos_x <= 5:
                s2 += 1
                continuer = False
            elif balle.pos_x >= w-5:
                s1 += 1
                continuer = False
            pygame.time.wait(1)
            balle.mouv()
            raquette1.mouvR()
            raquette2.mouvR()
            pygame.display.flip()


def fin(j, sj1, sj2):

    sDefaite = pygame.mixer.Sound("Sons/Bruit_2.wav")
    sVictoire = pygame.mixer.Sound("Sons/Bruit_8.wav")
    ecran = pygame.display.set_mode((640, 480))
    w, h = pygame.display.get_surface().get_size()
    if j == 1:
        fond = pygame.image.load("images/j1.png")
        pygame.mixer.Sound.play(sDefaite)
    elif j == 2:
        fond = pygame.image.load("images/j2.png")
        pygame.mixer.Sound.play(sVictoire)
    fin = True
    ecran.blit(fond, (0,0))
    ecran.blit(sj1, (w/4, 3*h/4))
    ecran.blit(sj2, (3*w/4, 3*h/4))
    pygame.display.flip()

    while fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = False
            if event.type == pygame.KEYUP:
                fin = False

    pygame.display.flip()


pygame.quit()
    


if __name__ == '__main__':
    main()

