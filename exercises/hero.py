import pygame

class Hero():
    """A class for the main character."""

    def __init__(self, ai_settings, screen):
        """Initialize the Hero!"""
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('assets/images/knight.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # Movement flags
        self.moving_right = False
        self.moving_left = False

        # For the decimals in hero's speed:
        self.center = float(self.rect.centerx)

    def update(self):
        """Going to check the movement of the hero."""
        if self.moving_right:
            self.center += self.ai_settings.hero_speed_factor

        if self.moving_left:
            self.center -= self.ai_settings.hero_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draws the hero!"""
        self.screen.blit(self.image, self.rect)
