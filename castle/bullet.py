from constants import SCREEN_WIDTH, SCREEN_HEIGHT, pygame
from pygame.sprite import Sprite
import math
class Bullet(Sprite):
    def __init__(self, image, x,y, scale, angle):
        super().__init__()
        self.image = pygame.transform.scale(image,(image.get_width()*scale, image.get_height()*scale))
        self.rect = self.image.get_rect(topleft = (x,y))
        self.angle = angle
        self.speed = 15
        
        self.dx = math.cos(self.angle) * self.speed
        self.dy = -math.sin(self.angle) * self.speed
        
    def update(self):
        
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH or self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT:
            self.kill()
        
        