from constants import *
from pygame.sprite import Sprite

class Chick(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image = pygame.image.load("assets/chick.png")
        self.rect = self.image.get_rect(topleft=(x,y))
        self.speed = 5
        self.direction = 1
        
    def update(self):
        self.rect.x += self.speed * self.direction
        
        
    