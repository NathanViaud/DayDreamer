import pygame
from joueur import joueur
from balle import Balle

class Jeu():
    def __init__(self, joueur1, joueur2):
        pygame.init()

        self.joueur1 = joueur1
        self.joueur2 = joueur2

        BLACK = (0,0,0)
        WHITE = (255,255,255)
        VITESSE = 7

        size = (700,500)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Ping Pong Bondour xD")

        joueurA = joueur(WHITE, 10, 100)
        joueurA.rect.x = 20
        joueurA.rect.y = 200

        joueurB = joueur(WHITE, 10, 100)
        joueurB.rect.x = 670
        joueurB.rect.y = 200

        balle = Balle(WHITE, 10, 10)
        balle.rect.x = 345
        balle.rect.y = 250

        all_sprites_list = pygame.sprite.Group()

        all_sprites_list.add(joueurA)
        all_sprites_list.add(joueurB)
        all_sprites_list.add(balle)

        play = True

        clock = pygame.time.Clock()

        scoreA, scoreB = 0,0

        while play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        play = False

            commandes = pygame.key.get_pressed()

            if commandes[pygame.K_s]:
                joueurA.deplaceBas(VITESSE)
            if commandes[pygame.K_z]:
                joueurA.deplaceHaut(VITESSE)
            if commandes[pygame.K_UP]:
                joueurB.deplaceHaut(VITESSE)
            if commandes[pygame.K_DOWN]:
                joueurB.deplaceBas(VITESSE)

            all_sprites_list.update()

            if balle.rect.y <= 0 or balle.rect.y >= 490:
                balle.vitesse[1] = -balle.vitesse[1]
            if pygame.sprite.collide_mask(balle, joueurA) or pygame.sprite.collide_mask(balle, joueurB):
                balle.rebond()

            screen.fill(BLACK)
            pygame.draw.line(screen, WHITE, [349, 0], [349,500], 5)
            all_sprites_list.draw(screen)

            font = pygame.font.Font(None, 74)
            
            text = font.render(str(scoreA), 1, WHITE)
            screen.blit(text, (250, 10))
            
            text = font.render(str(scoreB), 1, WHITE)
            screen.blit(text, (420, 10))

            font = pygame.font.Font(None, 44)
            
            text = font.render(self.joueur1, 1, WHITE)
            screen.blit(text, (10, 20))

            text = font.render(self.joueur2, 1, WHITE)
            screen.blit(text, (700-(len(self.joueur2)*(font.get_linesize())), 20))

            if balle.rect.x <= 0:
                scoreB += 1
                all_sprites_list.remove(balle)
                balle = Balle(WHITE, 10, 10)
                all_sprites_list.add(balle)
                balle.rect.x = 345
                balle.rect.y = 250

            elif balle.rect.x >= 700:
                scoreA += 1
                all_sprites_list.remove(balle)
                balle = Balle(WHITE, 10, 10)
                all_sprites_list.add(balle)
                balle.rect.x = 345
                balle.rect.y = 250
                balle.vitesse[0] = -balle.vitesse[0]

            pygame.display.flip()
            clock.tick(60)

        print("Au revoir x')")
        pygame.quit()