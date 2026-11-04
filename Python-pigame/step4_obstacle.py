import pygame
import random

# Game constants
WIDTH = 800
HEIGHT = 600
FPS = 60
BACKGROUND_COLOR = (0, 0, 0)  # RGB color for the background
PLAYER_COLOR = (60, 140, 255)  # RGB color for the player
PLAYER2_COLOR = (255, 140, 60)  # RGB color for the second player
PLAYER_SPEED = 6  # Speed of the player movement

SPAWN_OBSTACLE_DELAY = 500  # Delay in milliseconds between spawning obstacles

COLORS = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (255, 165, 0),  # Orange
]

class Player:
    """The player controlled by the user"""

    def __init__(self, x, y, color=PLAYER_COLOR, speed=PLAYER_SPEED):
        """Initialize the player with a position and size"""
        self.rect = pygame.Rect(x, y, 50, 50)
        self.speed = speed
        self.color = color

    def move_arrow(self):
        """Move the player's position based on key presses"""

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def move_wasd(self):
        """Move the player's position based on WASD key presses"""

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed

    def draw(self, surface):
        """Draw the player on the given surface"""
        pygame.draw.rect(surface, self.color, self.rect)

class Obstacle:
    """An obstacle that the player must avoid"""

    def __init__(self):
        """Initialize the obstacle with a position and size"""
        size = 40
        x = random.randint(0, WIDTH - size)
        self.rect = pygame.Rect(x, -size, size, size)
        self.color = random.choice(COLORS)
        self.speed = random.randint(2, 7)

    def move(self):
        """Move the obstacle down the screen"""
        self.rect.y += self.speed

    def is_off_screen(self):
        """Check if the obstacle has moved off the screen"""
        return self.rect.y > HEIGHT

    def draw(self, surface):
        """Draw the obstacle on the given surface"""
        pygame.draw.rect(surface, self.color, self.rect)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Player Game")
clock = pygame.time.Clock()

# Create a player object
player = Player(375, 530)
player2 = Player(100, 100, color=PLAYER2_COLOR, speed=2)

obstacles = []

last_obstacle_spawn_time = pygame.time.get_ticks()


# Game loop
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Obstacle spawning logic
    current_time = pygame.time.get_ticks()
    if current_time - last_obstacle_spawn_time > SPAWN_OBSTACLE_DELAY:
        obstacles.append(Obstacle())
        last_obstacle_spawn_time = current_time

    # Update the position of each obstacle
    for obstacle in obstacles:
        obstacle.move()

    # Remove obstacles that have moved off the screen
    # obstacles = [obstacle for obstacle in obstacles if not obstacle.is_off_screen()]

    visible_obstacles = []
    for obstacle in obstacles:
        if not obstacle.is_off_screen():
            visible_obstacles.append(obstacle)
    obstacles = visible_obstacles

    # Move the player
    player.move_arrow()
    player2.move_wasd()

    screen.fill(BACKGROUND_COLOR)
    player.draw(screen)
    player2.draw(screen)
    for obstacle in obstacles:
        obstacle.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()