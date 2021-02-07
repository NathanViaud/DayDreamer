import pygame
from game import Jeu

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
WHITE_ACTIVE = (200,200,200)

size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Menu mdrrrr")

input_text = ""
input_box = pygame.Rect(100, 100, 140, 32)
active = False

continuer = True

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continuer = False
                pygame.quit()
        elif event.type == pygame.QUIT:
            continuer = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = True
            else:
                active = False
    if active:
        pygame.draw.rect(screen, WHITE_ACTIVE, [100, 100, 140, 32])
    else:
        pygame.draw.rect(screen, WHITE, [100, 100, 140, 32])
        
    pygame.display.flip()

#jeu = Jeu("Abel", "Thyph")