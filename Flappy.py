"""Flappy.py
Authors: W. Henry Bateman
Date Completed:
Description:
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

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.gravity = -7

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
            self.rect = pygame.Rect(830,0,30,250)
            self.image.fill('#8EBC41')
        if type == 2:
            self.image = pygame.Surface(size = (30,100))
            self.rect = pygame.Rect(830,400,30,100)
            self.image.fill('#8EBC41')
        # Group 2
        if type == 3:
            self.image = pygame.Surface(size = (30,300))
            self.rect = pygame.Rect(830,200,30,300)
            self.image.fill('#8EBC41')
        if type == 4:
            self.image = pygame.Surface(size = (30,50))
            self.rect = pygame.Rect(830,0,30,50)
            self.image.fill('#8EBC41')
        # Group 3
        if type == 5:
            self.image = pygame.Surface(size = (30,150))
            self.rect = pygame.Rect(830,350,30,150)
            self.image.fill('#8EBC41')
        if type == 6:
            self.image = pygame.Surface(size = (30,150))
            self.rect = pygame.Rect(830,0,30,150)
            self.image.fill('#8EBC41')
    
    def update(self):
        self.rect.x -= 4
        if game_active == False:
            self.rect.x = 830

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

def display_score():
    game_font = pygame.font.Font('font/Pixeltype.ttf', 50)
    current_time = int(pygame.time.get_ticks()) - start_time
    score_surf = game_font.render(f"{int(current_time/1000)}",False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return current_time
    

pygame.init()

game_active = True
start_time = 0
score = 0

screen = pygame.display.set_mode((800, 600))
# Set window caption
pygame.display.set_caption("Flappy")
# Clock object to control framerate
clock = pygame.time.Clock()

player = pygame.sprite.GroupSingle()
loaded_player = player.add(Player())

obstacle_group = pygame.sprite.Group()

# Background Surfaces
sky_surface = pygame.image.load('Graphics/Sky.png').convert_alpha()
sky_surface_top = pygame.Surface(size = (800, 300))
sky_surface_top.fill(color = "#D7F3F6")
ground_surface = pygame.image.load('Graphics/Ground.png').convert_alpha()
ground_rect = ground_surface.get_rect(topleft = (0,500))
# text_surface = game_font.render('Flappy', True, 'Black').convert_alpha()

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 850)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active == True:
            if event.type ==  obstacle_timer:
                spawn_obstacle()
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True

    # Updates screen
    pygame.display.update()
    
    if game_active == True:
        # Show game view

        # Render background objects
        screen.blit(sky_surface_top, (0,0))
        screen.blit(sky_surface, (0,200))
        screen.blit(ground_surface, ground_rect)

        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        if pygame.sprite.groupcollide(player, obstacle_group, False, False):
            game_active = False

        score = int(display_score()/1000)
        # 4243 milliseconds to get to obstacle
    else:
        # Show Game Over screen
        screen.fill('#D7F3F6')
        obstacle_group.empty()
        start_time = pygame.time.get_ticks()

        game_font = pygame.font.Font('font/Pixeltype.ttf', 50)

        image_surf = pygame.image.load('graphics/pixil-frame-0-2.png').convert_alpha()
        image_rect = image_surf.get_rect(center = (400, 400))
        screen.blit(image_surf, image_rect)

        game_over_surf = game_font.render(f"GAME OVER",False,(64,64,64))
        game_over_rect = game_over_surf.get_rect(center = (400,50))
        screen.blit(game_over_surf, game_over_rect)
        
        score_surf = game_font.render(f"Score: {score} seconds",False,(64,64,64))
        score_rect = score_surf.get_rect(center = (400,90))
        screen.blit(score_surf,score_rect)
        # Press space to play again
        play_surf = game_font.render(f"Press SPACE to play again",False,(64,64,64))
        play_rect = play_surf.get_rect(center = (400,500))
        screen.blit(play_surf,play_rect)

    # Set refresh rate fps
    clock.tick(60)

