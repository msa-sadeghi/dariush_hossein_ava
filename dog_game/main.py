import random
import pygame

pygame.init()

screen = pygame.display.set_mode()
SCREEN_WIDTH = screen.get_width()
SCREEN_HEIGHT = screen.get_height()
score = 0
lives = 3
font = pygame.font.Font("assets/f.otf", 32)
score_text = font.render(f"Score:{score}", True, (190, 10, 180))
score_rect = score_text.get_rect()
score_rect.topleft = (0, 0)


lives_text = font.render(f"Lives:{lives}", True, (190, 10, 180))
lives_rect = lives_text.get_rect()
lives_rect.top = 0
lives_rect.centerx = SCREEN_WIDTH / 2




clock = pygame.time.Clock()
dog_image = pygame.image.load("assets/dog.png")

dog_left_image = dog_image
dog_right_image = pygame.transform.flip(dog_left_image, True, False)

dog_rect = dog_image.get_rect()
dog_rect.bottom = SCREEN_HEIGHT
dog_rect.centerx = SCREEN_WIDTH / 2

bone_image = pygame.image.load("assets/bone.png")
bone_rect = bone_image.get_rect()
bone_rect.top = 0
bone_rect.centerx = SCREEN_WIDTH / 2


bomb_image = pygame.image.load('assets/bomb.png')
bomb_rect = bomb_image.get_rect()
bomb_rect.top = 50
bomb_rect.left = random.randint(0, SCREEN_WIDTH - 48)



dog_normal_speed = 5
dog_boost_speed = 15

dog_speed = dog_normal_speed
boost_level = 100
boost_text = font.render(f"boost:{boost_level}", True, (190, 10, 180))
boost_rect = boost_text.get_rect()
boost_rect.topright = (SCREEN_WIDTH, 0)

running = True


def game_over():
    global running, score,lives, boost_level
    game_over_text = font.render("Game Over, Press Enter", True, (190,10,180))
    game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    screen.fill((0,0,0))
    screen.blit(game_over_text, game_over_rect)
    pygame.display.update()
    paused = True
    
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                paused = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    paused = False
                    score = 0
                    lives = 3
                    boost_level = 100



while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    bone_rect.y += 5
    if bone_rect.top >= SCREEN_HEIGHT:
        bone_rect.top = 0
        bone_rect.centerx = random.randint(bone_image.get_width() / 2, SCREEN_WIDTH - bone_image.get_width() / 2)
    bomb_rect.y += 10
    if bomb_rect.top >=SCREEN_HEIGHT:
        bomb_rect.top = 50
        bomb_rect.left = random.randint(0, SCREEN_WIDTH - 48)


    if dog_rect.colliderect(bone_rect):
        score += 1
        boost_level += 5
        if boost_level > 100:
            boost_level = 100
        bone_rect.top = 0
        bone_rect.centerx = random.randint(bone_image.get_width() / 2, SCREEN_WIDTH - bone_image.get_width() / 2)


    if dog_rect.colliderect(bomb_rect):
        lives -= 1
        bomb_rect.top = 50
        bomb_rect.left = random.randint(0, SCREEN_WIDTH - 48)
        if lives <= 0:
            game_over()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and dog_rect.top > 0:
        dog_rect.y -= dog_speed
    if keys[pygame.K_DOWN] and dog_rect.bottom < SCREEN_HEIGHT:
        dog_rect.y += dog_speed

    if keys[pygame.K_LEFT] and dog_rect.left > 0:
        dog_rect.x -= dog_speed
        dog_image = dog_left_image

    if keys[pygame.K_RIGHT] and dog_rect.right < SCREEN_WIDTH:
        dog_rect.x += dog_speed
        dog_image = dog_right_image

    if keys[pygame.K_SPACE] and boost_level > 0:
        boost_level -= 1
        dog_speed = dog_boost_speed

    if not keys[pygame.K_SPACE] or boost_level <= 0:
        dog_speed = dog_normal_speed

    score_text = font.render(f"Score:{score}", True, (190, 10, 180))
    boost_text = font.render(f"boost:{boost_level}", True, (190, 10, 180))
    lives_text = font.render(f"Lives:{lives}", True, (190, 10, 180))
    screen.fill((0, 0, 0))
    screen.blit(dog_image, dog_rect)
    screen.blit(bone_image, bone_rect)
    screen.blit(score_text, score_rect)
    screen.blit(boost_text, boost_rect)
    screen.blit(lives_text, lives_rect)
    screen.blit(bomb_image, bomb_rect)
    pygame.display.update()
    clock.tick(60)

# TODO   اضافه کردن استخوان به بالا و وسط صفحه
# TODO  استخوان به سمت پایین صفحه حرکت نماید
# TODO  سگ توسط باریکن به چهار جهت حرکت نماید
# TODO  در صورت برخورد استخوان و سگ، به بازیکن امتیاز داده شود
# TODO  در صورت خروج استخوان از پایین صفحه، از امتیاز بایکن کم شود
# TODO  در صورت صفر شدن جان بازیکن بازی تمام شود
