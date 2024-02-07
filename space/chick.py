from constants import *
from pygame.sprite import Sprite
from egg import Egg
import random
class Chick(Sprite):
    def __init__(self, x,y, egg_group):
        super().__init__()
        self.image = pygame.image.load("assets/chick.png")
        self.rect = self.image.get_rect(topleft=(x,y))
        self.speed = 5
        self.direction = 1
        self.egg_group = egg_group
        
    def update(self):
        self.rect.x += self.speed * self.direction
        
        if random.randint(1,1000) > 999 and len(self.egg_group) < 4:
            self.fire()
        
        
    def fire(self):
        Egg(self.rect.centerx, self.rect.bottom, self.egg_group)
        