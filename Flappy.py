"""Flappy.py
Authors: Vicky Singharaj, Katarina Schoening, W. Bateman
Date Completed: 12/3/2023

Description: This is a flappy bird type game made with pygame using Python
the user can enter their name to have their score and name displayed after they play. 
The user can opt to play again or click the 'x' to exit. 
"""

# TODO: Docstring for funcitons (classes and methods)
# TODO: When opening file, use Try / Exept


import pygame
import random
from Obstacle import Obstacle
from Player import Player
from Methods import spawn_obstacle
from Methods import display_score

    
# Initialize pygame
pygame.init()

# Initial variables
game_state = "start_menu"
start_time = 0
score = 0
text_input = ''
collision_sound = pygame.mixer.Sound('audio/metal-pipe-falling-sound-effect-made-with-Voicemod-technology.mp3')

# Set up screen
screen = pygame.display.set_mode((800, 600))

# Set window caption
pygame.display.set_caption("Flappy")

# Clock object to control framerate
clock = pygame.time.Clock()

# Init player group
player = pygame.sprite.GroupSingle()
loaded_player = player.add(Player())

# Init obstacle group
obstacle_group = pygame.sprite.Group()

# Background Surfaces
sky_surface = pygame.image.load('Graphics/Sky.png').convert_alpha()

sky_surface_top = pygame.Surface(size = (800, 300))
sky_surface_top.fill(color = "#D7F3F6") # Light blue color
ground_surface = pygame.image.load('Graphics/Ground.png').convert_alpha()
ground_rect = ground_surface.get_rect(topleft = (0,500))

# Obstacle timer
# TODO: Explain this more
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 850)

# Game loop
while True:
    # Checking event loop for game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_state == "game_loop":
            # Spawn obstacle when timer goes off
            if event.type ==  obstacle_timer:
                spawn_obstacle(obstacle_group = obstacle_group)
        # Begin game loop state when space pressed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if len(text_input) > 0:
                game_state = "game_loop"
        # Handle user text input for name
        if event.type == pygame.KEYDOWN and event.key != pygame.K_SPACE:
            if event.key == pygame.K_BACKSPACE:
                text_input = text_input[:-1]
                break
            else:
                # Add input to str if input is valid
                if event.unicode.isalpha() == True:
                    if len(text_input) <= 15:
                        text_input += event.unicode


    # Updates screen
    pygame.display.update()
    
    # Start menu state
    if game_state == "start_menu":
        game_font = pygame.font.Font('font/Pixeltype.ttf', 50)
        screen.fill('#D7F3F6')
        # Title
        title_surf = game_font.render(f"Welcome to Flappy",False,(64,64,64))
        title_rect = title_surf.get_rect(center = (400,150))
        screen.blit(title_surf,title_rect)
        # Start game prompt
        start_surf = game_font.render(f"Press SPACE to start",False,(64,64,64))
        start_rect = start_surf.get_rect(center = (400,500))
        screen.blit(start_surf,start_rect)

        # Name input prompt
        prompt_surf = game_font.render("Enter name", True, "black")
        screen.blit(prompt_surf, (315,300))
        
        # Text input surface
        text_surf = game_font.render(text_input, True, "black")
        screen.blit(text_surf, (315,350))
        
        # Reset clock for starting game
        start_time = pygame.time.get_ticks()


    elif game_state == "game_loop":
        # Enter main game loop state

        # Render background objects
        screen.blit(sky_surface_top, (0,0))
        screen.blit(sky_surface, (0,200))
        screen.blit(ground_surface, ground_rect)

        # Draw player sprite class & update every tick
        player.draw(screen)
        player.update()

        # Draw obstacle sprite class & update every tick
        obstacle_group.draw(screen)
        obstacle_group.update()

        # Enter endgame state when player sprite collides with obstacle sprite class
        if pygame.sprite.groupcollide(player, obstacle_group, False, False):
            collision_sound.play()
            game_state = "end"

        # Display score
        score = int(display_score(start_time = start_time, screen = screen)/1000)
    else:
        # Game over state

        # Show Game Over screen
        screen.fill('#D7F3F6')
        
        # Clear loaded obstacles
        obstacle_group.empty()
        
        # Reset clock
        start_time = pygame.time.get_ticks()

        # Font object for text
        game_font = pygame.font.Font('font/Pixeltype.ttf', 50)

        # Game over text
        game_over_surf = game_font.render(f"GAME OVER",False,(64,64,64))
        game_over_rect = game_over_surf.get_rect(center = (400,50))
        screen.blit(game_over_surf, game_over_rect)
        
        # Score text
        score_surf = game_font.render(f"Player {text_input}: {score} seconds",False,(64,64,64))
        score_rect = score_surf.get_rect(center = (400,90))
        screen.blit(score_surf,score_rect)
        
        # Press space to play again prompt
        play_surf = game_font.render(f"Press SPACE to play again",False,(64,64,64))
        play_rect = play_surf.get_rect(center = (400,500))
        screen.blit(play_surf,play_rect)

    # Set refresh rate fps
    clock.tick(60)

