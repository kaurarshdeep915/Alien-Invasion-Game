import pygame
import math
from pygame.sprite import Sprite
class Ship(Sprite):
    """Create a model of ship for Alien Invasion game."""

    def __init__(self,screen,ai_setting):
        """Initialize the image of ship on sthe screen."""
        super().__init__()
        self.screen = screen
        self.ai_setting = ai_setting

        # Upload the image of ship.
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()    
        self.screen_rect = screen.get_rect()
        # Adjusting the position of image.
        self.rect.x = 550
        self.rect.y = 480

        # Attribute to show the whether the right key is pressed or not.
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Update the position of ship if the key is pressed."""
        if self.moving_right == True and self.rect.left < 1100:
            self.rect.x += self.ai_setting.right_speed
        if self.moving_left == True and self.rect.left > 0:
            self.rect.x -= self.ai_setting.left_speed

    def center_ship(self):
        """To center the ship on the screen."""
        self.center = self.screen_rect.centerx


    def blitme(self):
        """Draw the ship at the location mentioned previously."""
        self.screen.blit(self.image,self.rect)
