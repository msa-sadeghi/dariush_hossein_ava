from constants import *
from world import World
from levels.level1 import world_data
from player import Player


my_player = Player()

game_world = World(world_data)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    game_world.draw()
    my_player.update(game_world.tilemap)
    pygame.display.update()
    clock.tick(FPS)