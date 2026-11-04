import pygame

# Game constants
WIDTH = 800
HEIGHT = 600
FPS = 60
BACKGROUND_COLOR = (0, 0, 0)  # RGB color for the background
PLAYER_COLOR = (60, 140, 255)  # RGB color for the player

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title of the window
pygame.display.set_caption("Moving Player Game")

# Set up the player rectangle (x, y, width, height)
player_rect = pygame.Rect(375,530,50,50)

player_speed = 6

# Set up the clock for controlling the frame rate
clock = pygame.time.Clock()

# Main loop
running = True

while running:
    # Handle events
    # Get all events (keyboard, mouse, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed

    # Fill the screen with a color (RGB)
    screen.fill(BACKGROUND_COLOR)

    # Draw the player
    pygame.draw.rect(screen, PLAYER_COLOR, player_rect)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate to 60 frames per second
    clock.tick(FPS)

# Quit Pygame
pygame.quit()