from constants import *
from pygame.sprite import Sprite
class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN_HEIGHT
        self.rect.centerx = SCREEN_WIDTH/2
        self.speed = 5
    
    def draw(self):
        screen.blit(self.image, self.rect)
        
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
        