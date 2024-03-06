from pygame.sprite import Sprite
from constants import *
class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.right_images = []
        self.left_images = []
        for i in range(1,5):
            img = pygame.image.load(f"assets/img/guy{i}.png")
            self.right_images.append(img)
            left_img = pygame.transform.flip(img, True, False)
            self.left_images.append(left_img)      
        self.frame_index = 0
        self.image = self.right_images[self.frame_index]
        self.rect = self.image.get_rect(topleft = (100, 400))
        self.update_time = pygame.time.get_ticks()
        self.yspeed = 0
        self.moving = False
        self.direction = 1        
    def update(self, tile_map):
        self.animation()
        self.move(tile_map)
        screen.blit(self.image, self.rect)    
    def move(self, tile_map):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction = -1
            self.moving = True
            dx -= 5
        if keys[pygame.K_RIGHT]:
            self.direction = 1
            self.moving = True
            dx += 5        
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.moving = False        
        if keys[pygame.K_SPACE]:
            self.yspeed = -15       
        self.yspeed += 1        
        dy += self.yspeed  
        
        for tile in tile_map:
            if tile[1].colliderect(self.rect.x +dx , self.rect.y, self.image.get_width(), self.image.get_height()):
                dx = 0
                
            if tile[1].colliderect(self.rect.x , self.rect.y + dy, self.image.get_width(), self.image.get_height()):
                if self.yspeed > 0:
                    self.yspeed = 0
                    dy = tile[1].top - self.rect.bottom
                elif self.yspeed < 0:
                    self.yspeed = 0
                    dy = tile[1].bottom - self.rect.top

            
              
        self.rect.x += dx
        self.rect.y += dy        
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT       
    def animation(self):
        if pygame.time.get_ticks() - self.update_time > 200:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.right_images):
            self.frame_index = 0            
        if not self.moving:            
            self.frame_index = 0    
        if self.direction == 1:
            self.image = self.right_images[self.frame_index]
        elif self.direction == -1:
            self.image = self.left_images[self.frame_index]
            