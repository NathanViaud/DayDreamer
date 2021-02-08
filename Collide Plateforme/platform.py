import pygame

class Platform():
    def __init__(self, x, y, screen):
        img = pygame.image.load("platform.png")
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen = screen

    def update(self):
        self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 2)
