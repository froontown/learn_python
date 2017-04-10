import sys
import pygame
from settings import Settings
from hero import Hero

def run():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("BULLETS AND MOVEMENT XTREME")

    # Make the hero!
    hero = Hero(screen)

    # The game loop
    while True:

        # Not going to refactor for the sake of practice.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()

        # I don't really need this cuz it defaults to black by just in case.
        # screen.fill(bg_color)

        hero.blitme()

        pygame.display.flip()

run()
