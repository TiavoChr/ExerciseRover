def rotate_orientation(current_orientation: str, direction: str) -> str:
    """
    Calcule la nouvelle orientation après une rotation.

    Args:
        current_orientation (str): Orientation actuelle ('N', 'S', 'E', 'W').
        direction (str): 'L' pour tourner à gauche, 'R' pour tourner à droite.

    Returns:
        str: Nouvelle orientation après rotation.
    """
    orientations = ['N', 'E', 'S', 'W']
    index = orientations.index(current_orientation)

    if direction == 'L':
        return orientations[(index - 1) % 4]
    elif direction == 'R':
        return orientations[(index + 1) % 4]
    else:
        raise ValueError("Direction invalide. Utilisez 'L' pour gauche ou 'R' pour droite.")
