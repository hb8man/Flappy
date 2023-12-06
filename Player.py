import pygame

class Player(pygame.sprite.Sprite):
    """Creates player sprite and changes y position.
    """
    def __init__(self):
        super().__init__()
        try:
            image = 'graphics/pixil-frame-0-2.png'
            self.image = pygame.image.load(image).convert_alpha()
        except IOError:
            print(f'{image} not found.')
            pygame.quit()
            exit()        
        self.scaled = pygame.transform.scale(self.image, (30,30))
        self.rect = self.scaled.get_rect(center = (240, 250))
        self.gravity = 0
        try:
            audio = 'audio/jump.mp3'
            self.jump_sound = pygame.mixer.Sound(audio)
        except IOError:
            print(f'{audio} not found.')    
            pygame.quit()
            exit()
        self.jump_sound.set_volume(0.04)

    # Make player sprite "jump" when space is pressed
    def player_input(self):
        """Player jump.

        Moves player up on screen when space is pressed.
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.gravity = -7
            self.jump_sound.play()
    
    # Change player y position down to mimic gravity
    def apply_gravity(self):
        """Player affected by gravity

        Moves player down on screen and sets y range for player.
        """
        self.gravity += 0.5
        self.rect.y += self.gravity
        if self.rect.bottom >= 500:
            self.rect.bottom = 500
        if self.rect.top <= 0:
            self.rect.top = 0  

    def update(self):
        """Checks for jumping and applies gravity 
        """
        self.player_input()
        self.apply_gravity()