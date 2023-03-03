import pygame
import math
from queue import Queue

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

    def get_pos(self):
        return (self.x, self.y)

# Create two aircraft objects
aircraft1 = Aircraft(100, 100, 1)
aircraft2 = Aircraft(700, 500, 1)

# Define the trajectories of the aircraft
trajectory1 = [(100, 100), (400, 300), (500, 200), (700, 100)]
trajectory2 = [(700, 500), (400, 200), (200, 300), (100, 500)]

# Define the index of the current waypoint for each aircraft
waypoint_index1 = 0
waypoint_index2 = 0

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

    # Check for collisions between the aircraft
    dx = aircraft1.x - aircraft2.x
    dy = aircraft1.y - aircraft2.y
    dist = math.sqrt(dx ** 2 + dy ** 2)
    if dist < 20:
        print("Collision detected!")
        
        # Use BFS to find a new trajectory and velocity for each aircraft to avoid collision
        def bfs(aircraft, other_aircraft, trajectory):
            visited = set()
            q = Queue()
            q.put((trajectory[0], [trajectory[0]], aircraft.speed))
            
            while not q.empty():
                pos, path, speed = q.get()
                if pos in visited:
                    continue
                visited.add(pos)
                
                # Check if this position is too close to the other aircraft
                other_pos = other_aircraft.get_pos()
                dx = pos[0] - other_pos[0]
                dy = pos[1] - other_pos[1]

				dist = math.sqrt(dx ** 2 + dy ** 2)
				if dist < 20:
					# If the position is too close, try reducing the speed
					if speed > 0.1:
						q.put((pos, path, speed * 0.9))
					continue
				
				# Check if we've reached the end of the trajectory
				if pos == trajectory[-1]:
					return path
				
				# Add neighboring positions to the queue
				x, y = pos
				for dx in [-speed, 0, speed]:
					for dy in [-speed, 0, speed]:
						new_pos = (x + dx, y + dy)
						if new_pos in visited or new_pos[0] < 0 or new_pos[0] > screen_width or new_pos[1] < 0 or new_pos[1] > screen_height:
							continue
						q.put((new_pos, path + [new_pos], speed))
			
			# If we can't find a path, return the original trajectory
			return trajectory
        
        new_trajectory1 = bfs(aircraft1, aircraft2, trajectory1)
        new_trajectory2 = bfs(aircraft2, aircraft1, trajectory2)
        
        # Reset the waypoint index for each aircraft
        waypoint_index1 = 0
        waypoint_index2 = 0
        
        # Update the trajectories
        trajectory1 = new_trajectory1
        trajectory2 = new_trajectory2

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the aircraft
    aircraft1.draw(screen)
    aircraft2.draw(screen)

    # Draw the trajectories
    pygame.draw.lines(screen, (0, 0, 255), False, trajectory1, 2)
    pygame.draw.lines(screen, (0, 255, 0), False, trajectory2, 2)

    # Update the display
    pygame.display.flip()

    # Delay to maintain a constant frame rate
    clock.tick(60)

# Clean up
pygame.quit()
This code first checks for collisions between the two aircraft. If a collision is detected, it uses the BFS algorithm to find a new trajectory and velocity for each aircraft to avoid the collision. The bfs function takes as input the current aircraft, the other aircraft, and the current trajectory, and returns a new trajectory that avoids the other aircraft.

The bfs function uses a breadth-first search to explore neighboring positions in the game world, starting from the current position. If a neighboring position is too close to the other aircraft, the function tries reducing the speed of the current aircraft to avoid a collision. If a new trajectory is found, the function returns it. Otherwise, it returns the original trajectory.

Once new trajectories are found, the code resets the waypoint index for each aircraft and updates the trajectories. The aircraft are then moved along their new trajectories as before.