import pygame
import random
import time

# Initialize pygame
pygame.init()

# Constants
WIDTH = 288
HEIGHT = 512

BIRD_WIDTH = 50
BIRD_HEIGHT = 50
PIPE_WIDTH = 70
PIPE_GAP = 200

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

# Load / initialize the images
background_image = pygame.image.load('game_objects/background-day.png')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
screen.blit(background_image, (0, 0))

bird_y = HEIGHT // 2
bird_y_change = 0

pipes = []

bird_image = pygame.image.load('game_objects/yellowbird-midflap.png')
bird_image = pygame.transform.scale(bird_image, (BIRD_WIDTH, BIRD_HEIGHT))

bird_down_image = pygame.image.load('game_objects/yellowbird-downflap.png')
bird_down_image = pygame.transform.scale(bird_image, (BIRD_WIDTH, BIRD_HEIGHT))

bird_up_image = pygame.image.load('game_objects/yellowbird-upflap.png')
bird_up_image = pygame.transform.scale(bird_image, (BIRD_WIDTH, BIRD_HEIGHT))

pipe_bottom_image = pygame.image.load('game_objects/pipe-green.png')
pipe_top_flipped_image = pygame.transform.flip(pipe_bottom_image, False, True)


# functions
def create_pipe():
    pipe_height = random.randint(100, 400)
    pipes.append({'x': WIDTH, 'top': pipe_height - PIPE_WIDTH, 'bottom': pipe_height + PIPE_GAP})

def move_pipes():
    for pipe in pipes:
        pipe['x'] -= 5

def draw_pipes():
    for pipe in pipes:
        screen.blit(pipe_top_flipped_image, (pipe['x'], pipe['top'] - pipe_top_flipped_image.get_height()))
        screen.blit(pipe_bottom_image, (pipe['x'], pipe['bottom']))

def check_collision(bird_y):
    for pipe in pipes:
        if (WIDTH // 2) + BIRD_WIDTH > pipe['x'] > (WIDTH // 2) - PIPE_WIDTH:
            if bird_y <= pipe['top'] or (bird_y + BIRD_HEIGHT) >= pipe['bottom']:
                return True
    if bird_y <= 0 or bird_y >= HEIGHT:
        return True
    return False


create_pipe()
# Game loop
running = True
time.sleep(2) # Delay to the game before starting it on the screen
while running:
    screen.blit(background_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_y_change = -10
    bird_y_change += 0.5
    bird_y += bird_y_change
    
    screen.blit(bird_image, (WIDTH // 2, bird_y))
    
    move_pipes()
    draw_pipes()

    if pipes[0]['x'] + PIPE_WIDTH < 0:
        pipes.pop(0)
        create_pipe()

    if check_collision(bird_y):
        running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
