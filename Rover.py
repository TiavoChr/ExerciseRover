from dataclasses import dataclass
from Orientation import Orientation

@dataclass
class Rover:
    # modifier la position
    position: Position
    orientation: Orientation
    grid_size: int 

    # def moveForward

    # def moveBackward

    def rotate_left(self):
        orientation_order = [
            Orientation.NORTH,
            Orientation.WEST,
            Orientation.SOUTH,
            Orientation.EAST
        ]
        current_index = orientation_order.index(self.orientation)
        self.orientation = orientation_order[(current_index + 1) % 4]

    def rotate_right(self):
        orientation_order = [
            Orientation.NORTH,
            Orientation.EAST,
            Orientation.SOUTH,
            Orientation.WEST
        ]
        current_index = orientation_order.index(self.orientation)
        self.orientation = orientation_order[(current_index + 1) % 4]