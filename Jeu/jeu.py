import pygame

from joueurxD import joueurxD

pygame.init()

size = (1024,768)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("cours forest")

joue = True

joueur = joueurxD(1, 3, 600)

all_sprites_updated = pygame.sprite.Group()

all_sprites_updated.add(joueur)

while joue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            joue = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                joue = False
    
    commandes = pygame.key.get_pressed()

    if commandes[pygame.K_LEFT]:
                joueur.deplaceGauche()
    if commandes[pygame.K_RIGHT]:
                joueur.deplaceDroite()
    
    screen.fill((255,255,255))
    all_sprites_updated.draw(screen)
    screen.blit(joueur.image, (joueur.pos_x, joueur.pos_y))
    pygame.time.wait(30)
    pygame.display.flip()

pygame.quit()