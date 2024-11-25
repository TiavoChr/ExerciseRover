class Planet:
    """
    Classe représentant la planète. Gère la grille toroïdale et les obstacles.
    """

    def __init__(self, grid_size: int):
        """
        Initialise la planète avec une grille de taille donnée.

        Args:
            grid_size (int): Taille de la grille (grille carrée de grid_size x grid_size).
        """
        self.grid_size = grid_size
        self.obstacles = set()  # Ensemble des coordonnées des obstacles

    def add_obstacle(self, x: int, y: int):
        """
        Ajoute un obstacle sur la grille.

        Args:
            x (int): Coordonnée x de l'obstacle.
            y (int): Coordonnée y de l'obstacle.
        """
        self.obstacles.add((x, y))

    def is_obstacle(self, x: int, y: int) -> bool:
        """
        Vérifie si une case contient un obstacle.

        Args:
            x (int): Coordonnée x.
            y (int): Coordonnée y.

        Returns:
            bool: True si un obstacle est présent, False sinon.
        """
        return (x, y) in self.obstacles

    def calculate_new_position(self, x: int, y: int, orientation: str, reverse=False):
        """
        Calcule la nouvelle position en fonction de l'orientation et vérifie les obstacles.

        Args:
            x (int): Coordonnée x actuelle.
            y (int): Coordonnée y actuelle.
            orientation (str): Orientation actuelle ('N', 'S', 'E', 'W').
            reverse (bool): Si True, calcule un mouvement en arrière.

        Returns:
            tuple: Nouvelles coordonnées (x, y) ou la position actuelle si un obstacle est rencontré.
        """
        if orientation == 'N':
            new_y = (y - 1 if reverse else y + 1) % self.grid_size
            new_x = x
        elif orientation == 'S':
            new_y = (y + 1 if reverse else y - 1) % self.grid_size
            new_x = x
        elif orientation == 'E':
            new_x = (x - 1 if reverse else x + 1) % self.grid_size
            new_y = y
        elif orientation == 'W':
            new_x = (x + 1 if reverse else x - 1) % self.grid_size
            new_y = y
        else:
            raise ValueError(f"Orientation inconnue : {orientation}")

        if self.is_obstacle(new_x, new_y):
            print(f"Obstacle détecté à la position ({new_x}, {new_y}). Mouvement bloqué.")
            return x, y  # Retourne la position actuelle si un obstacle est détecté

        return new_x, new_y
