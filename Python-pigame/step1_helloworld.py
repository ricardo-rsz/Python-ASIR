import pygame

# Windows dimensions
WIDTH = 800
HEIGHT = 600

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title of the window
pygame.display.set_caption("Hello World my first game")

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

    # Fill the screen with a color (RGB)
    screen.fill((100, 200, 250))  # Blue background

    # Update the display
    pygame.display.flip()

    # Limit the frame rate to 60 frames per second
    clock.tick(60)

# Quit Pygame
pygame.quit()