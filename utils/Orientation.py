from abc import ABC, abstractmethod
from typing import Dict

class Orientation(ABC):
    @abstractmethod
    def move_forward(self, position: Dict[str, int]):
        pass

    @abstractmethod
    def move_backward(self, position: Dict[str, int]):
        pass

class North(Orientation):
    def move_forward(self, position: Dict[str, int]):
        position['y'] += 1
        return position
    
    def move_backward(self, position: Dict[str, int]):
        position['y'] -= 1
        return position

class South(Orientation):
    def move_forward(self, position: Dict[str, int]):
        position['y'] -= 1
        return position
    
    def move_backward(self, position: Dict[str, int]):
        position['y'] += 1
        return position

class East(Orientation):
    def move_forward(self, position: Dict[str, int]):
        position['x'] += 1
        return position
    
    def move_backward(self, position: Dict[str, int]):
        position['x'] -= 1
        return position

class West(Orientation):
    def move_forward(self, position: Dict[str, int]):
        position['x'] -= 1
        return position
    
    def move_backward(self, position: Dict[str, int]):
        position['x'] += 1
        return position

def move_forward(position: Dict[str, int], orientation: Orientation):
    return orientation.move_forward(position)

def move_backward(position: Dict[str, int], orientation: Orientation):
    return orientation.move_backward(position)
