import random
import pygame
pygame.init()


screen = pygame.display.set_mode()
score = 0
font = pygame.font.Font("assets/f.otf", 32)
score_text = font.render(f"Score:{score}", True, (190,10,180))
score_rect = score_text.get_rect()
score_rect.topleft = (0,0)

SCREEN_WIDTH = screen.get_width()
SCREEN_HEIGHT = screen.get_height()
clock = pygame.time.Clock()
dog_image = pygame.image.load("assets/dog.png")

dog_left_image = dog_image
dog_right_image = pygame.transform.flip(dog_left_image, True, False)


dog_rect = dog_image.get_rect()
dog_rect.bottom = SCREEN_HEIGHT
dog_rect.centerx = SCREEN_WIDTH/2

bone_image = pygame.image.load("assets/bone.png")
bone_rect = bone_image.get_rect()
bone_rect.top = 0
bone_rect.centerx = SCREEN_WIDTH/2

dog_normal_speed = 5
dog_boost_speed = 15

dog_speed = dog_normal_speed
boost_level = 100
boost_text = font.render(f"boost:{boost_level}", True, (190,10,180))
boost_rect = boost_text.get_rect()
boost_rect.topright = (SCREEN_WIDTH,0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    bone_rect.y += 5
    if bone_rect.top >= SCREEN_HEIGHT:
        bone_rect.top = 0
        bone_rect.centerx = random.randint(bone_image.get_width()/2, SCREEN_WIDTH- bone_image.get_width()/2)

    if dog_rect.colliderect(bone_rect):
        score += 1
        boost_level += 5
        if boost_level > 100:
            boost_level = 100
        bone_rect.top = 0
        bone_rect.centerx = random.randint(bone_image.get_width()/2, SCREEN_WIDTH- bone_image.get_width()/2)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        dog_rect.y -= dog_speed
    if keys[pygame.K_DOWN]:
        dog_rect.y += dog_speed
    
    if keys[pygame.K_LEFT]:
        dog_rect.x -= dog_speed
        dog_image = dog_left_image

    if keys[pygame.K_RIGHT]:
        dog_rect.x += dog_speed
        dog_image = dog_right_image

    if keys[pygame.K_SPACE] and boost_level > 0:
        boost_level -= 1
        dog_speed = dog_boost_speed

    if not keys[pygame.K_SPACE] or boost_level <= 0:
        dog_speed = dog_normal_speed


    score_text = font.render(f"Score:{score}", True, (190,10,180))
    boost_text = font.render(f"boost:{boost_level}", True, (190,10,180))
    screen.fill((0,0,0))
    screen.blit(dog_image, dog_rect)
    screen.blit(bone_image, bone_rect)
    screen.blit(score_text, score_rect)
    screen.blit(boost_text, boost_rect)
    pygame.display.update()
    clock.tick(60)

# TODO   اضافه کردن استخوان به بالا و وسط صفحه
# TODO  استخوان به سمت پایین صفحه حرکت نماید
# TODO  سگ توسط باریکن به چهار جهت حرکت نماید
# TODO  در صورت برخورد استخوان و سگ، به بازیکن امتیاز داده شود
# TODO  در صورت خروج استخوان از پایین صفحه، از امتیاز بایکن کم شود
# TODO  در صورت صفر شدن جان بازیکن بازی تمام شود
                
                
                
                

                