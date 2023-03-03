import random
import time
def bfs(maze, start):
    queue = [(start, [start])]
    visited = set()
    while queue:
        (current_row, current_col), path = queue.pop(0)
        if maze[current_row][current_col] == "S":
            return path
        if (current_row, current_col) not in visited:
            visited.add((current_row, current_col))
            for (row_offset, col_offset) in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                neighbor_row = current_row + row_offset
                neighbor_col = current_col + col_offset
                if (0 <= neighbor_row < len(maze) and
                        0 <= neighbor_col < len(maze[0]) and
                        maze[neighbor_row][neighbor_col] != 'X' and
                        (neighbor_row, neighbor_col) not in visited):
                    if maze[neighbor_row][neighbor_col] == 'E':
                        # If the neighbor is an enchanted square, randomly teleport to another square
                        teleport_row, teleport_col = teleport(maze, visited)
                        queue.append(((teleport_row, teleport_col), path + [(teleport_row, teleport_col)]))
                    else:
                        # Otherwise, add the neighbor to the queue
                        queue.append(((neighbor_row, neighbor_col), path + [(neighbor_row, neighbor_col)]))
    # If no path was found, return None
    return None


def teleport(maze, visited):
    # Find a random square that is not a wall or a visited square
    while True:
        teleport_row = random.randint(0, len(maze) - 1)
        teleport_col = random.randint(0, len(maze[0]) - 1)
        if maze[teleport_row][teleport_col] != 'X' and (teleport_row, teleport_col) not in visited:
            return teleport_row, teleport_col

graph = ["X.XXXX.",
"X.....E",
"XXXXXX.",
".......",
"E.....S",
".X.XXXX"]


path = bfs(graph, (1,1))

import pygame
import sys

# initialize pygame
pygame.init()

# define constants
SCREEN_SIZE = (300, 300)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PAWN_SIZE = 30
PAWN_COLOR = (255, 0, 0)


screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Three Chess Pawns Problem")
clock = pygame.time.Clock()

# Draw the maze
position_index = 0
while position_index < (len(path)-1)  :
    for i in range(6):
        for j in range(7):
            if graph[i][j] == ".":
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(j * 30, i * 30, 30, 30))
            if graph[i][j] == "E":
                pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(j * 30, i * 30, 30, 30))   
            if graph[i][j] == "S":
                pygame.draw.rect(screen, (255, 0, 255), pygame.Rect(j * 30, i * 30, 30, 30))  
            if (i,j) == path[position_index]:
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(j * 30, i * 30, 30, 30))    
    position_index += 1 
 
    clock.tick(60)
    time.sleep(1)
    pygame.display.flip()
    #pygame.display.update()

pygame.quit()