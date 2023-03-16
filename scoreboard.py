import pygame
from pygame.sprite import Group
from ship import Ship
class Scoreboard():
    """Create a model for scoreboadr."""
    def __init__(self,screen,ai_setting,stats):
        """Initialize the attributes of scoreboad for the game."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_setting = ai_setting
        self.stats = stats

        # Scoreboard font and text color
        self.font = pygame.font.SysFont(None,32)
        self.text_color = self.ai_setting.score_text_color
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ship()

        
    def prep_score(self):
        """Prepare the score on scoreboard."""
        round_value = round(self.stats.score,-1)
        score_str = "Score: " + "{:,}".format(round_value)
        self.text_image = self.font.render(score_str,True,self.text_color,self.ai_setting.bg_color)
        self.image_rect = self.text_image.get_rect()
        self.image_rect.right = self.screen_rect.right -20
        self.image_rect.top = 20

    def prep_high_score(self):
        """Prepare the high score value."""
        round_high_score = round(self.stats.high_score,-1)
        high_score_str = "Highest score: " + "{:,}".format(round_high_score)
        self.highscore_text_image = self.font.render(high_score_str,True,
                                                     self.ai_setting.score_text_color,self.ai_setting.bg_color)
        self.highscore_rect = self.highscore_text_image.get_rect()
        self.highscore_rect.x = self.screen_rect.centerx - 100
        self.highscore_rect.top = self.image_rect.top

    def prep_level(self):
        """Prepare the levels of game."""
        level = "Level: " + str(self.stats.level)
        self.level_image = self.font.render(level,True,self.ai_setting.score_text_color
                                            ,self.ai_setting.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.screen_rect.left + 10
        self.level_rect.top = self.image_rect.top

    def prep_ship(self):
        """Prepare the count of ships on the screen."""
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.screen,self.ai_setting)
            ship.rect.x = self.screen_rect.left + 10 + ship_number * ship.rect.width
            ship.rect.y = 500
            self.ships.add(ship)


    def show_score(self):
        """To show the score on the screen."""
        self.screen.blit(self.text_image,self.image_rect)
        self.screen.blit(self.highscore_text_image,self.highscore_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)