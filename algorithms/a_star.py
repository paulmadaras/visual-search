# a_star.py
import time
import heapq
import pygame


def heuristic(node1, node2):
    x1, y1 = node1.get_pos()
    x2, y2 = node2.get_pos()
    return abs(x1 - x2) + abs(y1 - y2)

def a_star(draw, grid, start, end, speed):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {node: float('inf') for row in grid for node in row}
    g_score[start] = 0
    f_score = {node: float('inf') for row in grid for node in row}
    f_score[start] = heuristic(start, end)

    while open_set:
        pygame.event.pump()  # Handle events to prevent freezing
        current = heapq.heappop(open_set)[1]

        if current == end:
            break

        for neighbor in current.neighbors:
            if not neighbor.barrier:
                tentative_g_score = g_score[current] + 1
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                    if neighbor not in [i[1] for i in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))

        current.make_visited()
        draw()  # Update the display
        time.sleep(speed)  # Delay for visualization

    # Reconstruct path
    current = end
    while current in came_from:
        current = came_from[current]
        current.make_path()

    return True if current == end else False
