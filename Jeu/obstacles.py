import pygame

class obstacles:
    def __init__(self, x, y, screen):
        img = pygame.image.load('sprites/obstacles/obstacle1.png')
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen = screen

    def update(self):
        self.screen.blit(self.img, self.rect)
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 2)


    def deplacement(self, vitesse):
        self.rect.x += vitesse
        self.update()

