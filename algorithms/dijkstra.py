# dijkstra.py
import time
import heapq
import pygame

def dijkstra(draw, grid, start, end, speed):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    cost_so_far = {start: 0}

    while open_set:
        pygame.event.pump()  # Handle events to prevent freezing
        current_cost, current = heapq.heappop(open_set)

        if current == end:
            break

        for neighbor in current.neighbors:
            if not neighbor.barrier:
                new_cost = cost_so_far[current] + 1
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    heapq.heappush(open_set, (new_cost, neighbor))  # Change priority
                    came_from[neighbor] = current

        current.make_visited()
        draw()  # Update the display
        time.sleep(speed)  # Delay for visualization

    # Reconstruct path
    current = end
    while current in came_from:
        current = came_from[current]
        current.make_path()

    return True if current == end else False
