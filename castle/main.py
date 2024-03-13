from constants import *
from castle import Castle


castle = Castle(
    castle_image_100,
    castle_image_50, 
    castle_image_25,
    SCREEN_WIDTH - 250,
    SCREEN_HEIGHT - 350,
    0.2
    )


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bg_image, (0,0))  
    castle.draw(screen)     
    pygame.display.update()
    clock.tick(FPS)
    