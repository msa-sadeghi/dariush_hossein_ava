from constants import *
class World:
    def __init__(self):
        self.image = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.image.get_rect(topleft=(0,0))
    def draw(self):
        screen.blit(self.image, self.rect)