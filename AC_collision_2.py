import pygame
import math

# Set up the Pygame window
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Aircraft Trajectories")

# Define the aircraft class
class Aircraft:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), 10)

# Create two aircraft objects
aircraft1 = Aircraft(100, 100, 1)
aircraft2 = Aircraft(700, 500, 2)
aircraft3 = Aircraft(150, 150, 1)
aircraft4 = Aircraft(70, 500, 4)

# Define the trajectories of the aircraft
trajectory1 = [(100, 100), (400, 300), (500, 200), (700, 100)]
trajectory2 = [(700, 500), (400, 200), (200, 300), (100, 500)]
trajectory3 = [(800, 500), (200, 200), (200, 300), (100, 500)]
trajectory4 = [(750, 500), (400, 250), (200, 300), (100, 500)]

# Define the index of the current waypoint for each aircraft
waypoint_index1 = 0
waypoint_index2 = 0
waypoint_index3 = 0
waypoint_index4 = 0

# Set up the game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the aircraft towards their current waypoint
    if waypoint_index1 < len(trajectory1):
        waypoint_x, waypoint_y = trajectory1[waypoint_index1]
        dx = waypoint_x - aircraft1.x
        dy = waypoint_y - aircraft1.y
        dist = math.sqrt(dx ** 2 + dy ** 2)
        if dist < aircraft1.speed:
            waypoint_index1 += 1
        else:
            aircraft1.move(dx / dist, dy / dist)

    if waypoint_index2 < len(trajectory2):
        waypoint_x, waypoint_y = trajectory2[waypoint_index2]
        dx = waypoint_x - aircraft2.x
        dy = waypoint_y - aircraft2.y
        dist = math.sqrt(dx ** 2 + dy ** 2)
        if dist < aircraft2.speed:
            waypoint_index2 += 1
        else:
            aircraft2.move(dx / dist, dy / dist)
            
    if waypoint_index3 < len(trajectory3):
        waypoint_x, waypoint_y = trajectory3[waypoint_index3]
        dx = waypoint_x - aircraft3.x
        dy = waypoint_y - aircraft3.y
        dist = math.sqrt(dx ** 2 + dy ** 2)
        if dist < aircraft3.speed:
            waypoint_index3 += 1
        else:
            aircraft3.move(dx / dist, dy / dist)

    # Check for collisions between the aircraft
    dx = aircraft1.x - aircraft2.x
    dy = aircraft1.y - aircraft2.y
    dist = math.sqrt(dx ** 2 + dy ** 2)
    if dist < 20:
        print("Collision detected!")
        running = False

    # Draw the aircraft and the waypoints
    screen.fill((255, 255, 255))
    for waypoint_x, waypoint_y in trajectory1 + trajectory2 + trajectory3 + trajectory4:
        pygame.draw.circle(screen, (0, 0, 255), (int(waypoint_x), int(waypoint_y)), 5)
    aircraft1.draw(screen)
    aircraft2.draw(screen)
    aircraft3.draw(screen)
    aircraft4.draw(screen)
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Clean up
pygame.quit()