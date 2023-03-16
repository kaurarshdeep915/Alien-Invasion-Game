import pygame.font
class Button():
    """Create a model of button."""
    def __init__(self,screen,msg):
        """Initialize the attributes of button."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # set the dimensions of button.
        self.width, self.height = 200,50
        self.text_color = 255,255,255
        self.button_color = 0,255,0
        self.font = pygame.font.SysFont(None,48)
        # creating the button
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
        # Image msg on the button.
        self.image(msg)

    def image(self,msg):
        """msg image on the button."""
        self.image_msg = self.font.render(msg,True,self.text_color,self.button_color)
        self.image_msg_rect = self.image_msg.get_rect()
        self.image_msg_rect.center = self.rect.center

    def draw_button(self):
        """To draw the button on the game."""
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.image_msg,self.image_msg_rect)