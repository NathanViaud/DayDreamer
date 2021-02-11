import pygame

class plateforme():
    #x,y : position
    #width, height : dimensions
    #type : plat = plateforme classique | porte = porte qui bloque le jour | sol : le sol du niveau
    def __init__(self, x, y, screen, width, height, type):
        self.type = type
        if self.type == "porte":
            img = pygame.image.load("sprites/plateforme/p1.png")
        elif self.type == "plat":
            img = pygame.image.load("sprites/plateforme/p1.png")
        elif self.type == "sol":
            img = pygame.image.load("sprites/plateforme/p1.png")
        self.img = pygame.transform.scale(img, (width, height))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen = screen
        self.nuit = False
        self.x_initial = x
        self.y_initial = y
        self.width = width
        self.height = height

    
    def update(self):
        self.screen.blit(self.img, self.rect)
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 2)

    def deplacement(self, vitesse):
        self.rect.x += vitesse
        self.update()
        
    def sleep(self):
        if self.type =="porte" and self.nuit == False:
            self.x_initial = self.rect.x
            self.y_initial = self.rect.y
        self.nuit = not self.nuit
        if self.nuit == True:
            img = pygame.image.load("sprites/plateforme/p1.png")  #plateformes nuit
            if self.type == "porte":
                self.img = pygame.transform.scale(img, (0, 0))
                self.rect = self.img.get_rect()
        else:
            img = pygame.image.load("sprites/plateforme/p1.png")  #plateformes jour
            if self.type == "porte":
                self.img = pygame.transform.scale(img, (self.width, self.height))
                self.rect.x = self.x_initial
                self.rect.y = self.y_initial
                self.rect.width = self.width
                self.rect.height = self.height
        self.update()

    def removePorte(self):
        if self.type == "porte":
            for i in range(0,self.rect.height):
                self.img = pygame.transform.scale(self.img, (0, self.rect.y+1))
                self.rect = self.img.get_rect()
                self.update()
                print(self.rect.y)
                pygame.display.update()
                pygame.time.wait(1)
        
