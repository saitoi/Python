import pygame
import random
import sys
import time

# Initialize Pygame
pygame.init()

# Game variables
width, height = 640, 480
snake_size = 10
food_size = 10
snake_speed = 15

# Colors
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Game window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Python Snake Game')

clock = pygame.time.Clock()

# Snake
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

# Food
food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
food_spawn = True

score = 0

# Direction control
direction = 'RIGHT'
change_to = direction

def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (width / 2, height / 4)
    screen.fill(white)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Changing direction
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    elif change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    elif change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    elif change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_pos[1] -= 10
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    # Update the display
    pygame.display.update()

    # Control the game speed
    clock.tick(snake_speed)

    # Check for game over
    for block in snake_body[1:]:
        if block == snake_pos:
            game_over()
