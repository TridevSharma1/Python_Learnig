import pygame
import random

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

# Window size
width = 600
height = 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("🐍 Snake Game")

clock = pygame.time.Clock()
snake_size = 10
snake_speed = 15

font = pygame.font.SysFont(None, 35)

def message(msg, color):
    text = font.render(msg, True, color)
    win.blit(text, [width/6, height/3])

def gameLoop():
    game_over = False
    game_close = False

    x = width/2
    y = height/2

    x_change = 0
    y_change = 0

    snake_list = []
    length = 1

    food_x = round(random.randrange(0, width - snake_size) / 10) * 10
    food_y = round(random.randrange(0, height - snake_size) / 10) * 10

    while not game_over:

        while game_close:
            win.fill(black)
            message("Game Over! Press R to Restart", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_size
                    x_change = 0

        x += x_change
        y += y_change

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        win.fill(black)
        pygame.draw.rect(win, green, [food_x, food_y, snake_size, snake_size])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > length:
            del snake_list[0]

        for part in snake_list[:-1]:
            if part == snake_head:
                game_close = True

        for px, py in snake_list:
            pygame.draw.rect(win, white, [px, py, snake_size, snake_size])

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_size) / 10) * 10
            food_y = round(random.randrange(0, height - snake_size) / 10) * 10
            length += 1

        clock.tick(snake_speed)

    pygame.quit()

gameLoop()
