import unittest
from calculate import calc


class TestCalcFunction(unittest.TestCase):
    def test_circle_area_valid(self):
        result = calc("circle", "area", [3])
        self.assertIn("Area of circle with size(s) [3]", result)

    def test_circle_perimeter_valid(self):
        result = calc("circle", "perimeter", [5])
        self.assertIn("Perimeter of circle with size(s) [5]", result)

    def test_square_area_valid(self):
        result = calc("square", "area", [4])
        self.assertIn("Area of square with size(s) [4]", result)

    def test_square_perimeter_valid(self):
        result = calc("square", "perimeter", [6])
        self.assertIn("Perimeter of square with size(s) [6]", result)

    def test_triangle_area_valid(self):
        result = calc("triangle", "area", [3, 4, 5])
        self.assertIn("Area of triangle with size(s) [3, 4, 5]", result)

    def test_triangle_perimeter_valid(self):
        result = calc("triangle", "perimeter", [5, 12, 13])
        self.assertIn("Perimeter of triangle with size(s) [5, 12, 13]", result)

    def test_invalid_figure(self):
        with self.assertRaises(ValueError) as e:
            calc("hexagon", "area", [6])
        self.assertIn("Фигура hexagon недоступна", str(e.exception))

    def test_invalid_function(self):
        with self.assertRaises(ValueError) as e:
            calc("circle", "volume", [5])
        self.assertIn("Функция volume недоступна", str(e.exception))

    def test_incorrect_number_of_params(self):
        with self.assertRaises(ValueError) as e:
            calc("triangle", "area", [3, 4])
        self.assertIn("Ожидается 3 параметров для фигуры triangle", str(e.exception))

    def test_negative_size_value(self):
        with self.assertRaises(ValueError) as e:
            calc("square", "area", [-4])
        self.assertIn("Все размеры должны быть положительными", str(e.exception))

    def test_zero_size_value(self):
        with self.assertRaises(ValueError) as e:
            calc("circle", "perimeter", [0])
        self.assertIn("Все размеры должны быть положительными", str(e.exception))


if __name__ == "__main__":
    unittest.main()
