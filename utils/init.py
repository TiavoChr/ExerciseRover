from entities.Rover import Rover
from entities.Planet import Planet
from utils.Orientation import North, South, East, West

def init_rover(x_start: int, y_start: int, initial_orientation: str, grid_size: int = 30):
    """
    Initialise le Rover et la Planète.
    
    Args:
        x_start (int): Position initiale x du Rover.
        y_start (int): Position initiale y du Rover.
        initial_orientation (str): Orientation initiale ('N', 'S', 'E', 'W').
        grid_size (int): Taille de la grille de la planète (par défaut 30).
    
    Returns:
        tuple: (Rover, Planet) initialisés.
    
    Raises:
        ValueError: Si l'orientation initiale n'est pas valide.
        TypeError: Si les types des paramètres ne sont pas corrects.
    """
    # Validation des types des arguments
    try:
        if not isinstance(x_start, int) or not isinstance(y_start, int):
            raise TypeError("Les positions x_start et y_start doivent être des entiers.")
        if not isinstance(initial_orientation, str):
            raise TypeError("L'orientation initiale doit être une chaîne de caractères.")
        if not isinstance(grid_size, int) or grid_size <= 0:
            raise ValueError("La taille de la grille doit être un entier positif.")
    except (TypeError, ValueError) as e:
        print(f"Erreur dans les paramètres d'initialisation : {e}")
        raise

    # Initialisation de la planète avec gestion des erreurs
    try:
        planet = Planet(grid_size)
    except Exception as e:
        print(f"Erreur lors de l'initialisation de la planète : {e}")
        raise

    # Initialisation de la position du Rover
    position = {'x': x_start, 'y': y_start}
    
    # Dictionnaire des orientations disponibles
    orientations = {
        'N': North(),
        'S': South(),
        'E': East(),
        'W': West()
    }

    # Validation et création de l'orientation
    try:
        orientation = orientations[initial_orientation]
    except KeyError:
        print(f"Orientation non valide : {initial_orientation}. Valeurs possibles : {list(orientations.keys())}")
        raise ValueError(f"Orientation non valide : {initial_orientation}")

    # Initialisation du Rover avec gestion des erreurs
    try:
        rover = Rover(position, orientation)
    except Exception as e:
        print(f"Erreur lors de l'initialisation du Rover : {e}")
        raise

    return rover, planet
