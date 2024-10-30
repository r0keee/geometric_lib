import unittest

import sys
sys.path.append("../")

import triangle

class TriangleTestCase(unittest.TestCase):
    def test_default_area(self):
        res = triangle.area(3, 2)
        self.assertEqual(res, 3)
    def test_zero_area(self):
        res = triangle.area(0, 2)
        self.assertEqual(res, 0)
    def test_big_area(self):
        res = triangle.area(3_000_000, 5_000_000)
        self.assertEqual(res, 7_500_000_000_000)
    def test_string_area(self):
        self.assertRaises(TypeError, triangle.area, "a", 2)
    def test_negative_area(self):
        self.assertRaises(ValueError, triangle.area, -3, 4)
    def test_default_perimeter(self):
        res = triangle.perimeter(1, 2, 3)
        self.assertEqual(res, 6)
    def test_zero_perimeter(self):
        res = triangle.perimeter(0, 2, 3)
        self.assertEqual(res, 5)
    def test_big_perimeter(self):
        res = triangle.perimeter(1_000_000, 2_000_000, 3_000_000)
        self.assertEqual(res, 6_000_000)
    def test_string_perimeter(self):
        self.assertRaises(TypeError, triangle.perimeter, "a", 2, 3)
    def test_negative_perimeter(self):
        self.assertRaises(ValueError, triangle.perimeter, -6, 2, 3)


