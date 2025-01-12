import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from rover_core.rover import Rover
from rover_core.planet import Planet
from rover_core.movement import rotate_orientation

def test_rotate_left():
    assert rotate_orientation('N', 'L') == 'W'
    assert rotate_orientation('W', 'L') == 'S'
    assert rotate_orientation('S', 'L') == 'E'
    assert rotate_orientation('E', 'L') == 'N'

def test_rotate_right():
    assert rotate_orientation('N', 'R') == 'E'
    assert rotate_orientation('E', 'R') == 'S'
    assert rotate_orientation('S', 'R') == 'W'
    assert rotate_orientation('W', 'R') == 'N'

def test_invalid_direction():
    try:
        rotate_orientation('N', 'X')
    except ValueError as e:
        assert str(e) == "Direction invalide. Utilisez 'L' pour gauche ou 'R' pour droite."
