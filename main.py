from entities.Rover import Rover
from entities.Planet import Planet
from utils.Orientation import Orientation
from utils.Orientation import North
from utils.init import init_rover
from utils.Orientation import South
from utils.Orientation import East
from utils.Orientation import West

position = {'x': 5, 'y': 5}
orientation = North()

#  avance et arrière
orientation.move_forward(position)
print(position)  

orientation.move_backward(position)  
print(position) 

rover, planet = init_rover(5, 5, 'N', grid_size=30)

#poisition du rover
print(rover.get_position())  # {'x': 5, 'y': 5}

# orientation du rvoer
print(rover.get_orientation())  # Instance de North()

# grid de la planete
print(planet.get_grid_size())  # 30

