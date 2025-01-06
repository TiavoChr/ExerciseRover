def display_grid(position: dict, grid_size: int, obstacles: set):
    """
    Affiche une représentation visuelle de la grille avec la position du Rover et les obstacles.

    Args:
        position (dict): Position actuelle du Rover {'x': int, 'y': int}.
        grid_size (int): Taille de la grille (grille carrée).
        obstacles (set): Ensemble des positions des obstacles {(x1, y1), (x2, y2), ...}.

    Returns:
        None
    """
    for y in range(grid_size):
        row = ""
        for x in range(grid_size):
            if (x, y) in obstacles:
                row += "X "  # Représentation des obstacles
            elif x == position['x'] and y == position['y']:
                row += "R "  # Représentation du Rover
            else:
                row += ". "  # Cases vides
        print(row)
    print("\n")
