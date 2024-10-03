def area(side_a, side_b, side_c):
    """Вычисляет полупериметр треугольника по длине его сторон.

    Args:
        side_a (float): Длина первой стороны треугольника.
        side_b (float): Длина второй стороны треугольника.
        side_c (float): Длина третьей стороны треугольника.

    Returns:
        float: Полупериметр треугольника.

    Example:
        >>> area(3, 4, 5)
        6.0
    """
    return (side_a + side_b + side_c) / 2


def perimeter(side_a, side_b, side_c):
    """Вычисляет периметр треугольника по длине его сторон.

    Args:
        side_a (float): Длина первой стороны треугольника.
        side_b (float): Длина второй стороны треугольника.
        side_c (float): Длина третьей стороны треугольника.

    Returns:
        float: Периметр треугольника.

    Example:
        >>> perimeter(3, 4, 5)
        12
    """
    return side_a + side_b + side_c
