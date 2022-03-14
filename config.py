import pygame
from pygame.math import Vector2


# the dimensions of the displayed window
WINDOW_SIZE = Vector2(1280-2, 640-32)
# the background color of the displayed window
WINDOW_COLOR = (30, 30, 30)

# the color of the edges of the grid
GRID_COLOR = (30, 30, 30)
# the number of cells not displayed on the sides (required)
PADDING = Vector2(5)

# the color of the cells in the grid
CELL_COLOR = (255, 255, 255)
# the dimensions of the cells in the grid
CELL_SIZE = 40

# the key to start the animation or to pause it
START_KEY = pygame.K_SPACE
# the number of images displayed per second
FPS = 60
# the speed of the animation (in frames per second)
SPEED = 0.1