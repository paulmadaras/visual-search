import pygame
import sys
from algorithms import dfs, bfs, ucs, dijkstra, a_star
from node import Node

# Settings
WIDTH = 600
ROWS = 30
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pathfinding Visualization")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Helper Functions
def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)
    return grid

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, BLACK, (0, i * gap), (width, i * gap))
        pygame.draw.line(win, BLACK, (i * gap, 0), (i * gap, width))

def draw(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw(win)
    draw_grid(win, rows, width)
    pygame.display.update()

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    x, y = pos
    row = min(rows - 1, y // gap)  # Ensure row index is within bounds
    col = min(rows - 1, x // gap)  # Ensure col index is within bounds
    return row, col

def reset_grid(grid):
    for row in grid:
        for node in row:
            node.reset()

def main(win, width):
    grid = make_grid(ROWS, width)

    start = None
    end = None

    running = True
    while running:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            # Left mouse click to set start, end, and barriers
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)

                # Ensure row and col are valid before accessing the grid
                if 0 <= row < ROWS and 0 <= col < ROWS:
                    node = grid[row][col]
                    if not start and node != end:
                        start = node
                        start.make_start()
                    elif not end and node != start:
                        end = node
                        end.make_end()
                    elif node != end and node != start:
                        node.make_barrier()

            # Right mouse click to reset a node
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)

                # Ensure row and col are valid before accessing the grid
                if 0 <= row < ROWS and 0 <= col < ROWS:
                    node = grid[row][col]
                    node.reset()
                    if node == start:
                        start = None
                    elif node == end:
                        end = None

            # Keyboard actions for running algorithms
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    a_star.a_star(lambda: draw(win, grid, ROWS, width), grid, start, end, speed=0.05)

                elif event.key == pygame.K_d and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    dijkstra.dijkstra(lambda: draw(win, grid, ROWS, width), grid, start, end, speed=0.05)

                elif event.key == pygame.K_b and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    bfs.bfs(lambda: draw(win, grid, ROWS, width), grid, start, end, speed=0.05)

                elif event.key == pygame.K_u and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    ucs.ucs(lambda: draw(win, grid, ROWS, width), grid, start, end, speed=0.05)

                elif event.key == pygame.K_f and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    dfs.dfs(lambda: draw(win, grid, ROWS, width), grid, start, end, speed=0.05)

                elif event.key == pygame.K_r:
                    start = None
                    end = None
                    reset_grid(grid)

    pygame.quit()

main(WIN, WIDTH)
