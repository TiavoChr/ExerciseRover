import pytest
from entities.Rover import Rover
from utils.Orientation import North, South, East, West

@pytest.fixture
def initial_position():
    return {'x': 5, 'y': 5}

def test_rover_initialization(initial_position):
    rover = Rover(initial_position, North())
    assert rover.get_position() == {'x': 5, 'y': 5}
    assert isinstance(rover.get_orientation(), North)

def test_rover_move_forward(initial_position):
    rover = Rover(initial_position, North())
    rover.orientation.move_forward(rover.get_position())
    assert rover.get_position() == {'x': 5, 'y': 6}

def test_rover_move_backward(initial_position):
    rover = Rover(initial_position, North())
    rover.orientation.move_backward(rover.get_position())
    assert rover.get_position() == {'x': 5, 'y': 4}

def test_rover_change_orientation(initial_position):
    rover = Rover(initial_position, North())
    rover.set_orientation(East())
    assert isinstance(rover.get_orientation(), East)
    rover.orientation.move_forward(rover.get_position())
    assert rover.get_position() == {'x': 6, 'y': 5}
