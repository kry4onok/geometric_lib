import unittest
from circle import area, perimeter
import math

class TestCircle(unittest.TestCase):
    def test_area_positive_radius(self):
        r = 2.4
        expected_area = math.pi * r * r
        self.assertAlmostEqual(area(r), expected_area)

    def test_area_zero_radius(self):
        r = 0
        expected_area = 0
        self.assertEqual(area(r), expected_area)

    def test_area_negative_radius(self):
        r = -3
        with self.assertRaises(ValueError):
            area(r)

    def test_area_positive_radius(self):
        r = 25
        expected_area =  math.pi * r * r
        self.assertAlmostEqual(area(r), expected_area)

    def test_perimeter_positive_radius(self):
        r = 3.3
        expected_perimeter = 2 * math.pi * r
        self.assertAlmostEqual(perimeter(r), expected_perimeter)

    def test_perimeter_zero_radius(self):
        r = 0
        expected_perimeter = 0
        self.assertEqual(perimeter(r), expected_perimeter)

    def test_perimeter_negative_radius(self):
        r = -3
        with self.assertRaises(ValueError):
            perimeter(r)

    def test_perimetr_positive_radius(self):
        r = 25
        expected_perimetr = 2 * math.pi * r
        self.assertAlmostEqual(perimeter(r), expected_perimetr)


if __name__ == '__main__':
    unittest.main()