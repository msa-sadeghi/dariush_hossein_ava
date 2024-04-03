import pygame
class MousePointer:
    def __init__(self):
        self.image = pygame.image.load("assets/crosshair.png")
        w = self.image.get_width()
        h = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (w * 0.04, h * 0.04))
        pygame.mouse.set_visible(False)
        
    def draw(self,screen):
        pos = pygame.mouse.get_pos()
        screen.blit(self.image, pos)
        
        