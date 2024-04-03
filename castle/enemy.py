from pygame.sprite import Sprite
import pygame
class Enemy(Sprite):
    def __init__(self, health, animation_list, x,y, speed):
        super().__init__()
        self.alive = True
        self.speed = speed 
        self.health = health
        self.animation_list = animation_list
        self.frame_index = 0
        self.action = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect(topleft=(x,y))
        self.update_time = pygame.time.get_ticks()  
        self.last_attack_time = pygame.time.get_ticks()    
    def update(self, target, bullet_group):
        if pygame.sprite.spritecollide(self, bullet_group, True):
            self.health -= 25
        if self.health <= 0:
            self.alive = False
            target.money += 100
            target.score += 100
            self.update_action(2)
            
        
        if self.rect.right >= target.rect.left:
            self.update_action(1)
        if self.action == 0:
            self.rect.x += self.speed
            
        if self.action == 1 :
            if pygame.time.get_ticks() - self.last_attack_time > 3000:
                target.health -= 10
                if target.health < 0:
                    target.health = 0
                self.last_attack_time =   pygame.time.get_ticks()
            
        self.update_animation()
    
    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
    
       
    def update_animation(self):
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > 100:
            self.frame_index += 1
            if self.frame_index >= len(self.animation_list[self.action]):
                if self.action == 2:
                    self.frame_index = len(self.animation_list[self.action])-1
                else:
                    self.frame_index = 0
        
        