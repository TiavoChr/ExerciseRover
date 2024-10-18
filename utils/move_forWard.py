from abc import ABC, abstractmethod

class Orientation(ABC):
    @abstractmethod
    def move(self, position):
        pass

class North(Orientation):
    def move(self, position):
        position['y'] += 1
        return position

class South(Orientation):
    def move(self, position):
        position['y'] -= 1
        return position

class East(Orientation):
    def move(self, position):
        position['x'] += 1
        return position

class West(Orientation):
    def move(self, position):
        position['x'] -= 1
        return position

def move_forward(position, orientation: Orientation):
    return orientation.move(position)
