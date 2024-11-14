import unittest
from square import area, perimeter


class TestSquare(unittest.TestCase):
    def test_area_positive_side(self):
        side = 4.3
        expected_area = side**2
        self.assertEqual(area(side), expected_area)

    def test_area_zero_side(self):
        side = 0
        expected_area = 0
        self.assertEqual(area(side), expected_area)

    def test_area_negative_side(self):
        side = -5
        with self.assertRaises(ValueError):
            area(side)

    def test_perimeter_positive_side(self):
        side = 5.7
        expected_perimeter = 4 * side
        self.assertEqual(perimeter(side), expected_perimeter)

    def test_perimeter_zero_side(self):
        side = 0
        expected_perimeter = 0
        self.assertEqual(perimeter(side), expected_perimeter)

    def test_perimeter_negative_side(self):
        side = -2
        with self.assertRaises(ValueError):
            perimeter(side)


if __name__ == "__main__":
    unittest.main()
