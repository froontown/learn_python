import pygame

class Hero():
    """A class for the main character."""

    def __init__(self, ai_settings, screen):
        """Initialize the Hero!"""
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('assets/images/knight.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.moving_right = False

    def update(self):
        """Going to check the movement of the hero."""
        if self.moving_right:
            self.rect.centerx += 1

    def blitme(self):
        """Draws the hero!"""
        self.screen.blit(self.image, self.rect)
