class GameStat():
    """"Create a model for observing game statistics."""
    
    def __init__(self,ai_setting):
        """Initialize the attributes ot be determined in game statistics."""
        self.ai_setting = ai_setting
        self.game_reset()
        self.game_active = False
        self.high_score = 0

    def game_reset(self):
        """Resent the game state."""
        self.ship_left = self.ai_setting.ship_limit
        self.score = 0
        self.level = 1
