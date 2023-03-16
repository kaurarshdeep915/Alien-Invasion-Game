import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """Create a model of alien."""
    def __init__(self,screen):
        """Initialize the attributes of alien along with Sprite."""
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = self.rect.width
        self.x = float(self.rect.x)
        self.rect.y = self.rect.height
        self.y = float(self.rect.y)

    def check_edge(self):
        if self.x >= self.screen_rect.right - 40:
            return True
        if self.x <= 0:
            return True

    def update(self,ai_setting):
        """Update the position of alien."""
        self.x += ai_setting.aliens_speed_x * ai_setting.aliens_direction
        self.rect.x = self.x

    def blitme(self):
        """To show the alien on screen."""
        self.screen.blit(self.image,self.rect)