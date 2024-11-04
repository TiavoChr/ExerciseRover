from utils.Orientation import Orientation

class Rover:
    def __init__(self, position, orientation: Orientation):
        self.position = position 
        self.orientation = orientation 

    def set_orientation(self, orientation: Orientation):
        self.orientation = orientation

    def get_orientation(self):
        return self.orientation

    def get_position(self):
        return self.position

    def set_position(self, x, y):
        self.position['x'] = x
        self.position['y'] = y
