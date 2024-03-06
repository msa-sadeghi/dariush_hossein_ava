from constants import *
from world import World
from levels.level1 import world_data
from player import Player
from button import Button

my_player = Player()
enemy_group = pygame.sprite.Group()
game_world = World(world_data, enemy_group)

restart_btn = Button(SCREEN_WIDTH/2 - 200, SCREEN_HEIGHT/2, restart_btn_img)
exit_btn = Button(SCREEN_WIDTH/2 + 200, SCREEN_HEIGHT/2, exit_btn_img)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    game_world.draw()
    my_player.update(game_world.tilemap, enemy_group)
    if my_player.alive:
        enemy_group.update()
    else:
        restart_btn.draw(screen)
        exit_btn.draw(screen)
        if restart_btn.check_click():
            my_player.__init__()
            enemy_group.empty()
            game_world = World(world_data, enemy_group)
        if exit_btn.check_click():
            running = False
    enemy_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)