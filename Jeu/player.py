import pygame

from plateforme import *
from fond import *

class player():
    def __init__(self, x ,y, screen, world):
        img = pygame.image.load("sprites/idle.png")
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
        self.fond = fond

    def update(self):
        
        w, h = pygame.display.get_surface().get_size()
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False:
            self.vel_y = -10
            self.jumped = True
        if key[pygame.K_SPACE] == False:
            self.jumped = False
        if key[pygame.K_LEFT]:
            if self.rect.x <= w/2:
                self.world.gauche(2)
            else:
                dx -= 2
        if key[pygame.K_RIGHT]:
            if self.rect.x >= w/2:
                self.world.droite(2)
            else:
                dx += 2
        

        self.vel_y += 0.1
        if self.vel_y > 2:
            self.vel_y = 2
        dy += self.vel_y


        for plateforme in self.world.plateformes:
            if plateforme.rect.colliderect(self.rect.x, self.rect.y+dy, self.width, self.height):
                if self.vel_y < 0:
                    dy = plateforme.rect.bottom - self.rect.top
                if self.vel_y > 0:
                    dy = plateforme.rect.top - self.rect.bottom
        for fruit in self.world.fruits:
            if fruit.rect.colliderect(self.rect.x, self.rect.y, self.width, self.height):
                self.world.removeFruit(fruit)

        for ennemi in self.world.ennemis:
            if ennemi.rect.colliderect(self.rect.x, self.rect.y, self.width, self.height):
                print("touché")


        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > self.screen.get_height():
            self.rect.bottom = self.screen.get_height()
            dy = 550

        self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect, 2)