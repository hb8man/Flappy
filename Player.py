import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/pixil-frame-0-2.png').convert_alpha()
        self.scaled = pygame.transform.scale(self.image, (30,30))
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