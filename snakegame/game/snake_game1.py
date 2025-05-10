# filename: snake_game.py
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Define block size and FPS
block_size = 20
fps = 10

# Function to draw the snake
def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(game_window, green, [x, y, block_size, block_size])

# Function to move the snake
def move_snake(direction, snake_head):
    if direction == 'UP':
        snake_head[1] -= block_size
    elif direction == 'DOWN':
        snake_head[1] += block_size
    elif direction == 'LEFT':
        snake_head[0] -= block_size
    elif direction == 'RIGHT':
        snake_head[0] += block_size

# Function to generate food
def generate_food():
    food_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size
    return food_x, food_y

# Function to check collision between snake head and food
def check_collision(snake_head, food_x, food_y):
    if snake_head[0] == food_x and snake_head[1] == food_y:
        return True
    return False

# Function to check game over conditions
def is_game_over(snake_head, snake_list):
    if (snake_head[0] >= screen_width or snake_head[0] < 0 or
        snake_head[1] >= screen_height or snake_head[1] < 0):
        return True
    for segment in snake_list[:-1]:
        if segment == snake_head:
            return True
    return False

# Function to show score
font = pygame.font.SysFont(None, 50)
def show_score(score):
    score_text = font.render(f'Score: {score}', True, white)
    game_window.blit(score_text, [0, 0])

# Main game loop
def main():
    game_over = False
    game_exit = False
    direction = 'RIGHT'
    snake_head = [100, 50]
    snake_list = [snake_head]
    snake_length = 1
    food_x, food_y = generate_food()
    score = 0
    clock = pygame.time.Clock()

    while not game_exit:
        while game_over:
            game_window.fill(black)
            message = font.render('Game Over! Press Q-Quit or C-Play Again', True, red)
            game_window.blit(message, [screen_width / 6, screen_height / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        main()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'

        move_snake(direction, snake_head)
        snake_list.append(list(snake_head))

        if len(snake_list) > snake_length:
            del snake_list[0]

        if is_game_over(snake_head, snake_list):
            game_over = True

        if check_collision(snake_head, food_x, food_y):
            food_x, food_y = generate_food()
            snake_length += 1
            score += 1

        game_window.fill(black)
        pygame.draw.rect(game_window, red, [food_x, food_y, block_size, block_size])
        draw_snake(snake_list)
        show_score(score)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()