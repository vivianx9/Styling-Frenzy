import pygame
from characterone import CharacterOne
from charactertwo import C2

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

welcome_message = "Welcome to Street Fighter"
instructions_message = "Use WASD to move. Ability keys are E and Q"

c1 = CharacterOne(500, 350)
c2 = C2(800, 350)

game_start = False

# render the text for later
display_welcome_message = my_font1.render(welcome_message, True, (255, 255, 255))
display_instructions_message = my_font1.render(instructions_message, True, (255, 255, 255))

run = True

while run:

    # movement
    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_d]:
        c1.move_direction("right")
    if keys[pygame.K_a]:
        c1.move_direction("left")
    if keys[pygame.K_s]:
        c1.move_direction("down")
    if keys[pygame.K_w]:
        c1.move_direction("up")


    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

        if event.type == pygame.MOUSEBUTTONUP:
            game_start = True

    # blitting
    # screen.fill((100, 100, 100))
    if game_start is False:
        screen.blit(display_welcome_message, (350, 300))
        screen.blit(display_instructions_message, (300, 350))
    else:
        screen.blit(bg, (0, 0))
        screen.blit(c1.image, (200, 500))
        screen.blit(c2.image, (400, 500))
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()