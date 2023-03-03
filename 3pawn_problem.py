# import required modules
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

# create the game window
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Three Chess Pawns Problem")

# create the chessboard
chessboard = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# place the pawns on the chessboard
chessboard[0][0] = 1
chessboard[1][2] = 1
chessboard[2][1] = 1

# draw the chessboard and pawns
for i in range(3):
    for j in range(3):
        # draw the square
        square = pygame.Rect(j * 100, i * 100, 100, 100)
        color = BLACK if (i + j) % 2 == 0 else WHITE
        pygame.draw.rect(screen, color, square)
        
        # draw the pawn if there is one
        if chessboard[i][j] == 1:
            pawn = pygame.Rect(j * 100 + 35, i * 100 + 35, PAWN_SIZE, PAWN_SIZE)
            pygame.draw.circle(screen, PAWN_COLOR, pawn.center, int(PAWN_SIZE/2))

# update the game window
pygame.display.update()

# wait for the user to close the game window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()