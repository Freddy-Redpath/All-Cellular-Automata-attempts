from perlin_noise import PerlinNoise
import numpy as np
##UPDATE PYCHARM
# Parameters
width = 900
height = 600
z_min = 0
z_max = 2
noise = PerlinNoise(octaves=4, seed=42)  # Configure Perlin noise

# Generate 900x600 grid of noise values
grid = np.zeros((height, width))

# Fill the grid with Perlin noise
for y in range(height):
    for x in range(width):
        grid[y, x] = noise([x / width, y / height])

# Translate the noise values to (x, y, z) coordinates
coordinates = []
for y in range(height):
    for x in range(width):
        z = round(np.interp(grid[y, x], [-1, 1], [z_min, z_max]))  # Interpolate and round to 0, 1, or 2
        coordinates.append((x, y, z))

# Show the first few coordinates
print(coordinates[:10])  # Print first 10 coordinates as an example
