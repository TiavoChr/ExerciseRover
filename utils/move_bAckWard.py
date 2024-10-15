def move_backward(position, orientation):
    if orientation == 'N':
        position['y'] -= 1
    elif orientation == 'S':
        position['y'] += 1
    elif orientation == 'E':
        position['x'] -= 1
    elif orientation == 'W':
        position['x'] += 1
    
    return position
