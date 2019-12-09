import pygame


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1720
        self.screen_height = 960
        self.bg_color = (230, 230, 230)  # This could be removed if a background image exists
        self.bg_image = pygame.image.load('images\space.png')
        self.bg_rect = self.bg_image.get_rect()
