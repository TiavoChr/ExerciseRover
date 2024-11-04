from abc import ABC, abstractmethod

class Orientation(ABC):
    @abstractmethod
    def move_forward(self, position):
        pass

    @abstractmethod
    def move_backward(self, position):
        pass

class North(Orientation):
    def move_forward(self, position):
        position['y'] += 1
        return position
    
    def move_backward(self, position):
        position['y'] -= 1
        return position

class South(Orientation):
    def move_forward(self, position):
        position['y'] -= 1
        return position
    
    def move_backward(self, position):
        position['y'] += 1
        return position

class East(Orientation):
    def move_forward(self, position):
        position['x'] += 1
        return position
    
    def move_backward(self, position):
        position['x'] -= 1
        return position

class West(Orientation):
    def move_forward(self, position):
        position['x'] -= 1
        return position
    
    def move_backward(self, position):
        position['x'] += 1
        return position

def move_forward(position, orientation: Orientation):
    return orientation.move_forward(position)

def move_backward(position, orientation: Orientation):
    return orientation.move_backward(position)
