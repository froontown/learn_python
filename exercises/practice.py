import sys
import pygame
from settings import Settings
from hero import Hero
import game_functions as gf

def run():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("BULLETS AND MOVEMENT XTREME")

    # Make the hero!
    hero = Hero(ai_settings, screen)

    # The game loop
    while True:

        gf.check_events(hero)
        hero.update()
        gf.update_screen(ai_settings, screen, hero)

        # Not going to refactor for the sake of practice.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()

        hero.blitme()

        pygame.display.flip()

run()
