import pygame

pygame.init()

font = pygame.font.SysFont("Arial", 100)

class button:
    def __init__(self, x, y, text, active, screen):
        self.active = active
        self.text = font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.rect = pygame.Rect(x, y, self.size[0], self.size[1])
        self.screen = screen
        self.surface = pygame.Surface(self.size)


    def update(self):
        if self.active:
            self.surface.fill("red")
        else:
            self.surface.fill((0,0,0,0))
        self.surface.blit(self.text, (0, 0))
        self.screen.blit(self.surface, (self.rect.x, self.rect.y))

    def change_text(self, text):
        print(text)
        self.text = font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.rect.x, self.rect.y, self.size[0], self.size[1])

    def clear(self):
        self.change_text("                              ")
