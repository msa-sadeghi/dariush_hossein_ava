from constants import *
from castle import Castle
from enemy import Enemy
from mouse_pointer import MousePointer

bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

castle = Castle(
    castle_image_100,
    castle_image_50, 
    castle_image_25,
    SCREEN_WIDTH - 250,
    SCREEN_HEIGHT - 350,
    0.2
    )



enemy1 = Enemy(enemy_health[3], enemy_animations[3], 100, 350, 1)
enemy_group.add(enemy1)
mouse = MousePointer()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    castle.shoot(bullet_group)
    screen.blit(bg_image, (0,0))  
    mouse.draw(screen)
    castle.draw(screen) 
    bullet_group.draw(screen)    
    bullet_group.update()
    enemy_group.draw(screen)    
    enemy_group.update(castle, bullet_group)
    pygame.display.update()
    clock.tick(FPS)
    