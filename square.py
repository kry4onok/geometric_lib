def area(side_length):
    """Вычисляет площадь квадрата по длине его стороны.

    Args:
        side_length (float): Длина стороны квадрата.

    Returns:
        float: Площадь квадрата.

    Example:
        >>> area(4)
        16
    """
    return side_length * side_length


def perimeter(side_length):
    """Вычисляет периметр квадрата по длине его стороны.

    Args:
        side_length (float): Длина стороны квадрата.

    Returns:
        float: Периметр квадрата.

    Example:
        >>> perimeter(4)
        16
    """
    return 4 * side_length
