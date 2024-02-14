from constants import *
class World:
    def __init__(self, world_data):
        self.image = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.image.get_rect(topleft=(0,0))
        self.tilemap = []
        
        for i in range(ROWS):
            for j in range(COLS):
                if world_data[i][j] == 1:
                    img = dirt_img
                    rect = img.get_rect(topleft=(j * 32, i *32))
                    self.tilemap.append((img, rect))
                if world_data[i][j] == 2:
                    img = grass_img
                    rect = img.get_rect(topleft=(j * 32, i *32))
                    self.tilemap.append((img, rect))
        
    def draw(self):
        screen.blit(self.image, self.rect)
        for tile in self.tilemap:
            screen.blit(tile[0], tile[1])