# Pathfinding Visualization Tool

This program allows you to visualize different pathfinding algorithms on a grid-based interface. It provides an interactive way to understand how each algorithm explores the grid to find the shortest path between a start and an end node.

## Features
You can use the following **keyboard keys** to run the corresponding pathfinding algorithm:

- **`SPACE`**: Run **A* (A-Star)** algorithm.
- **`D`**: Run **Dijkstra's** algorithm.
- **`B`**: Run **Breadth-First Search (BFS)**.
- **`U`**: Run **Uniform Cost Search (UCS)**.
- **`F`**: Run **Depth-First Search (DFS)**.
- **`R`**: Reset the grid, clearing all nodes and barriers.

---

## How to Use
Follow these steps to use the visualization tool:

1. **Set Start Node**:  
   Left-click on a cell to mark it as the start node (green).

2. **Set End Node**:  
   Left-click on a different cell to mark it as the end node (red).

3. **Create Barriers**:  
   Left-click on any other cells to turn them into barriers (black).

4. **Choose an Algorithm**:  
   Press one of the following keys to visualize the corresponding algorithm:
   - `SPACE` for **A* (A-Star)**.
   - `D` for **Dijkstra's Algorithm**.
   - `B` for **Breadth-First Search (BFS)**.
   - `U` for **Uniform Cost Search (UCS)**.
   - `F` for **Depth-First Search (DFS)**.

5. **Reset the Grid**:  
   Press **`R`** to clear all nodes, barriers, and paths and restart the visualization.

---

## Requirements
- **Python 3.x**
- **Pygame** library (install via `pip install pygame`)

---

## How to Run
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the following command to start the program:
   ```bash
   python main.py
