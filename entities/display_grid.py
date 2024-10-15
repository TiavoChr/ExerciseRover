def display_grid(position, grid_size=10):

    for y in range(grid_size):
        row = ""
        for x in range(grid_size):
            if x == position['x'] and y == position['y']:
                row += "R "  #  Rover 
            else:
                row += ". "  
        print(row)
    print("\n")
