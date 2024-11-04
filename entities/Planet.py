class Planet:
    def __init__(self, grid_size=30):
        self.grid_size = grid_size
        self.grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

    def get_grid(self):
        return self.grid

    def get_grid_size(self):
        return self.grid_size
