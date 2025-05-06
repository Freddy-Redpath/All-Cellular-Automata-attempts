import random
import numpy as np
import pygame
from pygame.locals import *
import colorsys

w = 30
width, height = 900, 600
rows, cols = width // w, height // w
grid = np.zeros((rows, cols), dtype=int)
clock = pygame.time.Clock()
Window = pygame.display.set_mode((width, height))
showGrid = False


def calculateNeigbours(cx, cy):
    neigbourSum = 0
    dormentSum = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:  # Skip the current cell
                continue
            nx, ny = (cx + x) % rows, (cy + y) % cols
            if grid[nx][ny] == 1:
                dormentSum +=1
            if grid[nx][ny] == 2:
                neigbourSum += 1

    return neigbourSum, dormentSum


def draw():
    Window.fill((255, 255, 255))
    global showGrid
    # Draw the sand
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == 2:
                color = (36, 128, 36)
                pygame.draw.rect(Window, color, (x * w, y * w, w, w))
            elif grid[x][y] == 1:
                color = (100, 128, 100)
                pygame.draw.rect(Window, color, (x * w, y * w, w, w))
            elif grid[x][y] == 0:
                color = (255, 255, 255)
                pygame.draw.rect(Window, color, (x * w, y * w, w, w))
    if showGrid:
        drawGrid()
    pygame.display.flip()


def drawGrid():
    color = (128, 128, 128)
    for x in range(0, width // w):
        for y in range(0, height // w):
            pygame.draw.line(Window, color, (x * w, y), (x * w, height))
            pygame.draw.line(Window, color, (x, y * w), (width, y * w))


def initiateGrid():
    for x in range(rows):
        for y in range(cols):
            grid[x][y] = random.randint(0,2)





def setCell(screenX, screenY):
    gridPosX, gridPosY = int(screenX / w), int(screenY / w)

    if grid[gridPosX][gridPosY] == 2:
        grid[gridPosX][gridPosY] = 1

    elif grid[gridPosX][gridPosY] == 1:
        grid[gridPosX][gridPosY] = 0

    elif grid[gridPosX][gridPosY] == 0:
        grid[gridPosX][gridPosY] = 2


    draw()


def main():
    pygame.init()
    initiateGrid()

    running = True
    paused = False
    while running:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p or event.key == pygame.K_SPACE:
                    paused = not paused
                if event.key == pygame.K_g:
                    global showGrid
                    showGrid = not showGrid

                    draw()
            if event.type == pygame.MOUSEBUTTONDOWN and paused:
                mousePosition = pygame.mouse.get_pos()

                setCell(mousePosition[0], mousePosition[1])

            if event.type == QUIT:
                running = False
        if not paused:
            newGrid = np.zeros_like(grid)
            for x in range(rows):
                for y in range(cols):
                    neigbours, dormentNeigbours = calculateNeigbours(x, y)
                    if grid[x][y] == 0:  # Dead cell
                        if neigbours == 3:
                            newGrid[x][y] = 2  # Becomes alive
                        else:
                            newGrid[x][y] = 0  # Stays dead

                    elif grid[x][y] == 1:  # Dormant cell
                        if neigbours >= 4:
                            newGrid[x][y] = 2  # Becomes alive
                        else:
                            newGrid[x][y] = 1  # Stays dormant

                    elif grid[x][y] == 2:  # Alive cell
                        if 2 <= neigbours <= 3:
                            newGrid[x][y] = 2  # Stays alive
                        elif neigbours < 2:
                            newGrid[x][y] = 1  # Becomes dormant
                        else:
                            newGrid[x][y] = 0  # Dies

            grid[:] = newGrid
        draw()
        clock.tick(1)


if __name__ == "__main__":
    main()
