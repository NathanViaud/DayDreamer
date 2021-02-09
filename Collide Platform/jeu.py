import pygame
from Player import *
from platform import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

size = (1024, 768)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("DayDreamer")
bg_img = pygame.image.load('images/fond.png')

joue = True
world = []
platform = Platform(200, 450, screen)
world.append(platform)
player = Player(100, 550, screen, world)
while joue:

    clock.tick(fps)
    screen.blit(bg_img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            joue = False

    player.update()
    platform.update()
    pygame.time.wait(1)
    pygame.display.update()
pygame.quit()
