import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        # Group 1
        if type == 1:
            self.image = pygame.Surface(size = (30, 250))
            self.rect = pygame.Rect(830,0,25,235)
            self.image.fill('#8EBC41')
        if type == 2:
            self.image = pygame.Surface(size = (30, 100))
            self.rect = pygame.Rect(830,400,25,95)
            self.image.fill('#8EBC41')
        # Group 2
        if type == 3:
            self.image = pygame.Surface(size = (30,300))
            self.rect = pygame.Rect(830, 200, 25, 295)
            self.image.fill('#8EBC41')
        if type == 4:
            self.image = pygame.Surface(size = (30, 50))
            self.rect = pygame.Rect(830, 0, 25, 45)
            self.image.fill('#8EBC41')
        # Group 3
        if type == 5:
            self.image = pygame.Surface(size = (30, 150))
            self.rect = pygame.Rect(830, 350, 25, 145)
            self.image.fill('#8EBC41')
        if type == 6:
            self.image = pygame.Surface(size = (30, 150))
            self.rect = pygame.Rect(830, 0, 25, 145)
            self.image.fill('#8EBC41')
    
    def update(self):
        self.rect.x -= 4