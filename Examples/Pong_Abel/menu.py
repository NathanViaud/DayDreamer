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
font = pygame.font.Font(None, 32)

continuer = True

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continuer = False
            if active:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    print(input_text)
                    input_text = ""
                else:
                    input_text += event.unicode
        elif event.type == pygame.QUIT:
            continuer = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = True
            else:
                active = False
    if active:
        pygame.draw.rect(screen, WHITE_ACTIVE, input_box)
    else:
        pygame.draw.rect(screen, WHITE, input_box)
    text = font.render(input_text, True, BLACK)
    screen.blit(text, (input_box.x+5, input_box.y+5))
    pygame.display.flip()
pygame.quit()
jeu = Jeu("Abel", "Thyph")
