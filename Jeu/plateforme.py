import pygame

class plateforme():
    def __init__(self, x, y, screen):
        img = pygame.image.load("sprites/plateforme/p1.png")
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen = screen
        
    def droite(self, vitesse):
        self.rect.x -=  vitesse

    def gauche(self, vitesse):
        self.rect.x +=  vitesse

    def update(self):
        #self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 2)