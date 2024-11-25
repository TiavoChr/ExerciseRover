import pytest
from rover_core.planet import Planet

@pytest.fixture
def planet():
    planet = Planet(grid_size=10)
    planet.add_obstacle(3, 3)
    return planet

def test_add_obstacle(planet):
    assert planet.is_obstacle(3, 3) is True
    assert planet.is_obstacle(5, 5) is False

def test_toroidal_movement(planet):
    x, y = planet.calculate_new_position(0, 0, 'N')
    assert (x, y) == (0, 1)  # Bordure toroïdale
    x, y = planet.calculate_new_position(0, 0, 'S')
    assert (x, y) == (0, 9)  # Retour au bas de la grille
    x, y = planet.calculate_new_position(9, 9, 'E')
    assert (x, y) == (0, 9)  # Retour au début de la grille

def test_obstacle_detection(planet):
    # Position initiale sans obstacle
    x, y = planet.calculate_new_position(3, 2, 'N')
    assert (x, y) == (3, 2)  # Le mouvement est bloqué par un obstacle

    # Test sans obstacle (mouvement libre)
    planet.obstacles.remove((3, 3))  # Supprime l'obstacle
    x, y = planet.calculate_new_position(3, 2, 'N')
    assert (x, y) == (3, 3)  # La position devrait changer

