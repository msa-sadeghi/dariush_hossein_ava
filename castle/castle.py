from constants import *
import math
from bullet import Bullet
class Castle:
    def __init__(self, image_100, image_50, image_25, x,y, scale):
        self.health = 1000
        self.money = 0
        self.score = 0
        self.max_health = self.health
        
        w = image_100.get_width()
        h = image_100.get_height()
        self.image_100 = pygame.transform.scale(image_100, (w * scale, h * scale))
        self.image_50 = pygame.transform.scale(image_50, (w * scale, h * scale))
        self.image_25 = pygame.transform.scale(image_25, (w * scale, h * scale))
        self.rect = self.image_100.get_rect(topleft= (x,y))
        self.fired = False
        
    def draw(self, screen):
        if self.health <= 250:
            self.image = self.image_25
        elif self.health <= 500:
            self.image = self.image_50
        else:    
            self.image = self.image_100
        
        screen.blit(self.image, self.rect)
    def shoot(self, bullet_group):
        pos = pygame.mouse.get_pos()
        x_dist = pos[0] - self.rect.midleft[0]
        y_dist = -(pos[1] - self.rect.midleft[1])
        self.angle = math.atan2(y_dist, x_dist)
        
        if pygame.mouse.get_pressed()[0] and not self.fired:
            b = Bullet(bullet_image, self.rect.midleft[0], self.rect.midleft[1],0.2, self.angle)
            bullet_group.add(b)
            self.fired = True
        if not pygame.mouse.get_pressed()[0]:
            self.fired = False
        
            
            
            
        
        
                                                