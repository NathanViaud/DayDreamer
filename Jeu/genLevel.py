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
    def __init__(self,screen, niveau):
        self.screen = screen
        self.niveau = niveau


    def loadLevel(self, niveau):
        self.niveau = niveau
        if self.niveau == 0:
            return self.genTuto()
        elif self.niveau == 1:
            return self.genNiveau1()
        elif self.niveau == 2:
            return self.genNiveau2()
        elif self.niveau == 3:
            return self.genNiveau3()
        elif self.niveau == 4:
            return self.genNiveau4()


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
        p_saut4 = plateforme(2400,700, self.screen, 50, 50, "bloc")
        p_saut5 = plateforme(2662,700, self.screen, 50, 50, "bloc")
        p_sautfruit1 = plateforme(3000, 600, self.screen, 100, 10, "plat")
        p_sautfruit2 = plateforme(3200, 450, self.screen, 100, 10, "plat")
        p_sautfruit3 = plateforme(3400, 250, self.screen, 100, 10, "plat")
        p_porte = plateforme(4000, sol.rect.y-768, self.screen, 100,768, "porte")
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
        sol = plateforme(0, 750, self.screen, 8196, 18, "sol")
        p_saut1 = plateforme(1300, 600, self.screen, 100, 150, "plat")
        p_saut2 = plateforme(1400, 450, self.screen, 200, 1000, "plat")
        p_saut3 = plateforme(1820, 300, self.screen, 100, 10, "plat")
        p_saut4 = plateforme(2400,700, self.screen, 50, 50, "plat")
        p_saut5 = plateforme(2785,700, self.screen, 50, 50, "plat")
        p_saut6 = plateforme(1640, 600, self.screen, 100, 150, "plat")
        p_saut7 = plateforme(2578, 500, self.screen, 70, 10, "plat")
        p_sautfruit2 = plateforme(3200, 430, self.screen, 100, 10, "plat")
        p_sautfruit3 = plateforme(3400, 250, self.screen, 100, 10, "plat")
        p_sautfruit4 = plateforme(2790, 250, self.screen, 100, 10, "plat")
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
        f5 = fruit(2600, 180, self.screen)
        f6 = fruit(2820, 210, self.screen)
        f7 = fruit(1850, 260, self.screen)
        fruits.append(f2)
        fruits.append(f3)
        fruits.append(f4)
        fruits.append(f5)
        fruits.append(f6)
        fruits.append(f7)
        # Enemis:
        e1 = ennemi(2, 4470, 500, self.screen, 4470, 4470, 1, 200, 660, 2)
        e2 = ennemi(2, 4670, 500, self.screen, 4570, 4570, 1, 200, 670, 3)
        e3 = ennemi(2, 4870, 500, self.screen, 4570, 4570, 1, 200, 650, 4)

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
        l1 = lit(3800, 735, self.screen)

        # Sortie
        sort = sortie(5750, 622, self.screen)

        fond.reset()

        return world(fond, plateformes, fruits, ennemis, obs, cle1, l1, sort)

    def genNiveau2(self):
        from Jeu.ennemi import ennemi
        from Jeu.fond import fond
        from Jeu.ennemi import ennemi
        plateformes = []
        fruits = []
        ennemis = []
        obs = []
        fond = fond(self.screen, 8300)
        sol = plateforme(0, 750, self.screen, 8196, 18, "sol")
        p_saut1 = plateforme(800, 500, self.screen, 100, 10, "plat")
        p_saut2 = plateforme(650, 350, self.screen, 100, 10, "plat")
        p_saut3 = plateforme(800, 300, self.screen, 100, 10, "plat")
        p_saut4 = plateforme(950, 250, self.screen, 100, 10, "plat")
        p_saut5 = plateforme(1300, 280, self.screen, 100, 10, "plat")
        p_saut6 = plateforme(2300, 500, self.screen, 140, 10, "plat")
        p_saut7 = plateforme(2500, 200, self.screen, 100, 10, "plat")
        p_saut8 = plateforme(2600, 300, self.screen, 100, 10, "plat")
        p_saut9 = plateforme(3000, 450, self.screen, 100, 10, "plat")
        p_saut10 = plateforme(3200, 200, self.screen, 100, 10, "plat")
        p_saut11 = plateforme(3650, 500, self.screen, 100, 10, "plat")
        p_saut12 = plateforme(3850, 250, self.screen, 100, 10, "plat")
        ###################################
        p_saut13 = plateforme(5750, 575, self.screen, 100, 10, "plat")
        p_saut14 = plateforme(5950, 500, self.screen, 100, 10, "plat")
        p_saut15 = plateforme(6150, 425, self.screen, 100, 10, "plat")
        p_saut16 = plateforme(6350, 350, self.screen, 100, 10, "plat")
        p_saut17 = plateforme(6550, 275, self.screen, 1000, 10, "plat")
        p_saut18 = plateforme(7650, 450, self.screen, 100, 10, "plat")
        p_saut19 = plateforme(7850, 600, self.screen, 100, 10, "plat")

        p_porte = plateforme(4000, 0, self.screen, 100,768, "porte")

        plateformes.append(sol)
        plateformes.append(p_saut1)
        plateformes.append(p_saut2)
        plateformes.append(p_saut3)
        plateformes.append(p_saut4)
        plateformes.append(p_saut5)
        plateformes.append(p_saut6)
        plateformes.append(p_saut7)
        plateformes.append(p_saut8)
        plateformes.append(p_saut9)
        plateformes.append(p_saut10)
        plateformes.append(p_saut11)
        plateformes.append(p_saut12)
        ############################
        plateformes.append(p_saut13)
        plateformes.append(p_saut14)
        plateformes.append(p_saut15)
        plateformes.append(p_saut16)
        plateformes.append(p_saut17)
        plateformes.append(p_saut18)
        plateformes.append(p_saut19)

        plateformes.append(p_porte)

        # Fruits du niveau:
        f1 = fruit(840, 250, self.screen)
        f2 = fruit(1630, 545, self.screen)
        f3 = fruit(1630, 375, self.screen)
        f4 = fruit(2000, 430, self.screen)
        f5 = fruit(2540, 100, self.screen)
        f6 = fruit(3240, 150, self.screen)

        fruits.append(f1)
        fruits.append(f2)
        fruits.append(f3)
        fruits.append(f4)
        fruits.append(f5)
        fruits.append(f6)

        # Enemis:
        e1 = ennemi(2, 2000, 500, self.screen, 2000, 2000, 1, 350, 680, 1.75)
        e2 = ennemi(1, 4800, 700 , self.screen, 4799, 5050, 1, 350, 350, 0.5)
        e3 = ennemi(2, 7000, 300, self.screen, 7000, 7000, 4, 50, 680, 4)


        ennemis.append(e1)
        ennemis.append(e2)
        ennemis.append(e3)

        # Piques ( A changer)
        obstacle1 = obstacles(350, 690, self.screen)
        obstacle2 = obstacles(350, 630, self.screen)
        obstacle3 = obstacles(350, 570, self.screen)
        obstacle4 = obstacles(1530, 360, self.screen)
        obstacle5 = obstacles(1700, 360, self.screen)
        obstacle6 = obstacles(1530, 440, self.screen)
        obstacle7 = obstacles(1700, 440, self.screen)
        obstacle8 = obstacles(1530, 520, self.screen)
        obstacle9 = obstacles(1700, 520, self.screen)
        obstacle10 = obstacles(1530, 680, self.screen)
        obstacle12 = obstacles(1530, 600, self.screen)
        obstacle13 = obstacles(1700, 600,self.screen)
        obstacle14 = obstacles(2800, 680,self.screen)
        obstacle15 = obstacles(2800, 600,self.screen)
        obstacle16 = obstacles(2800, 520,self.screen)
        obstacle17 = obstacles(2800, 440,self.screen)
        obstacle18 = obstacles(2800, 360,self.screen)
        ##########
        obstacle19 = obstacles(5500, 620,self.screen)
        obstacle20 = obstacles(5500, 680,self.screen)
        obstacle21 = obstacles(5750, 680,self.screen)
        obstacle22 = obstacles(5830, 680,self.screen)
        obstacle23 = obstacles(5910, 680,self.screen)
        obstacle24 = obstacles(5990, 680,self.screen)
        obstacle25 = obstacles(6070, 680,self.screen)
        obstacle26 = obstacles(6150, 680,self.screen)
        obstacle27 = obstacles(6230, 680,self.screen)
        obstacle28 = obstacles(6310, 680,self.screen)
        obstacle29 = obstacles(6390, 680,self.screen)
        obstacle30 = obstacles(6470, 680,self.screen)
        obstacle31 = obstacles(6550, 680,self.screen)
        obstacle32 = obstacles(6630, 680,self.screen)
        obstacle33 = obstacles(6710, 680,self.screen)



        obs.append(obstacle1)
        obs.append(obstacle2)
        obs.append(obstacle3)
        obs.append(obstacle4)
        obs.append(obstacle5)
        obs.append(obstacle6)
        obs.append(obstacle7)
        obs.append(obstacle8)
        obs.append(obstacle9)
        obs.append(obstacle10)
        obs.append(obstacle12)
        obs.append(obstacle13)
        obs.append(obstacle14)
        obs.append(obstacle15)
        obs.append(obstacle16)
        obs.append(obstacle17)
        obs.append(obstacle18)
        ######################
        obs.append(obstacle19)
        obs.append(obstacle20)
        obs.append(obstacle21)
        obs.append(obstacle22)
        obs.append(obstacle23)
        obs.append(obstacle24)
        obs.append(obstacle25)
        obs.append(obstacle26)
        obs.append(obstacle27)
        obs.append(obstacle28)
        obs.append(obstacle29)
        obs.append(obstacle30)
        obs.append(obstacle31)
        obs.append(obstacle32)
        obs.append(obstacle33)


        #clé
        cle1 = cle(6800, 700,self.screen)

        #lit
        l1 = lit(3850, 235,self.screen)


        # Sortie
        sort = sortie(8000, 622,self.screen)

        fond.reset()

        return world(fond, plateformes, fruits, ennemis, obs, cle1, l1, sort)

    def genNiveau3(self):
        from Jeu.ennemi import ennemi
        from Jeu.fond import fond
        from Jeu.ennemi import ennemi
        plateformes = []
        fruits = []
        ennemis = []
        obs = []
        fond = fond(self.screen, 8200)
        sol = plateforme(0, 750, self.screen, 8196, 18, "sol")
        p_saut1 = plateforme(800, 500, self.screen, 100, 10, "plat")
        p_saut2 = plateforme(1050, 450, self.screen, 100, 10, "plat")
        p_saut3 = plateforme(800, 300, self.screen, 100, 10, "plat")
        p_saut4 = plateforme(1300, 250, self.screen, 100, 500, "plat")
        # parcours
        p_saut5 = plateforme(2100, 500, self.screen, 100, 10, "plat")
        p_saut6 = plateforme(2450, 420, self.screen, 80, 10, "plat")
        p_saut7 = plateforme(2800, 360, self.screen, 60, 10, "plat")
        p_saut8 = plateforme(3150, 280, self.screen, 40, 10, "plat")
        # fin parcours jour

        #-----------nuit---------------#
        p_saut9 = plateforme(4300, 500, self.screen, 110, 10, "plat")
        p_saut10 = plateforme(4650, 420, self.screen, 90, 10, "plat")
        p_saut11 = plateforme(5000, 360, self.screen, 70, 10, "plat")
        p_saut12 = plateforme(5350, 280, self.screen, 50, 10, "plat")
        p_saut13 = plateforme(5700, 280, self.screen, 30, 10, "plat")
        p_saut14 = plateforme(6030, 280, self.screen, 30, 10, "plat")
        p_saut15 = plateforme(6330, 280, self.screen, 20, 10, "plat")


        p_porte = plateforme(4000, 0, self.screen, 100,768, "porte")

        plateformes.append(sol)
        plateformes.append(p_saut1)
        plateformes.append(p_saut2)
        plateformes.append(p_saut3)
        plateformes.append(p_saut4)
        plateformes.append(p_saut5)
        plateformes.append(p_saut6)
        plateformes.append(p_saut7)
        plateformes.append(p_saut8)
        plateformes.append(p_saut9)
        plateformes.append(p_saut10)
        plateformes.append(p_saut11)
        plateformes.append(p_saut12)
        plateformes.append(p_saut13)
        plateformes.append(p_saut14)
        plateformes.append(p_saut15)

        plateformes.append(p_porte)

        # Fruits du niveau:
        f1 = fruit(840, 250, self.screen)
        f2 = fruit(3155, 230, self.screen)
        f3 = fruit(3155, 500, self.screen)

        fruits.append(f1)
        fruits.append(f2)
        fruits.append(f3)

        # Enemis:
        e1 = ennemi(1, 800, 650, self.screen, 799, 1200, 3, 350, 350, 3)
        e2 = ennemi(2, 7500, 300, self.screen, 7500, 7500, 4, 50, 680, 4)
        e3 = ennemi(2, 7000, 300, self.screen, 7000, 7000, 4, 50, 680, 4)
        e4 = ennemi(2, 7250, 300, self.screen, 7250, 7250, 4, 50, 680, 4)


        ennemis.append(e1)
        ennemis.append(e2)
        ennemis.append(e3)
        ennemis.append(e4)

        # Piques ( A changer)
        obstacle1 = obstacles(350, 690, self.screen)
        obstacle2 = obstacles(350, 640, self.screen)
        obstacle3 = obstacles(350, 368, self.screen)
        obstacle4 = obstacles(350, 318, self.screen)
        #debut triangle
        obstacle5 = obstacles(1400, 240, self.screen)
        obstacle6 = obstacles(1450, 290, self.screen)
        obstacle7 = obstacles(1500, 340, self.screen)
        obstacle8 = obstacles(1550, 390, self.screen)
        obstacle9 = obstacles(1600, 440, self.screen)
        obstacle10 = obstacles(1650, 590, self.screen)

        #fin triangle

        obstacle11 = obstacles(3150, 690, self.screen)
        obstacle12 = obstacles(3150, 640, self.screen)
        obstacle13 = obstacles(3150, 368, self.screen)
        obstacle14 = obstacles(3150, 318, self.screen)

        # debut
        obs.append(obstacle1)
        obs.append(obstacle2)
        obs.append(obstacle3)
        obs.append(obstacle4)

        # triangle
        obs.append(obstacle5)
        obs.append(obstacle6)
        obs.append(obstacle7)
        obs.append(obstacle8)
        obs.append(obstacle9)
        obs.append(obstacle10)

        # porte fin niveau jour
        obs.append(obstacle11)
        obs.append(obstacle12)
        obs.append(obstacle13)
        obs.append(obstacle14)


        #clé
        cle1 = cle(6330, 80, self.screen)

        #lit
        l1 = lit(3850, 690, self.screen)


        # Sortie
        sort = sortie(8000, 622, self.screen)

        fond.reset()

        return world(fond, plateformes, fruits, ennemis, obs, cle1, l1, sort)


    def genNiveau4(self):
        from Jeu.ennemi import ennemi
        from Jeu.fond import fond
        from Jeu.ennemi import ennemi
        plateformes = []
        fruits = []
        ennemis = []
        obs = []
        fond = fond(self.screen, 8200)
        sol = plateforme(0, 750, self.screen, 8196, 18, "sol")
        p_saut1 = plateforme(1800, 500, self.screen, 100, 10, "plat")
        p_saut2 = plateforme(2100, 400, self.screen, 100, 10, "plat")
        p_saut3 = plateforme(1830, 250, self.screen, 20, 10, "plat")
        p_saut4 = plateforme(2410, 100, self.screen, 150, 10, "plat")
        p_saut5 = plateforme(2680, 250, self.screen, 100, 10, "plat")
        p_saut6 = plateforme(2900, 415, self.screen, 100, 10, "plat")
        p_saut7 = plateforme(2680, 500, self.screen, 100, 10, "plat")
        p_saut8 = plateforme(2900, 200, self.screen, 100, 10, "plat")
        p_saut9 = plateforme(3300, 200, self.screen, 50, 10, "plat")
        p_saut10 = plateforme(3600, 200, self.screen, 20, 10, "plat")
        p_saut11 = plateforme(3880, 200, self.screen, 20, 10, "plat")
        p_saut12 = plateforme(3820, 400, self.screen, 100, 10, "plat")
        p_saut13 = plateforme(5500, 500, self.screen, 100, 10, "plat")
        p_saut14 = plateforme(5800, 415, self.screen, 30, 10, "plat")
        p_saut15 = plateforme(6050, 415, self.screen, 30, 10, "plat")
        p_saut16 = plateforme(6300, 400, self.screen, 100, 10, "plat")
        p_saut17 = plateforme(6330, 200, self.screen, 20, 10, "plat")



        p_porte = plateforme(4000, 0, self.screen, 100,768, "porte")

        plateformes.append(sol)
        plateformes.append(p_saut1)
        plateformes.append(p_saut2)
        plateformes.append(p_saut3)
        plateformes.append(p_saut4)
        plateformes.append(p_saut5)
        plateformes.append(p_saut6)
        plateformes.append(p_saut7)
        plateformes.append(p_saut8)
        plateformes.append(p_saut9)
        plateformes.append(p_saut10)
        plateformes.append(p_saut11)
        plateformes.append(p_saut12)

        plateformes.append(p_saut13)
        plateformes.append(p_saut14)
        plateformes.append(p_saut15)
        plateformes.append(p_saut16)
        plateformes.append(p_saut17)

        plateformes.append(p_porte)

        # Fruits du niveau:
        f1 = fruit(1815, 50, self.screen)
        f2 = fruit(2415, 500, self.screen)
        f3 = fruit(3880, 50, self.screen)

        fruits.append(f1)
        fruits.append(f2)
        fruits.append(f3)

        # Enemis:
        e1 = ennemi(1, 4500, 650, self.screen, 4499, 5000, 1, 350, 350, 1)
        e2 = ennemi(2, 1500, 300, self.screen, 1500, 1500, 4, 280, 680, 4)
        e3 = ennemi(2, 5300, 300, self.screen, 5300, 5300, 4, 50, 680, 4)
        e4 = ennemi(2, 5900, 300, self.screen, 5900, 5900, 4, 50, 680, 4)


        ennemis.append(e1)
        ennemis.append(e2)
        ennemis.append(e3)
        ennemis.append(e4)

        # Piques ( A changer)
        obstacle1 = obstacles(350, 690, self.screen)
        obstacle2 = obstacles(400, 690, self.screen)
        obstacle3 = obstacles(450, 690, self.screen)
        obstacle4 = obstacles(500, 690, self.screen)
        obstacle5 = obstacles(700, 690, self.screen)
        obstacle6 = obstacles(900, 690, self.screen)
        obstacle7 = obstacles(900, 640, self.screen)
        obstacle8 = obstacles(1100, 690, self.screen)
        obstacle9 = obstacles(1100, 640, self.screen)
        obstacle10 = obstacles(1100, 590, self.screen)

        obstacle11 = obstacles(2400, 690, self.screen)
        obstacle12 = obstacles(2400, 640, self.screen)
        obstacle13 = obstacles(2400, 368, self.screen)
        obstacle14 = obstacles(2550, 368, self.screen)
        obstacle15 = obstacles(2550, 500, self.screen)

        obstacle16 = obstacles(6600, 690, self.screen)
        obstacle17 = obstacles(6650, 690, self.screen)
        obstacle18 = obstacles(6700, 690, self.screen)
        obstacle19 = obstacles(6750, 690, self.screen)
        obstacle20 = obstacles(6950, 690, self.screen)
        obstacle21 = obstacles(7150, 690, self.screen)
        obstacle22 = obstacles(7150, 640, self.screen)
        obstacle23 = obstacles(7350, 690, self.screen)
        obstacle24 = obstacles(7350, 640, self.screen)
        obstacle25 = obstacles(7350, 590, self.screen)
        # debut
        obs.append(obstacle1)
        obs.append(obstacle2)
        obs.append(obstacle3)
        obs.append(obstacle4)
        obs.append(obstacle5)
        obs.append(obstacle6)
        obs.append(obstacle7)
        obs.append(obstacle8)
        obs.append(obstacle9)
        obs.append(obstacle10)
        obs.append(obstacle11)
        obs.append(obstacle12)
        obs.append(obstacle13)
        obs.append(obstacle14)
        obs.append(obstacle15)

        # nuit
        obs.append(obstacle16)
        obs.append(obstacle17)
        obs.append(obstacle18)
        obs.append(obstacle19)
        obs.append(obstacle20)
        obs.append(obstacle21)
        obs.append(obstacle22)
        obs.append(obstacle23)
        obs.append(obstacle24)
        obs.append(obstacle25)
        #clé
        cle1 = cle(6330, 80, self.screen)

        #lit
        l1 = lit(3850, 390, self.screen)


        # Sortie
        sort = sortie(8000, 622, self.screen)

        fond.reset()

        return world(fond, plateformes, fruits, ennemis, obs, cle1, l1, sort)
