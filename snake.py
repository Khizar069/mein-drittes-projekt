import pygame
import time
import random

# Initialisierung von pygame
pygame.init()

# Bildschirmgröße
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Spiel")

# Farben
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (213, 50, 80)
BLACK = (0, 0, 0)
BLUE = (50, 153, 213)

# Snake-Einstellungen
snake_block = 10
snake_speed = 15

# Schriftart
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def display_score(score):
    value = score_font.render(f"Punkte: {score}", True, WHITE)
    win.blit(value, [10, 10])

def game_over_message():
    msg = font_style.render("Game Over! Drücke R zum Neustart oder Q zum Beenden", True, RED)
    win.blit(msg, [WIDTH / 6, HEIGHT / 3])
    pygame.display.update()

def game_loop():
    game_over = False
    game_close = False

    x, y = WIDTH / 2, HEIGHT / 2
    x_change, y_change = 0, 0
    
    snake_body = []
    length_of_snake = 1
    
    food_x = random.randrange(0, WIDTH - snake_block, 10)
    food_y = random.randrange(0, HEIGHT - snake_block, 10)

    clock = pygame.time.Clock()

    while not game_over:
        while game_close:
            win.fill(BLACK)
            game_over_message()
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0
        
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True
        
        x += x_change
        y += y_change
        win.fill(BLACK)
        pygame.draw.rect(win, GREEN, [food_x, food_y, snake_block, snake_block])
        
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_body.append(snake_head)
        if len(snake_body) > length_of_snake:
            del snake_body[0]
        
        for block in snake_body[:-1]:
            if block == snake_head:
                game_close = True
        
        for block in snake_body:
            pygame.draw.rect(win, BLUE, [block[0], block[1], snake_block, snake_block])
        
        display_score(length_of_snake - 1)
        pygame.display.update()
        
        if x == food_x and y == food_y:
            food_x = random.randrange(0, WIDTH - snake_block, 10)
            food_y = random.randrange(0, HEIGHT - snake_block, 10)
            length_of_snake += 1
        
        clock.tick(snake_speed)
    
    pygame.quit()
    quit()

game_loop()
