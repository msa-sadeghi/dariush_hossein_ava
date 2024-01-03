import pygame
pygame.init()


screen = pygame.display.set_mode()

SCREEN_WIDTH = screen.get_width()
SCREEN_HEIGHT = screen.get_height()




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

# TODO   اضافه کردن سگ به پایین و وسط صفحه
# TODO   اضافه کردن استخوان به بالا و وسط صفحه
# TODO  استخوان به سمت پایین صفحه حرکت نماید
# TODO  سگ توسط باریکن به چهار جهت حرکت نماید
# TODO  در صورت برخورد استخوان و سگ، به بازیکن امتیاز داده شود
# TODO  در صورت خروج استخوان از پایین صفحه، از امتیاز بایکن کم شود
# TODO  در صورت صفر شدن جان بازیکن بازی تمام شود
                
                
                
                

                