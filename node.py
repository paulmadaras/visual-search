# node.py
import pygame

class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.width = width
        self.total_rows = total_rows
        self.color = (255, 255, 255)  # Default color is white
        self.neighbors = []
        self.barrier = False

    def get_pos(self):
        return self.row, self.col

    def make_start(self):
        self.color = (0, 255, 0)  # Green

    def make_end(self):
        self.color = (255, 0, 0)  # Red

    def make_visited(self):
        self.color = (173, 216, 230)  # Light Blue

    def make_barrier(self):
        self.color = (0, 0, 0)  # Black
        self.barrier = True

    def make_path(self):
        self.color = (128, 0, 128)  # Purple

    def reset(self):
        self.color = (255, 255, 255)  # White
        self.barrier = False

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.col * self.width, self.row * self.width, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1:  # Down
            self.neighbors.append(grid[self.row + 1][self.col])
        if self.row > 0:  # Up
            self.neighbors.append(grid[self.row - 1][self.col])
        if self.col < self.total_rows - 1:  # Right
            self.neighbors.append(grid[self.row][self.col + 1])
        if self.col > 0:  # Left
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        """Define less-than for priority queue."""
        return False  # Default comparison, modify as necessary
