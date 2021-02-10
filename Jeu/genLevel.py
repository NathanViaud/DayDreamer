import pygame
from Jeu.world import *
from Jeu.fond import *
from Jeu.plateforme import *
from Jeu.player import *
from Jeu.world import *
from Jeu.fruit import *
from Jeu.ennemi import *
from Jeu.obstacles import *
from Jeu.lit import *
from Jeu.sortie import *

class genLevel():
    def __init__(self, screen, niveau):
        self.screen = screen
        self.niveau = niveau


    def loadLevel(self, niveau):
        self.niveau = niveau
        if self.niveau == 0:
            return self.genTuto()
        if self.niveau == 1:
            return self.genNiveau1()

    
    def genTuto(self):
        from Jeu.fond import fond
        from Jeu.ennemi import ennemi
        fond = fond(self.screen, 6250)
        # Sol du terrain
        plateformes = []
        sol = plateforme(0, 750, self.screen, 8196, 18, "sol")
        p_saut1 = plateforme(1300, 600, self.screen, 100, 10, "plat")
        p_saut2 = plateforme(1600, 450, self.screen, 100, 10, "plat")
        p_saut3 = plateforme(1900, 600, self.screen, 100, 10, "plat")
        p_saut4 = plateforme(2400,700, self.screen, 50, 50, "plat")
        p_saut5 = plateforme(2662,700, self.screen, 50, 50, "plat")
        p_sautfruit1 = plateforme(3000, 600, self.screen, 100, 10, "plat")
        p_sautfruit2 = plateforme(3200, 450, self.screen, 100, 10, "plat")
        p_sautfruit3 = plateforme(3400, 250, self.screen, 100, 10, "plat")
        p_porte = plateforme(4000, 0, self.screen, 100,768, "porte")
        p_cle1 = plateforme(4250, 600, self.screen, 100, 10, "plat")
        p_cle2 = plateforme(4600, 450, self.screen, 100, 10, "plat")
        p_cle3 = plateforme(4800, 450, self.screen, 300, 10, "plat")
        p_cle4 = plateforme(5250,450, self.screen, 100, 10, "plat")
        plateformes.append(sol)
        plateformes.append(p_saut1)
        plateformes.append(p_saut2)
        plateformes.append(p_saut3)
        plateformes.append(p_saut4)
        plateformes.append(p_saut5)
        plateformes.append(p_sautfruit1)
        plateformes.append(p_sautfruit2)
        plateformes.append(p_sautfruit3)
        plateformes.append(p_porte)
        plateformes.append(p_cle1)
        plateformes.append(p_cle2)
        plateformes.append(p_cle3)
        plateformes.append(p_cle4)

        # Fruits du niveau:
        fruits = []
        f1 = fruit(3035, 555, self.screen)
        f2 = fruit(3235, 400, self.screen)
        f3 = fruit(3435, 200, self.screen)
        fruits.append(f1)
        fruits.append(f2)
        fruits.append(f3)

        # Enemis:
        e1 = ennemi(2, 4470, 500, self.screen, 4470, 4470, 1, 300, 650, 2)
        e2 = ennemi(1, 4800, p_cle2.rect.y - pygame.image.load("sprites/ennemis/pizza1.png").get_height(), self.screen, 4799, 5050, 2, 350, 350, 1)
        ennemis = []
        ennemis.append(e1)
        ennemis.append(e2)

        # Piques ( A changer)
        obstacle1 = obstacles(2460, 690, self.screen)
        obstacle2 = obstacles(2524, 690, self.screen)
        obstacle3 = obstacles(2588, 690, self.screen)
        obs = []
        obs.append(obstacle1)
        obs.append(obstacle2)
        obs.append(obstacle3)

        #clé
        cle1 = cle(5280, 400, self.screen)

        #lit
        l1 = lit(3800, 735, self.screen)

        # Sortie
        sort = sortie(5750, 622, self.screen)

        fond.reset()
        
        return world(fond, plateformes, fruits, ennemis, obs, cle1, l1, sort)

    def genNiveau1(self):
        from Jeu.ennemi import ennemi
        from Jeu.fond import fond
        from Jeu.ennemi import ennemi
        plateformes = []
        fruits = []
        ennemis = []
        obs = []
        fond = fond(self.screen, 6250)
        # Sol du terrain
        sol = plateforme(0, 750, self.screen, 8196, 18, "sol")
        p_saut1 = plateforme(1300, 600, self.screen, 100, 150, "plat")
        p_saut2 = plateforme(1400, 450, self.screen, 200, 1000, "plat")
        p_saut3 = plateforme(1820, 200, self.screen, 100, 10, "plat")
        p_saut4 = plateforme(2400,700, self.screen, 50, 50, "plat")
        p_saut5 = plateforme(2785,700, self.screen, 50, 50, "plat")
        p_saut6 = plateforme(1640, 600, self.screen, 100, 150, "plat")
        p_saut7 = plateforme(2578, 500, self.screen, 70, 10, "plat")
        p_sautfruit2 = plateforme(3200, 430, self.screen, 100, 10, "plat")
        p_sautfruit3 = plateforme(3400, 250, self.screen, 100, 10, "plat")
        p_sautfruit4 = plateforme(2790, 220, self.screen, 100, 10, "plat")
        p_porte = plateforme(4000, 0, self.screen, 100,768, "porte")
        p_cle1 = plateforme(4250, 600, self.screen, 100, 10, "plat")
        p_cle2 = plateforme(4600, 450, self.screen, 100, 10, "plat")
        p_cle3 = plateforme(4800, 450, self.screen, 300, 10, "plat")
        p_cle4 = plateforme(5250,450, self.screen, 100, 10, "plat")
        plateformes.append(sol)
        plateformes.append(p_saut1)
        plateformes.append(p_saut2)
        plateformes.append(p_saut3)
        plateformes.append(p_saut4)
        plateformes.append(p_saut5)
        plateformes.append(p_saut6)
        plateformes.append(p_saut7)
        plateformes.append(p_sautfruit2)
        plateformes.append(p_sautfruit3)
        plateformes.append(p_sautfruit4)
        plateformes.append(p_porte)
        # plateformes.append(p_cle1)
        # plateformes.append(p_cle2)
        # plateformes.append(p_cle3)
        # plateformes.append(p_cle4)

        # Fruits du niveau:
        f2 = fruit(3235, 380, self.screen)
        f3 = fruit(3435, 200, self.screen)
        f4 = fruit(1605, 700, self.screen)
        f5 = fruit(2600, 100, self.screen)
        f6 = fruit(2820, 180, self.screen)
        f7 = fruit(1850, 160, self.screen)
        fruits.append(f2)
        fruits.append(f3)
        fruits.append(f4)
        fruits.append(f5)
        fruits.append(f6)
        fruits.append(f7)
        # Enemis:
        e1 = ennemi(2, 4470, 500, self.screen, 4470, 4470, 1, 200, 650, 2)
        e2 = ennemi(2, 4670, 500, self.screen, 4570, 4570, 1, 200, 600, 3)
        e3 = ennemi(2, 4870, 500, self.screen, 4570, 4570, 1, 200, 600, 4)

        # e2 = ennemi(1, 4800, 350, screen, 4799, 5050, 2, 350, 350, 1)
        ennemis.append(e1)
        ennemis.append(e2)
        ennemis.append(e3)

        # Piques ( A changer)
        obstacle1 = obstacles(2460, 690, self.screen)
        obstacle2 = obstacles(2524, 690, self.screen)
        obstacle3 = obstacles(2588, 690, self.screen)
        obstacle4 = obstacles(1450, 400, self.screen)
        obstacle5 = obstacles(2652, 690, self.screen)
        obstacle6 = obstacles(2716, 690, self.screen)
        obs.append(obstacle1)
        obs.append(obstacle2)
        obs.append(obstacle3)
        obs.append(obstacle4)
        obs.append(obstacle5)
        obs.append(obstacle6)

        #clé
        cle1 = cle(5280, 700, self.screen)

        #lit
        l1 = lit(3800, 700, self.screen)

        # Sortie
        sort = sortie(5750, 622, self.screen)

        fond.reset()

        return world(fond, plateformes, fruits, ennemis, obs, cle1, l1, sort)