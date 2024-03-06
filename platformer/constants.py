import pygame

screen = pygame.display.set_mode()
SCREEN_WIDTH = screen.get_width()
SCREEN_HEIGHT = screen.get_height()
COLS = SCREEN_WIDTH//32
print(COLS)
ROWS = SCREEN_HEIGHT//32
print(ROWS)


FPS = 60
clock = pygame.time.Clock()

bg_img = pygame.image.load("assets/background.png")
dirt_img = pygame.image.load("assets/dirt.png")
grass_img = pygame.image.load("assets/grass.png")
water_img = pygame.image.load("assets/water.png")
restart_btn_img = pygame.image.load("assets/img/restart_btn.png")
w = restart_btn_img.get_width()
h = restart_btn_img.get_height()
exit_btn_img = pygame.transform.scale(pygame.image.load("assets/img/exit_btn.png"), (w,h))