import pygame

class Player():
    def __init__(self, x ,y, screen, world):
        img = pygame.image.load("idle.png")
        self.screen = screen
        self.world = world
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False

    def update(self):

        dx = 0
        dy = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False:
            self.vel_y = -10
            self.jumped = True
        if key[pygame.K_SPACE] == False:
            self.jumped = False
        if key[pygame.K_LEFT]:
            dx -= 2 
        if key[pygame.K_RIGHT]:
            dx += 2
        

        self.vel_y += 0.1
        if self.vel_y > 2:
            self.vel_y = 2
        dy += self.vel_y


        if self.world[0].rect.colliderect(self.rect.x, self.rect.y+dy, self.width, self.height):
            if self.vel_y < 0:
                dy = self.world[0].rect.bottom - self.rect.top
            if self.vel_y > 0:
                dy = self.world[0].rect.top - self.rect.bottom


        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > self.screen.get_height():
            self.rect.bottom = self.screen.get_height()
            dy = 550

        self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect, 2)