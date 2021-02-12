import pygame

def runScore(screen, score):
    pygame.display.set_caption("Enregistrez votre score !")
    screen.fill((0,0,0))

    bg = pygame.image.load("images/congratulations.png")
    w, h = pygame.display.get_surface().get_size()

    input_text = ""
    input_box = pygame.Rect(w/2-200, h/2-25, 400, 50)
    font = pygame.font.Font("font/font_menu.ttf", 40)
    font_petit = pygame.font.Font("font/font_menu.ttf", 20)
    instruction1 = font_petit.render("Appuyez sur Entree pour valider votre pseudo", True, (255,255,255))
    instruction2 = font_petit.render("Ou sur Echap pour revenir au menu", True, (255,255,255))

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
        text_score = font.render("Score : "+str(score), True, (255,255,255))
        screen.blit(text_score, (input_box.x, input_box.y-100))
        screen.blit(instruction1, ((screen.get_width() - instruction1.get_rect().width) / 2, input_box.y+100))
        screen.blit(instruction2, ((screen.get_width() - instruction2.get_rect().width) / 2, input_box.y+200))
        pygame.draw.rect(screen, (230,230,230), input_box)
        text = font.render(input_text, True, (0,0,0))
        screen.blit(text, (input_box.x+5, input_box.y+5))
        pygame.display.flip()