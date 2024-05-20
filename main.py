import pygame
from kirby import Kirby
from mario import Mario
from player_one import PlayerOne
from player_two import PlayerTwo

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Times New Roman', 15)
my_font1 = pygame.font.SysFont('Times New Roman', 30)
pygame.display.set_caption("Street Fighter")

# set up variables for the display
size = (1024, 768)
screen = pygame.display.set_mode(size)
bg = pygame.image.load("images/background.png")
bg = pygame.transform.scale(bg, (1024, 768))

welcome_message = "Welcome to Street Fighter"
instructions_message = "Use WASD to move. Ability keys are E and Q"
character_instructions1 = "Choose a character for player 1"
character_instructions2 = "Choose a character for player 2"

kirby = Kirby(200, 600)
mario = Mario(300, 600)
p1_bar = PlayerOne(45, 650)
p2_bar = PlayerTwo(700, 650)


game_start = False
fight_start = False
p1_chosen = False
characters_determined = False

p1_c1 = False
p1_c2 = False
p2_c1 = False
p2_c2 = False

p1_health = 100
p2_health = 100

# render the text for later
display_welcome_message = my_font1.render(welcome_message, True, (255, 255, 255))
display_instructions_message = my_font1.render(instructions_message, True, (255, 255, 255))
display_character_instructions1 = my_font1.render(character_instructions1, True, (255, 255, 255))
display_character_instructions2 = my_font1.render(character_instructions2, True, (255, 255, 255))


run = True

while run:

    # movement
    keys = pygame.key.get_pressed()  # checking pressed keys

    if kirby.x >= 100 and kirby.x <= 800 and mario.x >= 100 and mario.x <= 800:
        # movement for player one
        if p1_c1:
            if keys[pygame.K_d]:
                kirby.move_direction("right")
            if keys[pygame.K_a]:
                kirby.move_direction("left")

        elif p1_c2:
            if keys[pygame.K_d]:
                mario.move_direction("right")
            if keys[pygame.K_a]:
                mario.move_direction("left")

        # movement for player two
        if p2_c1:
            if keys[pygame.K_RIGHT]:
                kirby.move_direction("right")
            if keys[pygame.K_LEFT]:
                kirby.move_direction("left")

        elif p2_c2:
            if keys[pygame.K_RIGHT]:
                mario.move_direction("right")
            if keys[pygame.K_LEFT]:
                mario.move_direction("left")

    elif kirby.x < 100:
        kirby.x = 100

    elif kirby.x > 800:
        kirby.x = 800

    elif mario.x < 100:
        mario.x = 100

    elif mario.x > 800:
        mario.x = 800


    # character health
    if p1_health == 100:
        p1_bar.health_bar(100)
    elif p1_health == 75:
        p1_bar.health_bar(75)
    elif p1_health == 50:
        p1_bar.health_bar(50)
    elif p1_health == 25:
        p1_bar.health_bar(25)
    elif p1_health == 0:
        p1_bar.health_bar(0)

    if p2_health == 100:
        p2_bar.health_bar(100)
    elif p2_health == 75:
        p2_bar.health_bar(75)
    elif p2_health == 50:
        p2_bar.health_bar(50)
    elif p2_health == 25:
        p2_bar.health_bar(25)
    elif p2_health == 0:
        p2_bar.health_bar(0)


    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

        if event.type == pygame.MOUSEBUTTONUP and game_start and p1_chosen:
            fight_start = True


        if characters_determined is False:
            if fight_start:
                if p1_c1:
                    kirby = Kirby(300, 500)
                if p1_c2:
                    mario = Mario(300, 450)
                if p2_c1:
                    kirby = Kirby(700, 500)
                if p2_c2:
                    mario = Mario(700, 450)
                characters_determined = True

            if fight_start is False:
                if p1_chosen:
                    pos = pygame.mouse.get_pos()
                    if kirby.rect.collidepoint(pos):
                        if event.type == pygame.MOUSEBUTTONUP:
                            p2_c1 = True
                            fight_start = True
                    if mario.rect.collidepoint(pos):
                        if event.type == pygame.MOUSEBUTTONUP:
                            p2_c2 = True
                            fight_start = True

                else:
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
            screen.blit(p1_bar.image, (p1_bar.x, p1_bar.y))
            screen.blit(p2_bar.image, (p2_bar.x, p2_bar.y))
            if p1_c1:
                # kirby = Kirby(300, 600)
                screen.blit(kirby.image, (kirby.x, kirby.y))
            if p1_c2:
                # mario = Mario(300, 600)
                screen.blit(mario.image, (mario.x, mario.y))
            if p2_c1:
                # kirby = Kirby(700, 600)
                screen.blit(kirby.image, (kirby.x, kirby.y))
            if p2_c2:
                # mario = Mario(700, 600)
                screen.blit(mario.image, (mario.x, mario.y))
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()