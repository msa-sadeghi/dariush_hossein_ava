from constants import pygame
class Castle:
    def __init__(self, image_100, image_50, image_25, x,y, scale):
        self.health = 1000
        self.max_health = self.health
        
        w = image_100.get_width()
        h = image_100.get_height()
        self.image_100 = pygame.transform.scale(image_100, (w * scale, h * scale))
        self.image_50 = pygame.transform.scale(image_50, (w * scale, h * scale))
        self.image_25 = pygame.transform.scale(image_25, (w * scale, h * scale))
        self.rect = self.image_100.get_rect(topleft= (x,y))
        
    def draw(self, screen):
        self.image = self.image_100
        screen.blit(self.image, self.rect)
        
                                                