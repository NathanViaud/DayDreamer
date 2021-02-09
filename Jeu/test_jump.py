import pygame

from joueurxD import joueurxD

from fond import *
from plateforme import *
from player import *
from world import *
from fruit import *
from ennemi import *
from obstacles import *

pygame.init()

VITESSE_SAUT = 40
HAUTEUR_SAUT = 100

size = (1024,768)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("cours forest")

joue = True

enCourse = False

enSaut = False

course = pygame.mixer.Sound("./son/course.wav")
saut = pygame.mixer.Sound("./son/saut.wav")
fond = fond(pygame.image.load("images/fond.png"), screen, 8196)

#p_saut1 = plateforme(450, 450, screen)
#p_saut2 = plateforme(750, 550, screen)

# plateformes = []
# 
# plateformes.append(p_saut1)
# plateformes.append(p_saut2)
# 
# f1 = fruit(800, 740, screen)
# f2 = fruit(1700, 740, screen)
# fruits = [f1, f2]
# 
# e1 = ennemi(1, 700, 678, screen, 300, 900, 1)
# e2 = ennemi(2, 1500, 350, screen, 1000, 1900, 1)
# 
# ennemis =  [e1, e2]
# world = world(fond, plateformes, fruits, ennemis)
# 
# joueur = player(3, 600, screen, world)


# World tutoriel:
tutorial = True


#texte a afficher
white = (255,255,255)
font = pygame.font.Font(None, 50)
mouvement_tuto = font.render("Utilisez les fleches directionnelles pour bouger", True, white)
saut = font.render("Pour sauter utilisez la barre espace", True, white)

# Sol du terrain
sol = plateforme(0, 750, screen, 8196, 18)
p_saut1 = plateforme(1300, 600, screen, 100, 10)
p_saut2 = plateforme(1600, 450, screen, 100, 10)
p_saut3 = plateforme(1900, 600, screen, 100, 10)
p_saut4 = plateforme(2400,700, screen, 50, 50)
p_saut5 = plateforme(2662,700, screen, 50, 50)
plateformes = []
plateformes.append(sol)
plateformes.append(p_saut1)
plateformes.append(p_saut2)
plateformes.append(p_saut3)
plateformes.append(p_saut4)
plateformes.append(p_saut5)

# Fruits du niveau:
fruits = []
f1 = fruit(800, 600, screen)
f2 = fruit(1100, 400, screen)
fruits.append(f1)
fruits.append(f2)

# Enemis:
ennemis = []

# Piques ( A changer)
obs = []
obstacle1 = obstacles(1500, 550, screen)
obs.append(obstacle1)

tuto = world(fond, plateformes, fruits, ennemis, obs)


# Joueur:
joueur = player(3, 600, screen, tuto)

while joue:
    pygame.time.wait(1)
    screen.blit(fond.img, (fond.pos_x, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            joue = False
    tuto.update()
    for ennemi in ennemis:
        ennemi.moveE()

    
    joueur.deplaceAnimation()
    joueur.update()
    if tutorial == True:
        screen.blit(mouvement_tuto, (fond.pos_x+100, 244))
        screen.blit(saut, (fond.pos_x+1500,244))
    pygame.display.update()
pygame.quit()