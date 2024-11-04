# from entities.init_rover import init_rover
# from utils.move_forWard import move_forward
# from utils.move_bAckWard import move_backward
# from entities.display_grid import display_grid
from entities.Rover import Rover
from entities.Planet import Planet
from utils.Orientation import Orientation
from utils.Orientation import North
from utils.init import init_rover
from utils.Orientation import South
from utils.Orientation import East
from utils.Orientation import West

# if __name__ == "__main__":
#     position, orientation, grid = init_rover(0, 0, 'E', grid_size=10)
#     print("position initiale : 0,0,E")

#     #grille planet
#     display_grid(position)

#     # avance
#     position = move_forward(position, orientation)
#     position = move_forward(position, orientation)
#     position = move_forward(position, orientation)
#     position = move_forward(position, orientation)
#     position = move_forward(position, orientation)
#     print(f"position après avoir avancer : {position}")  
#     display_grid(position)

#     # reculer 
#     position = move_backward(position, orientation)
#     print(f"position après avoir reculer : {position}")  
#     display_grid(position)

# Exemple d'initialisation du Rover avec une orientation
position = {'x': 5, 'y': 5}
orientation = North()

# Déplacement en avant et en arrière
orientation.move_forward(position)  # Avancer vers le Nord
print(position)  # {'x': 5, 'y': 6}

orientation.move_backward(position)  # Reculer vers le Nord
print(position)  # {'x': 5, 'y': 5}

rover, planet = init_rover(5, 5, 'N', grid_size=30)

# Obtenir la position du rover
print(rover.get_position())  # {'x': 5, 'y': 5}

# Obtenir l'orientation du rover
print(rover.get_orientation())  # Instance de North()

# Obtenir la grille de la planète
print(planet.get_grid_size())  # 30

