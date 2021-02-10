import pygame

class plateforme():
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
        

    
    def update(self):
        self.screen.blit(self.img, self.rect)
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 2)

    def deplacement(self, vitesse):
        self.rect.x += vitesse
        self.update()
        
    def sleep(self):
        self.nuit = not self.nuit
        if self.nuit == True:
            img = pygame.image.load("sprites/plateforme/p1.png")  #plateformes nuit
            if self.type == "porte":
                self.img = pygame.transform.scale(img, (0, 0))
                self.rect = self.img.get_rect()
        else:
            img = pygame.image.load("sprites/plateforme/p1.png")  #plateformes jour
        self.img = pygame.transform.scale(img, (self.rect.width, self.rect.height))
        self.update()
