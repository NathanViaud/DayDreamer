import pygame

def runScore(screen):
    pygame.display.set_caption("Enregistrez votre score !")
    screen.fill((0,0,0))

    bg = pygame.image.load("images/congratulations.png")
    w, h = pygame.display.get_surface().get_size()

    input_text = ""
    input_box = pygame.Rect(w/2-200, h/2-25, 400, 50)
    font = pygame.font.Font("font/font_menu.ttf", 40)

    loop = True

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = False
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    loop = False
                    return input_text
                else:
                    input_text += event.unicode
            elif event.type == pygame.QUIT:
                loop = False
        screen.blit(bg, (0,0))
        pygame.draw.rect(screen, (230,230,230), input_box)
        text = font.render(input_text, True, (0,0,0))
        screen.blit(text, (input_box.x+5, input_box.y+5))
        pygame.display.flip()