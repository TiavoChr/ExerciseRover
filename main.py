from entities.init_rover import init_rover
from utils.move_forWard import move_forward
from utils.move_bAckWard import move_backward
from entities.display_grid import display_grid


if __name__ == "__main__":
    position, orientation, grid = init_rover(0, 0, 'E', grid_size=10)
    print("position initiale : 0,0,E")

    #grille planet
    display_grid(position)

    # avance
    position = move_forward(position, orientation)
    position = move_forward(position, orientation)
    position = move_forward(position, orientation)
    position = move_forward(position, orientation)
    position = move_forward(position, orientation)
    print(f"position après avoir avancer : {position}")  
    display_grid(position)

    # reculer 
    position = move_backward(position, orientation)
    print(f"position après avoir reculer : {position}")  
    display_grid(position)
