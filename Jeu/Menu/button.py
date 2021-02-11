import pygame

pygame.init()

font = pygame.font.Font("font/font_menu.ttf", 50)
font_lancement = pygame.font.Font("font/font_menu.ttf", 30)

pygame.font.init()

bg = pygame.image.load("images/menu/menu4.png")

Black = (42,42,87)

class button:
    def __init__(self, x, y, text, active, screen):
        self.active = active
        self.text = font.render(text, True, Black)
        self.size = self.text.get_size()
        self.rect = pygame.Rect(x, y, self.size[0], self.size[1])
        self.screen = screen
        self.surface = pygame.Surface(self.size)
        self.contenu = text


    def update(self):
        if self.active:
            self.text = font.render(self.contenu, True, (116,116,116))
            pygame.draw.rect(self.screen, Black, pygame.Rect(self.rect.x - 10, self.rect.y, self.size[0] + 20, self.size[1] + 10), 2)
        elif self.contenu == "Lancement de la partie":
            self.text = font_lancement.render(self.contenu, True, (116,116,116))
        else:
            self.text = font.render(self.contenu, True, Black)
        self.screen.blit(self.text, (self.rect.x, self.rect.y))

    def change_text(self, text):
        self.active = False
        self.contenu = text
        self.update()
        self.size = self.text.get_size()
        self.rect.size = self.size
        self.rect.x = (self.screen.get_width() - self.rect.width) / 2
        self.rect.y = (self.screen.get_height() - self.rect.height + 50) / 2

    def clear(self):
        self.contenu = "        "
        self.screen.blit(self.text, (self.rect.x, self.rect.y))
        self.screen.blit(bg, (0,0))