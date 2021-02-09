import pygame

class Player():
    def __init__(self, x ,y, screen, world):
        self.images_r = []
        self.images_l = []
        self.index = 0
        self.counter = 0
        for num in range (1,3):
            img_r = pygame.image.load(f'./sprites/player{num}.png')
            img_l = pygame.transform.flip(img_r, True, False)
            self.images_r.append(img_r)
            self.images_l.append(img_l)
        self.image = self.images_r[self.index]
        self.screen = screen
        self.world = world
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = " "

    def update(self):

        dx = 0
        dy = 0
        mov_cooldown = 20
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False:
            self.vel_y = -10
            self.jumped = True
        if key[pygame.K_LEFT]:
            dx -= 2
            self.counter += 1
            self.direction = "gauche"
        if key[pygame.K_RIGHT]:
            dx += 2
            self.index += 1
            self.counter += 1
            self.direction = "droite"
        if key[pygame.K_RIGHT] == False and key[pygame.K_LEFT] == False:
            self.image = self.images_r[0]
            self.counter = 0
            self.index = 0


        if self.counter > mov_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_r):
                self.index = 0
            if self.direction == "droite":
                self.image = self.images_r[self.index]
            if self.direction == "gauche":
                self.image = self.images_l[self.index]

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

        self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect, 2)