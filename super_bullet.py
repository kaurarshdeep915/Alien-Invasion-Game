import pygame
from pygame.sprite import Sprite
class Super_bullet(Sprite):
    """Create a model for super bullet."""
    def __init__(self,screen,ai_setting,ship):
        """Initialize the attributes of super bullet and sprite."""
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0,ai_setting.super_bullet_width,ai_setting.super_bullet_height)
        self.screen_rect = screen.get_rect()
        self.rect.x = ship.rect.x
        self.rect.y = ship.rect.y
        self.rect.top = ship.rect.top
        self.rect.centerx = ship.rect.centerx
        self.y = float(self.rect.y)
        self.speed = ai_setting.super_bullet_speed
        self.color = ai_setting.super_bullet_color

    def update(self):
        """Update the position of super bullet."""
        self.y -= self.speed
        self.rect.y = self.y

    def draw(self):
        """Draw the super bullet on the screen."""
        pygame.draw.rect(self.screen,self.color,self.rect)
