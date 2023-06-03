import matplotlib.pyplot as plt
import numpy as np

class Grid:
    def __init__(self, size):
        # Initialize the grid with all cells dead
        self.grid = np.zeros((size, size))

    def next_state(self):
        # Placeholder for the method that will calculate the next state
        pass

def draw(grid):
    # Draw the grid
    plt.imshow(grid.grid, cmap='binary')
    plt.show()

def main():
    grid = Grid(size=10)

    while True:
        draw(grid)
        grid.next_state()

if __name__ == '__main__':
    main()
