#Conway's Game of Life

# Author: Drew-Woodz
# Date: June 3, 2023
# Version: 2.0
# License: MIT
# Usage: python main.py
# Notes: This is a simple implementation of Conway's Game of Life in Python using numpy and matplotlib.
#        The initial grid is a 300x300 matrix with 45000 random living cells.
#        The grid is updated every 0.05 seconds.
#        The simulation can be stopped by pressing Ctrl+C.
#        The code is available at https://github.com/Drew-Woodz/GAMEofLIFE
#        The rules of the game are as follows:
#        1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
#        2. Any live cell with two or three live neighbours lives on to the next generation.
#        3. Any live cell with more than three live neighbours dies, as if by overpopulation.
#        4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

import matplotlib.pyplot as plt
import numpy as np

class Grid:
    def __init__(self, size, n):
        # Initialize the grid with all cells dead
        self.grid = np.zeros((size, size))
        # Add a glider
        self.grid[1, 2] = 1
        self.grid[2, 0] = 1
        self.grid[2, 2] = 1
        self.grid[3, 1] = 1
        self.grid[3, 2] = 1

        for _ in range(n):
            # Randomly choose a cell
            i, j = np.random.randint(0, size, 2)
            self.grid[i, j] = 1

    def next_state(self):
        new_grid = self.grid.copy()

        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1]):
                total = (self.grid[i, (j-1)%self.grid.shape[0]] + self.grid[i, (j+1)%self.grid.shape[0]] +
                         self.grid[(i-1)%self.grid.shape[1], j] + self.grid[(i+1)%self.grid.shape[1], j] +
                         self.grid[(i-1)%self.grid.shape[1], (j-1)%self.grid.shape[0]] + self.grid[(i-1)%self.grid.shape[1], (j+1)%self.grid.shape[0]] +
                         self.grid[(i+1)%self.grid.shape[1], (j-1)%self.grid.shape[0]] + self.grid[(i+1)%self.grid.shape[1], (j+1)%self.grid.shape[0]])
                if self.grid[i, j]  == 1:
                    if (total < 2) or (total > 3):
                        new_grid[i, j] = 0
                else:
                    if total == 3:
                        new_grid[i, j] = 1
        self.grid = new_grid

def draw(grid):
    # Draw the grid
    plt.imshow(grid.grid, cmap='binary')
    plt.draw()

def main():
    grid = Grid(size=300, n=45000)  # Create a 300x300 grid with 45000 random living cells
    plt.ion()
    draw(grid)  # Draw the initial grid
    input("Press Enter to start the simulation...")
    try:
        while True:
            grid.next_state()
            draw(grid)
            plt.pause(0.05)  # Update more quickly to see the evolution
            plt.clf()
    except KeyboardInterrupt:
        print("Interrupted!")
        plt.close('all')

if __name__ == '__main__':
    main()
