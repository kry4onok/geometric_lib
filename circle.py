import math


def area(radius):
    """Вычисляет площадь круга по заданному радиусу.

    Args:
        radius (float): Радиус круга.

    Returns:
        float: Площадь круга.

    Example:
        >>> area(10)
        314.1592653589793
    """
    return math.pi * radius * radius


def perimeter(radius):
    """Вычисляет периметр (длину окружности) по заданному радиусу.

    Args:
        radius (float): Радиус круга.

    Returns:
        float: Периметр круга.

    Example:
        >>> perimeter(10)
        62.83185307179586
    """
    return 2 * math.pi * radius
