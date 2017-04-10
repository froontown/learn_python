import sys
import pygame

def check_events(hero):
    """Checks to see if a key is pressed."""
    for event in pygame.event.get():
        if event.type == pygame.quit:
            sys.exit()

        # Let's make the dude run to the right!!!
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                hero.rect.centerx += 3

def update_screen(ai_settings, screen, hero):
    """Update the screen."""
    # Redraw the screen during each pass through the loop
    # screen.fill(ai_settings.bg_color)
    hero.blitme()

    # Display the most recently rendered screen
    pygame.display.flip()
