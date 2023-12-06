"""Flappy.py
Authors: Vicky Singharaj, Katarina Schoening, W. Bateman
Date Completed: 12/3/2023
Description: This is a flappy bird type game made with pygame using Python
the user can enter their name to have their score and name displayed after they play. 
The user can opt to play again or click the 'x' to exit. 
"""

import pygame
import random


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/pixil-frame-0-2.png').convert_alpha()
        self.scaled = pygame.transform.scale(self.image,(30,30))
        self.rect = self.scaled.get_rect(center = (240, 250))
        self.gravity = 0
        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.04)

    # Make player sprite "jump" when space is pressed
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.gravity = -7
            self.jump_sound.play()
    
    # Change player y position down to mimic gravity
    def apply_gravity(self):
        self.gravity += 0.5
        self.rect.y += self.gravity
        if self.rect.bottom >= 500:
            self.rect.bottom = 500
        if self.rect.top <= 0:
            self.rect.top = 0  

    def update(self):
        self.player_input()
        self.apply_gravity()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        # Group 1
        if type == 1:
            self.image = pygame.Surface(size = (30,250))
            self.rect = pygame.Rect(830,0,25,235)
            self.image.fill('#8EBC41')
        if type == 2:
            self.image = pygame.Surface(size = (30,100))
            self.rect = pygame.Rect(830,400,25,95)
            self.image.fill('#8EBC41')
        # Group 2
        if type == 3:
            self.image = pygame.Surface(size = (30,300))
            self.rect = pygame.Rect(830,200,25,295)
            self.image.fill('#8EBC41')
        if type == 4:
            self.image = pygame.Surface(size = (30,50))
            self.rect = pygame.Rect(830,0,25,45)
            self.image.fill('#8EBC41')
        # Group 3
        if type == 5:
            self.image = pygame.Surface(size = (30,150))
            self.rect = pygame.Rect(830,350,25,145)
            self.image.fill('#8EBC41')
        if type == 6:
            self.image = pygame.Surface(size = (30,150))
            self.rect = pygame.Rect(830,0,25,145)
            self.image.fill('#8EBC41')
    
    def update(self):
        self.rect.x -= 4
        if game_state == "game":
            self.rect.x = 830

# Adds two obstacle sprites from random int
def spawn_obstacle():
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
def display_score():
    game_font = pygame.font.Font('font/Pixeltype.ttf', 50)
    current_time = int(pygame.time.get_ticks()) - start_time
    score_surf = game_font.render(f"{int(current_time/1000)}",False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return current_time
    
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
sky_surface_top.fill(color = "#D7F3F6")
ground_surface = pygame.image.load('Graphics/Ground.png').convert_alpha()
ground_rect = ground_surface.get_rect(topleft = (0,500))

# Obstacle timer
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
                spawn_obstacle()
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
        score = int(display_score()/1000)
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

