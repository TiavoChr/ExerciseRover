def init_rover(x_start, y_start, initial_orientation, grid_size=30):

    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    
    position = {'x': x_start, 'y': y_start}
    orientation = initial_orientation  # Nord SUD ESt Wesst
    
    return position, orientation, grid
