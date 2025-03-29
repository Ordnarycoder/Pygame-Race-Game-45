import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Race Game with Obstacles and Buffs")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Car settings
CAR_WIDTH, CAR_HEIGHT = 50, 100
car_x = SCREEN_WIDTH // 2 - CAR_WIDTH // 2
car_y = SCREEN_HEIGHT - CAR_HEIGHT - 10
car_speed = 5

# Obstacle settings
obstacle_width, obstacle_height = 50, 100
obstacle_speed = 5
obstacle_list = []

# Buff settings
buff_list = []
BUFF_EFFECT = -1  # Example: reduce car speed by 1 when buff is collected

# Create custom events
ADD_OBSTACLE_EVENT = pygame.USEREVENT + 1
ADD_BUFF_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(ADD_OBSTACLE_EVENT, 1500)  # Add an obstacle every 1500 ms
pygame.time.set_timer(ADD_BUFF_EVENT, 5000)        # Add a buff every 5000 ms

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == ADD_OBSTACLE_EVENT:
            # Create a new obstacle at a random x position (starting above the screen)
            obs_x = random.randint(0, SCREEN_WIDTH - obstacle_width)
            obs_y = -obstacle_height  # Start off-screen (above)
            obstacle_list.append(pygame.Rect(obs_x, obs_y, obstacle_width, obstacle_height))
            # Increase speeds to gradually ramp up difficulty
            car_speed += 0.2
            obstacle_speed += 0.2
        elif event.type == ADD_BUFF_EVENT:
            # Create a buff at a random x position (starting above the screen)
            buff_x = random.randint(0, SCREEN_WIDTH - obstacle_width)
            buff_y = -obstacle_height
            buff_rect = pygame.Rect(buff_x, buff_y, obstacle_width, obstacle_height)
            buff_list.append(buff_rect)
    
    # Handle key presses for car movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= car_speed
    if keys[pygame.K_RIGHT]:
        car_x += car_speed

    # Keep the car within screen boundaries
    car_x = max(0, min(car_x, SCREEN_WIDTH - CAR_WIDTH))
    
    # Update obstacles: move them downwards
    new_obstacles = []
    for obstacle in obstacle_list:
        obstacle.y += obstacle_speed
        if obstacle.y < SCREEN_HEIGHT:
            new_obstacles.append(obstacle)
    obstacle_list = new_obstacles

    # Update buffs: move them downwards
    new_buffs = []
    for buff in buff_list:
        buff.y += obstacle_speed  # Same speed as obstacles; adjust if needed
        if buff.y < SCREEN_HEIGHT:
            new_buffs.append(buff)
    buff_list = new_buffs

    # Create a rectangle for the car to check for collisions
    car_rect = pygame.Rect(car_x, car_y, CAR_WIDTH, CAR_HEIGHT)
    
    # Check for collision with obstacles
    for obstacle in obstacle_list:
        if car_rect.colliderect(obstacle):
            print("Collision with obstacle detected! Game Over.")
            running = False

    # Check for collision with buffs
    # If collision happens, apply buff effect (for example, reduce car speed) and remove buff
    for buff in buff_list:
        if car_rect.colliderect(buff):
            print("Buff collected!")
            car_speed = max(5, car_speed + BUFF_EFFECT)  # Ensure car speed doesn't drop below a minimum value
            buff_list.remove(buff)  # Remove buff after collection

    # Drawing
    screen.fill((50, 50, 50))  # Fill the background (gray)

    # Draw the car (red rectangle)
    pygame.draw.rect(screen, (255, 0, 0), car_rect)

    # Draw obstacles (green rectangles)
    for obstacle in obstacle_list:
        pygame.draw.rect(screen, (0, 255, 0), obstacle)

    # Draw buffs (blue rectangles)
    for buff in buff_list:
        pygame.draw.rect(screen, (0, 0, 255), buff)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate to 60 FPS
    clock.tick(60)

pygame.quit()
sys.exit()
