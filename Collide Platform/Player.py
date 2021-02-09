import pygame

immobile = pygame.image.load("sprites/player1.png")

class Player():
    def __init__(self, x ,y, screen, world):
        self.images_r = []
        self.images_l = []
        self.index = 0

        for i in range (1,3):
            self.images_l.append(immobile)
        for i in range (1,3):
            self.images_l.append(pygame.image.load("sprites/player2.png"))
        for i in range (1,3):
            self.images_l.append(immobile)
        for i in range (1,3):
            self.images_l.append(pygame.image.load("sprites/player3.png"))

        for i in range (1,3):
            self.images_r.append(immobile)
        for i in range (1,3):
            self.images_r.append(pygame.image.load("sprites/droite1.png"))
        for i in range (1,3):
            self.images_r.append(immobile)
        for i in range (1,3):
            self.images_r.append(pygame.image.load("sprites/droite2.png"))

        self.image = immobile
        self.screen = screen
        self.world = world
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = ""

    def update(self):

        if self.index >= 7:
            self.index = 0

        dx = 0
        dy = 0
        mov_cooldown = 20
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False:
            self.vel_y = -10
            self.jumped = True
        if key[pygame.K_LEFT]:
            dx -= 10
            self.index += 1
            self.direction = "gauche"
        if key[pygame.K_RIGHT]:
            dx += 10
            self.index += 1
            self.direction = "droite"
        if key[pygame.K_RIGHT] == False and key[pygame.K_LEFT] == False:
            self.image = immobile
            self.index = 0
        if key[pygame.K_RIGHT] and key[pygame.K_LEFT]:
            self.image = immobile
            self.index = 0

        self.vel_y += 0.1
        if self.vel_y > 2:
            self.vel_y = 2
        dy += self.vel_y

        if self.world[0].rect.colliderect(self.rect.x+dx, self.rect.y, self.width, self.height):
            dx = 0
        if self.world[0].rect.colliderect(self.rect.x, self.rect.y+dy, self.width, self.height):
            if self.vel_y < 0:
                dy = self.world[0].rect.bottom - self.rect.top
                self.vel_y = 0
            elif self.vel_y > 0:
                dy = self.world[0].rect.top - self.rect.bottom
                self.vel_y = 0
            self.jumped = False


        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > self.screen.get_height():
            self.rect.bottom = self.screen.get_height()
            dy = 550
            self.jumped = False
        
        print(self.index)
        self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect, 2)


    def deplaceAnimation(self):
        if self.direction == "gauche":
            self.image = self.images_r[self.index]
        elif self.direction == "droite":
            self.image = self.images_l[self.index]
        else:
            self.image = immobile