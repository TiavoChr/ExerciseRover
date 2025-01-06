class Rover:
    """
    Classe représentant le Rover. Gère sa position, son orientation et ses déplacements.
    """

    def __init__(self, position: dict, orientation: str):
        """
        Initialise le Rover.

        Args:
            position (dict): Position initiale du Rover sous la forme {'x': int, 'y': int}.
            orientation (str): Orientation initiale ('N', 'S', 'E', 'W').
        """
        self.position = position
        self.orientation = orientation

    def move_forward(self, planet):
        """
        Déplace le Rover vers l'avant en fonction de son orientation.

        Args:
            planet (Planet): Instance de la classe Planet pour gérer les limites et obstacles.

        Returns:
            None
        """
        self.position['x'], self.position['y'] = planet.calculate_new_position(
            self.position['x'], self.position['y'], self.orientation
        )

    def move_backward(self, planet):
        """
        Déplace le Rover vers l'arrière en fonction de son orientation.

        Args:
            planet (Planet): Instance de la classe Planet pour gérer les limites et obstacles.

        Returns:
            None
        """
        self.position['x'], self.position['y'] = planet.calculate_new_position(
            self.position['x'], self.position['y'], self.orientation, reverse=True
        )

    def rotate_left(self):
        """
        Oriente le Rover à gauche (90° anti-horaire).

        Returns:
            None
        """
        orientations = ['N', 'W', 'S', 'E']
        self.orientation = orientations[(orientations.index(self.orientation) + 1) % 4]

    def rotate_right(self):
        """
        Oriente le Rover à droite (90° horaire).

        Returns:
            None
        """
        orientations = ['N', 'E', 'S', 'W']
        self.orientation = orientations[(orientations.index(self.orientation) - 1) % 4]

    def get_position(self):
        """
        Retourne la position actuelle du Rover.

        Returns:
            dict: Position sous la forme {'x': int, 'y': int}.
        """
        return self.position

    def get_orientation(self):
        """
        Retourne l'orientation actuelle du Rover.

        Returns:
            str: Orientation actuelle ('N', 'S', 'E', 'W').
        """
        return self.orientation
