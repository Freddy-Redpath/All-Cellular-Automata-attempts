import random
import numpy as np
import pygame
from pygame.locals import *
import colorsys
# Constants
w = 5
hueValue = 200
gravity = 0.1


# Check if a row is within the bounds
def within_cols(i):
    return 0 <= i <= cols - 1


# Check if a column is within the bounds
def within_rows(j):
    return 0 <= j <= rows - 1


# Create a 2D array
def make_2D_array(cols, rows):
    return [[0 for _ in range(rows)] for _ in range(cols)]
def make_2D_col_array(cols, rows):
    return [[(random.randint(230,255),random.randint(230,255),120) for _ in range(rows)] for _ in range(cols)]
def make_2D_bool_array(cols, rows):
    return [[False for _ in range(rows)] for _ in range(cols)]


# Initialize Pygame
pygame.init()

# Setup
width, height = 1280, 768
cols, rows = width // w, height // w
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
bg_image = pygame.image.load('background.jpg')
bg_image = pygame.transform.scale(bg_image, (width, height))
# Create grid and velocity grid
grid = make_2D_bool_array(cols, rows)
velocity_grid = make_2D_array(cols, rows)
color_Grid = make_2D_col_array(cols,rows)

def draw():
    screen.blit(bg_image, (0, 0))

    # Draw the sand
    for i in range(cols):
        for j in range(rows):
            if grid[i][j] > 0:
                # Convert HSB to RGB
                '''
                rgb_color = colorsys.hsv_to_rgb(grid[i][j] / 360, 1, 1)
                color = tuple(int(c * 255) for c in rgb_color)
                '''
                color = color_Grid[i][j]
                pygame.draw.rect(screen, color, (i * w, j * w, w, w))


    pygame.display.flip()


def main():
    global grid, velocity_grid, hueValue

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        if pygame.mouse.get_pressed()[0]:
            mouse_col, mouse_row = pygame.mouse.get_pos()[0] // w, pygame.mouse.get_pos()[1] // w

            # Randomly add an area of sand particles
            matrix = 10
            extent = matrix // 2
            for i in range(-extent, extent + 1):
                for j in range(-extent, extent + 1):
                    if random.random() < 0.75:
                        col, row = mouse_col + i, mouse_row + j
                        if within_cols(col) and within_rows(row):
                            grid[col][row] = hueValue
                            velocity_grid[col][row] = 1

            # Change the color of the sand over time
            hueValue += 0.5
            if hueValue > 360:
                hueValue = 1

        # Draw the sand
        draw()

        # Create a 2D array for the next frame of animation
        next_grid = make_2D_array(cols, rows)
        next_velocity_grid = make_2D_array(cols, rows)

        # Check every cell
        for i in range(cols):
            for j in range(rows):
                state = grid[i][j]
                velocity = velocity_grid[i][j]
                moved = False
                if state:
                    new_pos = int(j + velocity)
                    for y in range(new_pos, j, -1):
                        if 0 <= y < rows:  # Check if y is within bounds
                            below = grid[i][y]
                            dir = 1 if random.random() < 0.5 else -1
                            below_a = grid[i + dir][y] if within_cols(i + dir) else -1
                            below_b = grid[i - dir][y] if within_cols(i - dir) else -1

                            if below == False:
                                next_grid[i][y] = state
                                next_velocity_grid[i][y] = velocity + gravity
                                moved = True
                                break
                            elif below_a == False:
                                next_grid[i + dir][y] = state
                                next_velocity_grid[i + dir][y] = velocity + gravity
                                moved = True
                                break
                            elif below_b == False:
                                next_grid[i - dir][y] = state
                                next_velocity_grid[i - dir][y] = velocity + gravity
                                moved = True
                                break

                if state and not moved:
                    next_grid[i][j] = grid[i][j]
                    next_velocity_grid[i][j] = velocity_grid[i][j] + gravity

        grid = next_grid
        velocity_grid = next_velocity_grid

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
