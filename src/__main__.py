from rover_core.rover import Rover
from rover_core.planet import Planet
from utils.grid_display import display_grid

def main():
    # Initialisation de la planète et du Rover
    planet = Planet(grid_size=10)
    planet.add_obstacle(3, 3)
    planet.add_obstacle(7, 7)

    rover = Rover(position={'x': 0, 'y': 0}, orientation='N')

    # Simulation
    print("=== Début de la simulation du Rover ===")
    display_grid(rover.get_position(), planet.grid_size, planet.obstacles)

    # Déplacement vers l'avant
    rover.move_forward(planet)
    print(f"Après 'Avancer': Position: {rover.get_position()}, Orientation: {rover.get_orientation()}")
    display_grid(rover.get_position(), planet.grid_size, planet.obstacles)

    # Rotation à gauche
    rover.rotate_left()
    print(f"Après 'Tourner à gauche': Orientation: {rover.get_orientation()}")
    display_grid(rover.get_position(), planet.grid_size, planet.obstacles)

    # Déplacement vers l'avant
    rover.move_forward(planet)
    print(f"Après 'Avancer': Position: {rover.get_position()}, Orientation: {rover.get_orientation()}")
    display_grid(rover.get_position(), planet.grid_size, planet.obstacles)

if __name__ == "__main__":
    main()
