import math


def area(a, b, c):
    # Проверка на неотрицательные значения
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Стороны треугольника не могут быть отрицательными")
    # Проверка на неравенство треугольника
    if not (a + b > c and a + c > b and b + c > a):
        raise ValueError("Стороны не образуют треугольник")

    # Формула Герона
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def perimeter(a, b, c):
    # Проверка на неотрицательные значения
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Стороны треугольника не могут быть отрицательными")
    # Проверка на неравенство треугольника
    if not (a + b > c and a + c > b and b + c > a):
        raise ValueError("Стороны не образуют треугольник")

    return a + b + c
