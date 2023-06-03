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
    grid = Grid(size=300, n=3500)  # Create a 100x100 grid with 500 random living cells
    plt.ion()
    try:
        while True:
            draw(grid)
            grid.next_state()
            plt.pause(0.05)  # Update more quickly to see the evolution
            plt.clf()
    except KeyboardInterrupt:
        print("Interrupted!")
        plt.close('all')


if __name__ == '__main__':
    main()
