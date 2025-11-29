import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🔥 Simple Shooting Game")

WHITE = (255, 255, 255)
RED = (255, 50, 50)
BLUE = (50, 50, 255)
BLACK = (0, 0, 0)

player_x = 300
player_y = 450
player_speed = 5

bullets = []
enemies = []

score = 0
font = pygame.font.SysFont(None, 35)

def draw():
    win.fill(BLACK)

    # player
    pygame.draw.rect(win, BLUE, (player_x, player_y, 40, 40))

    # bullets
    for b in bullets:
        pygame.draw.rect(win, WHITE, (b[0], b[1], 5, 10))

    # enemies
    for e in enemies:
        pygame.draw.rect(win, RED, (e[0], e[1], 40, 40))

    text = font.render(f"Score: {score}", True, WHITE)
    win.blit(text, (10, 10))

    pygame.display.update()

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)

    # spawn enemies
    if random.randint(1, 40) == 1:
        enemies.append([random.randint(0, 560), 0])

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # shooting
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([player_x + 20, player_y])

    # player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH-40:
        player_x += player_speed

    # move bullets
    for b in bullets:
        b[1] -= 7
        if b[1] < 0:
            bullets.remove(b)

    # move enemies
    for e in enemies:
        e[1] += 3
        if e[1] > HEIGHT:
            enemies.remove(e)

    # collision detection
    for e in enemies:
        for b in bullets:
            if (b[0] > e[0] and b[0] < e[0]+40) and (b[1] > e[1] and b[1] < e[1]+40):
                bullets.remove(b)
                enemies.remove(e)
                score += 1

    draw()

pygame.quit()
