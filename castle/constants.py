import pygame
SCREEN_WIDTH = 1065
SCREEN_HEIGHT = 600
FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bg_image = pygame.image.load("assets/bg.png")
armour_image = pygame.image.load("assets/armour.png")
bullet_image = pygame.image.load("assets/bullet.png")
crosshair_image = pygame.image.load("assets/crosshair.png")
repair_image = pygame.image.load("assets/repair.png")

castle_image_100 = pygame.image.load("assets/castle/castle_100.png")
castle_image_50 = pygame.image.load("assets/castle/castle_50.png")
castle_image_25 = pygame.image.load("assets/castle/castle_25.png")

tower_image_100 = pygame.image.load("assets/tower/tower_100.png")
tower_image_50 = pygame.image.load("assets/tower/tower_50.png")
tower_image_25 = pygame.image.load("assets/tower/tower_25.png")

enemy_animations = []
enemy_types = ('knight', 'goblin', 'purple_goblin', 'red_goblin')
enemy_health = (75, 100, 125, 150)
animation_types = ('walk', 'attack', 'death')

for enemy in enemy_types:
    animation_list = []
    for animation in animation_types:
        animation_enemy = []
        for i in range(20):
            img = pygame.image.load(f"assets/enemies/{enemy}/{animation}/{i}.png")
            w = img.get_width()
            h = img.get_height()
            img = pygame.transform.scale(img, (w * 0.2, h * 0.2))
            animation_enemy.append(img)
        animation_list.append(animation_enemy)
    enemy_animations.append(animation_list)
    
        
        
    

