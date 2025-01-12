import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from rover_core.rover import Rover
from rover_core.planet import Planet

@pytest.fixture
def planet():
    planet = Planet(grid_size=10)
    planet.add_obstacle(3, 3)
    return planet

@pytest.fixture
def rover():
    return Rover(position={'x': 2, 'y': 3}, orientation='N')

def test_rover_initial_position(rover):
    assert rover.get_position() == {'x': 2, 'y': 3}
    assert rover.get_orientation() == 'N'

def test_rover_move_forward_no_obstacle(rover, planet):
    rover.move_forward(planet)
    assert rover.get_position() == {'x': 2, 'y': 4}

def test_rover_obstacle(rover, planet):
    rover.position = {'x': 3, 'y': 2}  # Juste avant un obstacle
    rover.move_forward(planet)
    assert rover.get_position() == {'x': 3, 'y': 2}  # Le mouvement doit être bloqué
