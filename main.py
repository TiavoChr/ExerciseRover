from typing import Dict
from entities.Rover import Rover
from entities.Planet import Planet
from utils.Orientation import Orientation
from utils.Orientation import North
from utils.init import init_rover

# Gestion des erreurs lors de la définition de la position initiale
try:
    position: Dict[str, int] = {'x': 5, 'y': 5}
    if not isinstance(position, dict) or 'x' not in position or 'y' not in position:
        raise ValueError("La position doit être un dictionnaire avec des clés 'x' et 'y'.")
except ValueError as e:
    print(f"Erreur lors de l'initialisation de la position : {e}")
    position = {'x': 0, 'y': 0}  # Position par défaut en cas d'erreur

# Gestion des erreurs lors de l'initialisation de l'orientation
try:
    orientation: Orientation = North()
    if not isinstance(orientation, Orientation):
        raise TypeError("L'orientation doit être une instance de la classe Orientation.")
except TypeError as e:
    print(f"Erreur lors de l'initialisation de l'orientation : {e}")
    orientation = North()  # Orientation par défaut

# Déplacement vers l'avant et l'arrière
try:
    orientation.move_forward(position)
    print(f"Position après un déplacement vers l'avant : {position}")
except Exception as e:
    print(f"Erreur lors du déplacement vers l'avant : {e}")

try:
    orientation.move_backward(position)
    print(f"Position après un déplacement vers l'arrière : {position}")
except Exception as e:
    print(f"Erreur lors du déplacement vers l'arrière : {e}")

# Initialisation du Rover et de la Planète avec gestion d'erreurs
try:
    rover: Rover
    planet: Planet
    rover, planet = init_rover(5, 5, 'N', grid_size=30)
except ValueError as e:
    print(f"Erreur lors de l'initialisation du Rover ou de la Planète : {e}")
    rover = None
    planet = None

# Vérifications avant d'accéder aux propriétés du Rover et de la Planète
if rover:
    try:
        print(f"Position du Rover : {rover.get_position()}")
        print(f"Orientation du Rover : {rover.get_orientation()}")
    except Exception as e:
        print(f"Erreur lors de la récupération des informations du Rover : {e}")

if planet:
    try:
        print(f"Grille de la Planète (taille) : {planet.get_grid_size()}")
    except Exception as e:
        print(f"Erreur lors de la récupération de la taille de la grille de la Planète : {e}")
