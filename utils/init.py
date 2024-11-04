from entities.Rover import Rover
from entities.Planet import Planet
from utils.Orientation import Orientation
from utils.Orientation import North
from utils.Orientation import South
from utils.Orientation import East
from utils.Orientation import West

def init_rover(x_start, y_start, initial_orientation, grid_size=30):
    # Initialisation de la planète
    planet = Planet(grid_size)

    # Initialisation du Rover avec une position et une orientation
    position = {'x': x_start, 'y': y_start}

    # Mapping des orientations avec les classes correspondantes
    orientations = {
        'N': North(),
        'S': South(),
        'E': East(),
        'W': West()
    }
    
    if initial_orientation in orientations:
        orientation = orientations[initial_orientation]
    else:
        raise ValueError("Orientation non valide")
    
    rover = Rover(position, orientation)

    return rover, planet
