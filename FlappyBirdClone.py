import pygame
from pygame.locals import * 
import sys

# can resize if needed
window_width = 500
window_height = 300

# Want ground to be a little above lower portion of screen
ground = 250

window = pygame.display.set_mode((window_width, window_height))
# Bird sprite subject to change
bird = pygame.image.load("bird_test_sprite.png")

def flappygame():

    # Bird location at start
    bird_x = 50
    bird_y = 100

    # Moves bird up and down, value changes based on user action
    bird_y_change = 0

    while True:

        for event in pygame.event.get():
            # Esc to quit program
            if event.type == KEYDOWN  and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            # Up arrow to move up, else affected by gravity
            # Speeds can be adjusted; will depend on screen size
            if event.type == KEYDOWN and event.key == K_UP:
                bird_y_change = -.05
            else:
                bird_y_change = .025

        # Applies change in Y
        bird_y += bird_y_change

        # Upper and Lower Boundaries for Bird on Screen
        if bird_y <= 0:
            bird_y = 0
        if bird_y >= ground:
            bird_y = ground

        window.fill((0,0,0)) # Will be switched with background
        # Regenerates bird with new position
        window.blit(bird, (bird_x, bird_y))

        pygame.display.update() 
        
def main():
    pygame.init()
    while True:
        for event in pygame.event.get(): 
            # Quits game if escape pressed
            if event.type == QUIT or (
                event.type == KEYDOWN  and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            # Starts game if space pressed
            elif event.type == KEYDOWN and event.key == K_SPACE:
                flappygame()
            else:
                pygame.display.update()
            

if __name__ == "__main__":
    main()