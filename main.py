from typing import Dict
from entities.Rover import Rover
from entities.Planet import Planet
from utils.Orientation import Orientation
from utils.Orientation import North
from utils.init import init_rover

position: Dict[str, int] = {'x': 5, 'y': 5}
orientation: Orientation = North()


#  avance et arrière
orientation.move_forward(position)
print(position)  

orientation.move_backward(position)  
print(position) 

rover: Rover
planet: Planet
rover, planet = init_rover(5, 5, 'N', grid_size=30)


#poisition du rover
print(rover.get_position())

# orientation du rvoer
print(rover.get_orientation()) 

# grid de la planete
print(planet.get_grid_size())  # 30

