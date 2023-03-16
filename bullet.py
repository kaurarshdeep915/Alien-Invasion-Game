import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    """Create a model of bullet for alien invasion game."""
    def __init__(self,ai_setting,screen,ship):
        """Initialize the attributes of bullets along with using attributes of Sprite."""
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0,ai_setting.bullet_width,ai_setting.bullet_height)
        self.rect.x = ship.rect.x + 33
        self.rect.y = ship.rect.y
        self.rect.top = ship.rect.top
        self.color = ai_setting.bullet_color
        self.speed = ai_setting.bullet_speed
        # To conver the integer position into floating point.
        self.y = float(self.rect.y)

    def update(self):
        """Update the position of bullet to show it moving."""
        self.y -= self.speed
        self.rect.y = self.y

    def draw(self):
        """To draw bullet on screen."""
        pygame.draw.rect(self.screen,self.color,self.rect)

