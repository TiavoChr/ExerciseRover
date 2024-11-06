import pytest
from utils.Orientation import North, South, East, West

@pytest.fixture
def position():
    return {'x': 0, 'y': 0}

def test_north_move_forward(position):
    north = North()
    updated_position = north.move_forward(position)
    assert updated_position['y'] == 1
    assert updated_position['x'] == 0

def test_north_move_backward(position):
    north = North()
    updated_position = north.move_backward(position)
    assert updated_position['y'] == -1
    assert updated_position['x'] == 0

def test_south_move_forward(position):
    south = South()
    updated_position = south.move_forward(position)
    assert updated_position['y'] == -1
    assert updated_position['x'] == 0

def test_south_move_backward(position):
    south = South()
    updated_position = south.move_backward(position)
    assert updated_position['y'] == 1
    assert updated_position['x'] == 0

def test_east_move_forward(position):
    east = East()
    updated_position = east.move_forward(position)
    assert updated_position['x'] == 1
    assert updated_position['y'] == 0

def test_east_move_backward(position):
    east = East()
    updated_position = east.move_backward(position)
    assert updated_position['x'] == -1
    assert updated_position['y'] == 0

def test_west_move_forward(position):
    west = West()
    updated_position = west.move_forward(position)
    assert updated_position['x'] == -1
    assert updated_position['y'] == 0

def test_west_move_backward(position):
    west = West()
    updated_position = west.move_backward(position)
    assert updated_position['x'] == 1
    assert updated_position['y'] == 0