import sys
import pygame
from bullet import Bullet
from alien import Alien
from super_bullet import Super_bullet
from time import sleep

def fire_bullet(bullet,ai_setting,screen,ship):
    """Function shows the condition for when will be a new bullet fired."""
    if len(bullet) < ai_setting.bullet_allowed:
            new_bullet = Bullet(ai_setting,screen,ship)
            bullet.add(new_bullet)
    else:
        pass

def fire_super_bullet(screen,super_bullet,ai_setting,ship):
    """To fire super bullet."""
    if len(super_bullet) < ai_setting.super_bullet_allowed:
        new_super_bullet = Super_bullet(screen,ai_setting,ship)
        super_bullet.add(new_super_bullet)
    else:
        pass

def check_keydown_event(event,super_bullet,ship,ai_setting,screen,bullet,stats,aliens):
    """Respond to keypress."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(bullet,ai_setting,screen,ship)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_s:
        fire_super_bullet(screen,super_bullet,ai_setting,ship)
    elif event.key == pygame.K_p:
        start_game(stats,aliens,bullet,super_bullet,ship,screen,ai_setting)

def check_keyup_event(event,ship):
    """Respond to key release."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship,ai_setting,screen,bullet,super_bullet,play_button,stats,aliens,sb):
    """To check the event and call accordingly."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event,super_bullet,ship,ai_setting,screen,bullet,stats,aliens)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            click_position(play_button,mouse_x,mouse_y,stats,aliens,bullet,
                   super_bullet,screen,ai_setting,ship,sb)

def start_game(stats,aliens,bullet,super_bullet,ship,screen,ai_setting,sb):
    """To satrt the game."""
    pygame.mouse.set_visible(False)
    stats.game_active = True
    stats.game_reset()
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ship()
    # Reset the bullets and aliens group.
    aliens.empty()
    bullet.empty()
    super_bullet.empty()
    # reset fleet and ship position.
    alien_fleet(screen,ai_setting,aliens,ship)
    ship.center_ship()


def click_position(play_button,mouse_x,mouse_y,stats,aliens,bullet,
                   super_bullet,screen,ai_setting,ship,sb):
    """Check the position of mouse."""
    if play_button.rect.collidepoint(mouse_x,mouse_y) and stats.game_active == False:
        start_game(stats,aliens,bullet,super_bullet,ship,screen,ai_setting,sb)


def number_of_alien_x(screen,ai_setting,alien_width):
    """Get the number of aliens can be aligned on a row."""
    alien = Alien(screen)
    available_space_x = ai_setting.screen_width - (2 * alien_width)
    number_of_aliens = int(available_space_x / (2 * alien_width))
    return number_of_aliens

def number_of_rows(ai_setting,ship_height,alien_height):
    """Find the number of rows of alien can be created in the game."""
    available_space_y = ai_setting.screen_height - (3 * alien_height) - ship_height
    number_of_alien_y = int(available_space_y / (2 * alien_height))
    return number_of_alien_y

def create_alien(screen,aliens,alien_number_x,alien_width,alien_height,row_number):
    """Create alein for game."""
    alien = Alien(screen)
    alien_width = alien.rect.width
    alien.rect.x = alien.x = alien_width + 2 * alien_number_x * alien_width
    alien.rect.y = alien.y = 2 * alien_height + 2 * row_number * alien_height
    aliens.add(alien)

def alien_fleet(screen,ai_setting,aliens,ship):
    """Create alein fleet."""
    alien = Alien (screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    ship_height = ship.rect.height
    number_of_alien = number_of_alien_x(screen,ai_setting,alien_width)
    number_rows = number_of_rows(ai_setting,ship_height,alien_height)

    for row_number in range(number_rows):  
        for alien_number_x in range(number_of_alien):
            create_alien(screen,aliens,alien_number_x,alien_width,alien_height,row_number)

def update_screen(bg_color,screen,ship,bullet,aliens,super_bullet,stats,play_button,sb):
    """Update the screen while going through loop."""
    screen.fill(bg_color)
    ship.blitme()
    for bullet_1 in bullet.sprites():
        bullet_1.draw()
    for bullet in super_bullet.sprites():
        bullet.draw()
    aliens.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()

def check_high_score(stats,sb):
    """Check high score value comparison to current score."""
    if stats.high_score < stats.score:
        stats.high_score = stats.score
        sb.prep_high_score()


def update_bullet(bullet,aliens,screen,ai_setting,ship,stats,sb):
    """update the position of bullet and remove the unwanted bullets from memory."""
    bullet.update()
    # To check bullet alien collision
    check_bullet_alien_collision(bullet,aliens,screen,ai_setting,ship,stats,sb)

def check_bullet_alien_collision(bullet,aliens,screen,ai_setting,ship,stats,sb):
    # To remove bullet.
    for bullet_1 in bullet.copy():
        if bullet_1.rect.y <= 0:
            bullet.remove(bullet_1)
    # collide bullet with alien and remove both correspondingly.
    collision = pygame.sprite.groupcollide(bullet,aliens,True,True)
    # Increase the score corresponding to the aliens hit by bullet.
    if collision:
        for aliens in collision.values():
            stats.score += ai_setting.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)
    # recreating the fleet of aliens
    for bullet_1 in bullet.sprites():
        if len(aliens) == 0:
            bullet.empty()
            ai_setting.increasing()
            stats.level += 1
            sb.prep_level()
            alien_fleet(screen,ai_setting,aliens,ship)

def update_super_bullet(super_bullet,aliens,screen,ai_setting,ship,stats,sb):
    """Update the position of super bullet."""
    super_bullet.update()
    # function for alien bullet collision.
    check_super_bullet_alien_collision(super_bullet,aliens,screen,ai_setting,ship,stats,sb)

def check_super_bullet_alien_collision(super_bullet,aliens,screen,ai_setting,ship,stats,sb):
    # To remove the super_bullet after it cross the screen top.
    for bullet in super_bullet.copy():
        if bullet.rect.y <= 0:
            super_bullet.remove(bullet)
    # Remove the aliens after collision.
    collision = pygame.sprite.groupcollide(super_bullet,aliens,False,True)
    # Increase the score after collision between super bullet and aliens.
    if collision:
        for aliens in collision.values():
            stats.score += ai_setting.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)
    # recreating the fleet of aliens
    for superbullet in super_bullet.sprites():
        if len(aliens) == 0:
            super_bullet.empty()
            ai_setting.increasing()
            stats.level += 1
            sb.prep_level()
            alien_fleet(screen,ai_setting,aliens,ship)


def change_fleet_direction(aliens,ai_setting):
    """change the direction of fleet after it reaches the edge."""
    for alien in aliens.sprites():
        alien.y += ai_setting.aliens_speed_y
        alien.rect.y = alien.y
    ai_setting.aliens_direction *= -1

def check_fleet_edge(aliens,ai_setting):
    """Check the fleet edge and change the direction."""
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(aliens,ai_setting)

def ship_hit(stats,aliens,bullet,screen,ai_setting,ship,sb):
    """Changes when a ship is hit by alien."""
    if stats.ship_left > 0:
        stats.ship_left -= 1
        # Empty the group of aliens and fleet.
        aliens.empty()
        bullet.empty()
        # create a fleet of aliens and center the ship.
        alien_fleet(screen,ai_setting,aliens,ship)
        ship.center_ship()
        # Update the count of ships on the screen
        sb.prep_ship()
        # pause the time for few seconds.
        sleep(0.5)
    else:
        stats.game_active = False
        ai_setting.dynamic_values()
        pygame.mouse.set_visible(True)

def update_aliens(aliens,ai_setting,ship,stats,bullet,screen,sb):
    """Update the position of aliens."""
    for alien in aliens.sprites():
        check_fleet_edge(aliens,ai_setting)
        aliens.update(ai_setting)
    # To check alien and ship collision.
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(stats,aliens,bullet,screen,ai_setting,ship,sb)
    # If alien hit the bottom of screen.
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(stats,aliens,bullet,screen,ai_setting,ship,sb)