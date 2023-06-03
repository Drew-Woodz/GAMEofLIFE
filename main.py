#Conway's Game of Life
# The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells,
# each of which is in one of two possible states, alive or dead, or "populated" or "unpopulated".
# Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically,
# or diagonally adjacent. At each step in time, the following transitions occur:
#
# Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
#
# Any live cell with two or three live neighbours lives on to the next generation.
# 
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# 
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
#
# The initial pattern constitutes the seed of the system. The first generation is created by applying
# the above rules simultaneously to every cell in the seed—births and deaths occur simultaneously, and
# the discrete moment at which this happens is sometimes called a tick (in other words, each generation
# is a pure function of the preceding one). The rules continue to be applied repeatedly to create further
# generations.
# Author: Andrew Lockwood
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
