import pygame

class Hero():
    """A class for the main character."""

    def __init__(self, screen):
        """Initialize the Hero!"""
        self.screen = screen
        
        self.image = pygame.image.load('assets/images/knight.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        """Draws the hero!"""
        self.screen.blit(self.image, self.rect)
