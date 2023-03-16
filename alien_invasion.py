import pygame
import os
import game_functions as gf
os.chdir('alien_invasion\image')
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStat
from button import Button
from scoreboard import Scoreboard
def run_game():
    """Initialize the game, settings and create a screen object."""
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(screen,ai_setting)
    bullet = Group()
    aliens = Group()
    play_button = Button(screen,'Play')
    gf.alien_fleet(screen,ai_setting,aliens,ship)
    super_bullet = Group()
    stats = GameStat(ai_setting)
    sb = Scoreboard(screen,ai_setting,stats)

    # Start the main loop for the game.
    while True:
        gf.check_events(ship,ai_setting,screen,bullet,super_bullet,play_button,stats,aliens,sb)
        if stats.game_active:
            ship.update()  
            gf.update_bullet(bullet,aliens,screen,ai_setting,ship,stats,sb)
            gf.update_super_bullet(super_bullet,aliens,screen,ai_setting,ship,stats,sb)
            gf.update_aliens(aliens,ai_setting,ship,stats,bullet,screen,sb)
        gf.update_screen(ai_setting.bg_color,screen,ship,bullet,aliens,super_bullet,stats,play_button,sb)

run_game()