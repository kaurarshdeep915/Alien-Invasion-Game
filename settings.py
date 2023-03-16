class Settings():
    """Create a model of settings for game Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        self.screen_width = 1200
        self.screen_height = 630
        self.bg_color = (0,0,0)
        # SETTINGS FOR BULLETS
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0,0,255)
        self.bullet_allowed = 100
        # SETTINGS FOR ALIENS  
        self.aliens_direction = 1
        # SETTINGS FOR SUPER BULLET
        self.super_bullet_width = 300
        self.super_bullet_height = 10
        self.super_bullet_color = (255,0,0)
        self.super_bullet_allowed = 1
        # SETTINGS FOR SHIP
        self.ship_limit = 2
        #SETTIMGS FOR SCOREBOARD
        self.score_text_color = (255,255,255)
        # For dynamic values
        self.dynamic_values()
        # Rate at which the speed should increase after every level
        self.speedup_scale = 1.1
        # Rate at which the alien point increase.
        self.point_scaleup = 1.5

    def dynamic_values(self):
        """Values that change with level."""
        # speed of ship
        self.right_speed = 1
        self.left_speed = 0.2
        # Speed of aliens
        self.aliens_speed_x = 0.01
        self.aliens_speed_y = 5
        # Bullet speed
        self.bullet_speed = 1
        # Super Bullet speed
        self.super_bullet_speed = 1
        # Alien hit points
        self.alien_points = 50

    def increasing(self):
        """Increasing the speed after every level."""
         # speed of ship
        self.right_speed *= self.speedup_scale
        self.left_speed *= self.speedup_scale
        # Speed of aliens
        self.aliens_speed_x *= self.speedup_scale
        self.aliens_speed_y *= self.speedup_scale
        # Bullet speed
        self.bullet_speed *= self.speedup_scale
        # Super Bullet speed
        self.super_bullet_speed *= self.speedup_scale
        # Alien hit points
        self.alien_points = int(self.alien_points * self.point_scaleup)