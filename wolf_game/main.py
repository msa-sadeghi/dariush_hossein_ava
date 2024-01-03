import random
import pygame

pygame.init()



def game_over():
    global score,lives, running
    
    game_over_text = font72.render("Game Over, press enter to play again", True, (10,230,210))
    game_over_rect = game_over_text.get_rect()
    game_over_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    score_text = font48.render(f"Score:{score}", True, (240, 10, 238))
    lives_text = font48.render(f"Lives {lives}",True, (240, 10, 238))
    pygame.mixer.music.stop()
    screen.fill((0,0,0))
    screen.blit(score_text, score_rect)
    screen.blit(lives_text, lives_rect)
    screen.blit(game_over_text, game_over_rect)
    pygame.display.update()
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    paused = False
                    score = 0
                    lives = 3
                    pygame.mixer.music.play(-1)


            







SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 700
FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


font72 = pygame.font.Font("assets/f.otf",72)
font48 = pygame.font.Font("assets/f.otf",48)

welcome_text = font72.render("Welcome To My Game", True, (10,190,180))
welcome_rect = welcome_text.get_rect()
welcome_rect.center = (SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)

score = 0
lives = 3

score_text = font48.render(f"Score:{score}", True, (240, 10, 238))
score_rect = score_text.get_rect()
score_rect.topleft = (0,0)


lives_text = font48.render(f"Lives {lives}",True, (240, 10, 238))
lives_rect = lives_text.get_rect()
lives_rect.topright = (SCREEN_WIDTH, 0)


wolf_image = pygame.image.load("assets/wolf.png")
wolf_rect = wolf_image.get_rect()
wolf_rect.bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT)

sheep_image = pygame.image.load("assets/sheep.png")
sheep_image = pygame.transform.flip(sheep_image, True, False)
sheep_rect = sheep_image.get_rect()
sheep_rect.bottomleft = (0, random.randint(200, SCREEN_HEIGHT))


pygame.mixer.music.load("assets/Bad Piggies Theme.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
catch_sound = pygame.mixer.Sound("assets/c.wav")



start_time = pygame.time.get_ticks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.time.get_ticks() - start_time < 2000:
        screen.blit(welcome_text, welcome_rect)
    else:
        ########################################
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and wolf_rect.top > 0:
            wolf_rect.y -= 5

        if keys[pygame.K_DOWN] and wolf_rect.bottom < SCREEN_HEIGHT:
            wolf_rect.y += 5

        if keys[pygame.K_LEFT] and wolf_rect.left > 0:
            wolf_rect.x -= 5

        if keys[pygame.K_RIGHT] and wolf_rect.right < SCREEN_WIDTH:
            wolf_rect.x += 5

        sheep_rect.x += 5
        if sheep_rect.right > SCREEN_WIDTH:
            sheep_rect.bottomleft = (0, random.randint(200, SCREEN_HEIGHT))
            lives -= 1
            if lives <= 0:
                game_over()

        if wolf_rect.colliderect(sheep_rect):
            sheep_rect.bottomleft = (0, random.randint(200, SCREEN_HEIGHT))
            catch_sound.play()
            score += 1


        score_text = font48.render(f"Score:{score}", True, (240, 10, 238))
        lives_text = font48.render(f"Lives {lives}",True, (240, 10, 238))
        screen.fill((0,0,0))
        screen.blit(wolf_image, wolf_rect)
        screen.blit(sheep_image, sheep_rect)
        screen.blit(score_text, score_rect)
        screen.blit(lives_text, lives_rect)
        ##########################################

    pygame.display.update()
    clock.tick(FPS)


