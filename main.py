import pygame
import sys
from algorithms import dfs, bfs, ucs, dijkstra, a_star
from node import Node

# Constants
GRID_SIZE = 30
SCREEN_SIZE = 600
SCREEN = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Pathfinding Visualizer")

# Colors
COLOR_BG = (255, 255, 255)
COLOR_GRID = (0, 0, 0)

# Create the grid structure
def build_grid(size, dimension):
    spacing = dimension // size
    return [[Node(row, col, spacing, size) for col in range(size)] for row in range(size)]

# Draw grid lines
def render_gridlines(display, size, dimension):
    spacing = dimension // size
    for line in range(size):
        pygame.draw.line(display, COLOR_GRID, (0, line * spacing), (dimension, line * spacing))
        pygame.draw.line(display, COLOR_GRID, (line * spacing, 0), (line * spacing, dimension))

# Display elements and grid
def render(display, grid, size, dimension):
    display.fill(COLOR_BG)
    for row in grid:
        for cell in row:
            cell.draw(display)
    render_gridlines(display, size, dimension)
    pygame.display.update()

# Calculate grid coordinates from mouse position
def get_cell_coordinates(position, size, dimension):
    spacing = dimension // size
    x, y = position
    return min(size - 1, y // spacing), min(size - 1, x // spacing)

# Clear the grid to default state
def clear_grid(grid):
    for row in grid:
        for cell in row:
            cell.reset()

# Main program logic
def main_program(display, dimension):
    grid = build_grid(GRID_SIZE, dimension)
    start_node = None
    end_node = None
    running = True

    while running:
        render(display, grid, GRID_SIZE, dimension)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            # Mouse input for start, end, and barriers
            if pygame.mouse.get_pressed()[0]:
                position = pygame.mouse.get_pos()
                row, col = get_cell_coordinates(position, GRID_SIZE, dimension)

                if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
                    current_node = grid[row][col]
                    if not start_node and current_node != end_node:
                        start_node = current_node
                        start_node.make_start()
                    elif not end_node and current_node != start_node:
                        end_node = current_node
                        end_node.make_end()
                    elif current_node != start_node and current_node != end_node:
                        current_node.make_barrier()

            # Mouse input to reset nodes
            elif pygame.mouse.get_pressed()[2]:
                position = pygame.mouse.get_pos()
                row, col = get_cell_coordinates(position, GRID_SIZE, dimension)

                if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
                    current_node = grid[row][col]
                    current_node.reset()
                    if current_node == start_node:
                        start_node = None
                    elif current_node == end_node:
                        end_node = None

            # Keyboard input for algorithms and reset
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start_node and end_node:
                    for row in grid:
                        for cell in row:
                            cell.update_neighbors(grid)
                    a_star.a_star(lambda: render(display, grid, GRID_SIZE, dimension), grid, start_node, end_node, speed=0.1)

                elif event.key == pygame.K_d and start_node and end_node:
                    for row in grid:
                        for cell in row:
                            cell.update_neighbors(grid)
                    dijkstra.dijkstra(lambda: render(display, grid, GRID_SIZE, dimension), grid, start_node, end_node, speed=0.1)

                elif event.key == pygame.K_b and start_node and end_node:
                    for row in grid:
                        for cell in row:
                            cell.update_neighbors(grid)
                    bfs.bfs(lambda: render(display, grid, GRID_SIZE, dimension), grid, start_node, end_node, speed=0.1)

                elif event.key == pygame.K_u and start_node and end_node:
                    for row in grid:
                        for cell in row:
                            cell.update_neighbors(grid)
                    ucs.ucs(lambda: render(display, grid, GRID_SIZE, dimension), grid, start_node, end_node, speed=0.1)

                elif event.key == pygame.K_f and start_node and end_node:
                    for row in grid:
                        for cell in row:
                            cell.update_neighbors(grid)
                    dfs.dfs(lambda: render(display, grid, GRID_SIZE, dimension), grid, start_node, end_node, speed=0.1)

                elif event.key == pygame.K_r:
                    start_node = None
                    end_node = None
                    clear_grid(grid)

    pygame.quit()

main_program(SCREEN, SCREEN_SIZE)
