import unittest

import sys
sys.path.append("../")

import rectangle

class RectangleTestCase(unittest.TestCase):
    def test_default_area(self):
        res = rectangle.area(2, 3)
        self.assertEqual(res, 6)
    def test_zero_area(self):
        res = rectangle.area(0, 3)
        self.assertEqual(res, 0)
    def test_square_area(self):
        res = rectangle.area(3, 3)
        self.assertEqual(res, 9)
    def test_big_area(self):
        res = rectangle.area(2_000_000, 1_000_000)
        self.assertEqual(res, 2_000_000_000_000)
    def test_string_area(self):
        self.assertRaises(TypeError, rectangle.area, "a", 6)
    def test_negative_area(self):
        self.assertRaises(ValueError, rectangle.area, -1, 5)
    def test_default_perimeter(self):
        res = rectangle.perimeter(2, 3)
        self.assertEqual(res, 10)
    def test_zero_perimeter(self):
        res = rectangle.perimeter(0, 0)
        self.assertEqual(res, 0)
    def test_square_perimeter(self):
        res = rectangle.perimeter(3, 3)
        self.assertEqual(res, 12)
    def test_big_perimeter(self):
        res = rectangle.perimeter(2_000_000, 1_000_000)
        self.assertEqual(res, 6_000_000)
    def test_string_perimeter(self):
        self.assertRaises(TypeError, rectangle.perimeter, "a", 6)
    def test_negative_perimeter(self):
        self.assertRaises(ValueError, rectangle.perimeter, -5, 1)



