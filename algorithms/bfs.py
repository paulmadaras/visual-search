# bfs.py
import pygame
import time
from collections import deque

def bfs(draw, grid, start, end, speed):
    queue = deque([start])
    visited = set()

    while queue:
        pygame.event.pump()  # Handle events to prevent freezing
        current = queue.popleft()

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
                    queue.append(neighbor)

    return False  # No path found
