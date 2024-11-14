import math


def area(r):
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return math.pi * r * r


def perimeter(r):
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return 2 * math.pi * r
