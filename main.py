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
my_font2 = pygame.font.SysFont('Times New Roman', 20)
pygame.display.set_caption("Street Fighter")

# set up variables for the display
size = (1024, 768)
screen = pygame.display.set_mode(size)
bg = pygame.image.load("images/background.png")
bg = pygame.transform.scale(bg, (1024, 768))

welcome_message = "Welcome to Street Fighter"
instructions_message = "Player One: Use AD to move. E is attack and Q is block."
instructions_message2 = "Player Two: Use LEFT and RIGHT arrows to move. UP arrow to attack and DOWN arrow to block."
character_instructions1 = "Choose a character for player 1"
character_instructions2 = "Choose a character for player 2"

winning_message = "Game over! The winner is"
winner = "player"

kirby = Kirby(200, 600)
mario = Mario(300, 600)
p1_bar = PlayerOne(45, 650)
p2_bar = PlayerTwo(700, 650)


game_start = False
fight_start = False
p1_chosen = False
characters_determined = False
game_end = False

attack = False
p1_block = False
p2_block = False

p1_c1 = False
p1_c2 = False
p2_c1 = False
p2_c2 = False

p1_health = 100
p2_health = 100

# render the text for later
display_welcome_message = my_font1.render(welcome_message, True, (255, 255, 255))
display_instructions_message = my_font2.render(instructions_message, True, (255, 255, 255))
display_instructions2_message = my_font2.render(instructions_message2, True, (255, 255, 255))
display_character_instructions1 = my_font1.render(character_instructions1, True, (255, 255, 255))
display_character_instructions2 = my_font1.render(character_instructions2, True, (255, 255, 255))
display_winning_message = my_font1.render(winning_message, True, (255, 255, 255))


run = True

while run:

    # movement
    keys = pygame.key.get_pressed()  # checking pressed keys

    if fight_start:
        # if p1.x >= 100 and p1.x <= 800 and p2.x >= 100 and p2.x <= 800:
        if p1.x >= 100 and p1.x <= 800:
            # movement for player one
                if keys[pygame.K_d]:
                    p1.move_direction("right")
                if keys[pygame.K_a]:
                    p1.move_direction("left")

            # movement for player two
                if keys[pygame.K_RIGHT]:
                    p2.move_direction("right")
                if keys[pygame.K_LEFT]:
                    p2.move_direction("left")

        # attacking and blocking
        # player one block
        if keys[pygame.K_q]:
            # p1.ability("block")
            p1_block = True
        else:
            p1_block = False

        # player two block
        if keys[pygame.K_DOWN]:
            # p2.ability("block")
            p2_block = True
        else:
            p2_block = False

        if attack is False:
            # player one attack
            if keys[pygame.K_e]:
                if p1.rect.colliderect(p2.rect) and p2_block is False:
                    p2_health -= 25
                    attack = True
            # player two attack
            if keys[pygame.K_UP]:
                if p2.rect.colliderect(p1.rect) and p1_block is False:
                    p1_health -= 25
                    attack = True

        if attack:
            pygame.time.wait(1000)
            attack = False

        if p1_health == 0 or p2_health == 0:
            game_end = True
            if p1_health == 0:
                winner = "Player Two"
            if p2_health == 0:
                winner = "Player One"
            display_winner = my_font1.render(winner, True, (255, 255, 255))


    # character health bar
    p1_bar.health_bar(p1_health)
    p2_bar.health_bar(p2_health)


    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

        if fight_start is False:
            if characters_determined:
                if p1_c1:
                    p1 = Kirby(300, 500)
                if p1_c2:
                    p1 = Mario(300, 450)
                if p2_c1:
                    p2 = Kirby(700, 500)
                if p2_c2:
                    p2 = Mario(700, 450)
                fight_start = True

            else:
                if p1_chosen:
                    pos = pygame.mouse.get_pos()
                    if kirby.rect.collidepoint(pos):
                        if event.type == pygame.MOUSEBUTTONUP:
                            p2_c1 = True
                            characters_determined = True
                    if mario.rect.collidepoint(pos):
                        if event.type == pygame.MOUSEBUTTONUP:
                            p2_c2 = True
                            characters_determined = True


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
    if game_end is False:
        if game_start is False:
            screen.blit(display_welcome_message, (350, 300))
            screen.blit(display_instructions_message, (200, 350))
            screen.blit(display_instructions2_message, (50, 400))
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
                screen.blit(p1.image, (p1.x, p1.y))
                screen.blit(p2.image, (p2.x, p2.y))
    else:
        screen.fill((100, 100, 100))
        screen.blit(display_winning_message, (300, 200))
        screen.blit(display_winner, (400, 300))

    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()