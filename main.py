import pygame
from characterone import CharacterOne

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Times New Roman', 15)
pygame.display.set_caption("Street Fighter")

# set up variables for the display
size = (1024, 768)
screen = pygame.display.set_mode(size)
bg = pygame.image.load("background.png")

c1 = CharacterOne(500, 350)

run = True

while run:
    # --- Main event loop

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


    # blitting
    screen.blit(bg, (0, 0))
    screen.blit(c1.image, (200, 500))
    pygame.display.update()