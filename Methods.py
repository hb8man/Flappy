import pygame
from Obstacle import Obstacle
import random

# Adds two obstacle sprites from random int
def spawn_obstacle(obstacle_group):
    """Selects obstacle to spawn.

    Randomly selects from 3 different obstacle orientations, and
    adds it to the obstacle group when the obstacle timer is called.
    """
    random_number = random.randint(1,3)
    if random_number == 1:
        obstacle_group.add(Obstacle(1))
        obstacle_group.add(Obstacle(2))
    if random_number == 2:
        obstacle_group.add(Obstacle(3))
        obstacle_group.add(Obstacle(4))
    if random_number == 3:
        obstacle_group.add(Obstacle(5))
        obstacle_group.add(Obstacle(6))

# Formats and returns score
def display_score(start_time, screen):
    """ Displays seconds lasted during game.

    Displays total time in game since game loop started to display
    player score. 
    """
    try:
        font = 'font/Pixeltype.ttf'
        game_font = pygame.font.Font(font, 50)
    except IOError:
        print(f'{font} not found.')
        pygame.quit()
        exit()        
        
    current_time = int(pygame.time.get_ticks()) - start_time
    score_surf = game_font.render(f"{int(current_time/1000)}",False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return current_time