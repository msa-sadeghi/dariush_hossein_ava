from constants import *
from player import Player
from chick import Chick

bullet_group = pygame.sprite.Group()
egg_group = pygame.sprite.Group()
my_player = Player(bullet_group)
chick_group = pygame.sprite.Group()
level = 1
def start_level():
    for i in range(5):
        for j in range(10):
            new_chick = Chick(j * 96, i *96 + 100, egg_group)
            chick_group.add(new_chick)
            
        
start_level()


def if_on_ege():
    edge = False
    for chick in chick_group:
        if chick.rect.left < 0 or chick.rect.right > SCREEN_WIDTH:
            edge = True
            
    if edge == True:
        for chick in chick_group:
            chick.direction *= -1
            chick.rect.y += 5 * level
            
def check_collisions():
    if pygame.sprite.groupcollide(bullet_group, chick_group, True, True):
        pass
    if pygame.sprite.spritecollide(my_player, egg_group, True):
        pass


running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
            if event.key == pygame.K_SPACE:
                my_player.fire()
    screen.fill((0,0,0)) 
    check_collisions() 
    bullet_group.draw(screen)
    bullet_group.update()
    egg_group.draw(screen)
    egg_group.update()
    if_on_ege()         
    my_player.move()
    my_player.draw()
    chick_group.update()
    chick_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)