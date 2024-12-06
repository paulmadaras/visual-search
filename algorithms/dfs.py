# dfs.py
import pygame
import time

def dfs(draw, grid, start, end, speed):
    stack = [start]
    visited = set()

    while stack:
        pygame.event.pump()  # Handle events to prevent freezing
        current = stack.pop()

        if current not in visited:
            visited.add(current)
            current.make_visited()
            draw()  # Update the display

            # Delay for visualization
            time.sleep(speed)

            if current == end:
                return True  # Found the end

            for neighbor in current.neighbors:
                if neighbor not in visited and not neighbor.barrier:
                    stack.append(neighbor)

    return False  # No path found
