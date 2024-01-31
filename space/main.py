from constants import *
from player import Player
from chick import Chick


my_player = Player()
chick_group = pygame.sprite.Group()
level = 1
def start_level():
    for i in range(5):
        for j in range(10):
            new_chick = Chick(j * 96, i *96)
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
            



running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    screen.fill((0,0,0))  
    if_on_ege()         
    my_player.move()
    my_player.draw()
    chick_group.update()
    chick_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)