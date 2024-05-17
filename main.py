import pygame
from kirby import Kirby
from mario import Mario

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Times New Roman', 15)
my_font1 = pygame.font.SysFont('Times New Roman', 30)
pygame.display.set_caption("Street Fighter")

# set up variables for the display
size = (1024, 768)
screen = pygame.display.set_mode(size)
bg = pygame.image.load("background.png")
bg = pygame.transform.scale(bg, (1024, 768))

welcome_message = "Welcome to Street Fighter"
instructions_message = "Use WASD to move. Ability keys are E and Q"
character_instructions1 = "Choose a character for player 1"
character_instructions2 = "Choose a character for player 2"

kirby = Kirby(300, 600)
mario = Mario(300, 600)



game_start = False
fight_start = False
p1_chosen = False

p1_c1 = False
p1_c2 = False
p2_c1 = False
p2_c2 = False

# render the text for later
display_welcome_message = my_font1.render(welcome_message, True, (255, 255, 255))
display_instructions_message = my_font1.render(instructions_message, True, (255, 255, 255))
display_character_instructions1 = my_font1.render(character_instructions1, True, (255, 255, 255))
display_character_instructions2 = my_font1.render(character_instructions2, True, (255, 255, 255))


run = True

while run:

    # movement
    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_d]:
        kirby.move_direction("right")
    if keys[pygame.K_a]:
        kirby.move_direction("left")
    if keys[pygame.K_s]:
        kirby.move_direction("down")
    if keys[pygame.K_w]:
        kirby.move_direction("up")

    if keys[pygame.K_RIGHT]:
        mario.move_direction("right")
    if keys[pygame.K_LEFT]:
        mario.move_direction("left")
    if keys[pygame.K_DOWN]:
        mario.move_direction("down")
    if keys[pygame.K_UP]:
        mario.move_direction("up")


    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

        if event.type == pygame.MOUSEBUTTONUP and game_start and p1_chosen:
            fight_start = True

        # if event.type == pygame.MOUSEBUTTONUP and fight_start is False and p1_chosen:
        #     pos = pygame.mouse.get_pos()
        #     if kirby.rect.collidepoint(pos):
        #         p2_c1 = True
        #         print(p2_c1)
        #         fight_start = True
        #     if mario.rect.collidepoint(pos):
        #         p2_c2 = True
        #         fight_start = True

        if fight_start is False and p1_chosen:
            pos = pygame.mouse.get_pos()
            if kirby.rect.collidepoint(pos):
                if event.type == pygame.MOUSEBUTTONUP:
                    p2_c1 = True
                    print(p2_c1)
                    fight_start = True
            if mario.rect.collidepoint(pos):
                if event.type == pygame.MOUSEBUTTONUP:
                    p2_c2 = True
                    fight_start = True



        # if event.type == pygame.MOUSEBUTTONUP and fight_start is False and p1_chosen is False:
        #     pos = pygame.mouse.get_pos()
        #     if kirby.rect.collidepoint(pos):
        #         p1_c1 = True
        #         print(p1_c1)
        #         p1_chosen = True
        #     if mario.rect.collidepoint(pos):
        #         p1_c2 = True
        #         p1_chosen = True

        if fight_start is False and p1_chosen is False:
            pos = pygame.mouse.get_pos()
            if kirby.rect.collidepoint(pos):
                if event.type == pygame.MOUSEBUTTONUP:
                    p1_c1 = True
                    p1_chosen = True
            if mario.rect.collidepoint(pos):
                if event.type == pygame.MOUSEBUTTONUP:
                    p1_c2 = True
                    p1_chosen = True


        if event.type == pygame.MOUSEBUTTONUP:
            game_start = True


    # blitting
    # screen.fill((100, 100, 100))
    if game_start is False:
        screen.blit(display_welcome_message, (350, 300))
        screen.blit(display_instructions_message, (300, 350))
    else:
        if fight_start is False:
            screen.fill((100, 100, 100))
            screen.blit(kirby.image, (200, 600))
            screen.blit(mario.image, (350, 600))
            if p1_chosen is False:
                screen.blit(display_character_instructions1, (300, 200))
            else:
                screen.blit(display_character_instructions2, (300, 200))
        else:
            screen.blit(bg, (0, 0))
            if p1_c1:
                kirby = Kirby(300, 600)
                screen.blit(kirby.image, (kirby.x, kirby.y))
            if p1_c2:
                mario = Mario(300, 600)
                screen.blit(mario.image, (mario.x, mario.y))
            if p2_c1:
                kirby = Kirby(700, 600)
                screen.blit(kirby.image, (kirby.x, kirby.y))
            if p2_c2:
                mario = Mario(700, 600)
                screen.blit(mario.image, (mario.x, mario.y))
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()