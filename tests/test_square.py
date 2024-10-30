import unittest

import sys
sys.path.append("../")

import square

class SquareTestCase(unittest.TestCase):
    def test_default_area(self):
        res = square.area(3)
        self.assertEqual(res, 9)
    def test_zero_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)
    def test_big_area(self):
        res = square.area(1_000_000)
        self.assertEqual(res, 1_000_000_000_000)
    def test_string_area(self):
        self.assertRaises(TypeError, square.area, "a")
    def test_negative_area(self):
        self.assertRaises(ValueError, square.area, -1)
    def test_default_perimeter(self):
        res = square.perimeter(3)
        self.assertEqual(res, 12)
    def test_zero_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)
        res = square.perimeter(3)
        self.assertEqual(res, 12)
    def test_big_perimeter(self):
        res = square.perimeter(1_000_000)
        self.assertEqual(res, 4_000_000)
    def test_string_perimeter(self):
        self.assertRaises(TypeError, square.perimeter, "a")
    def test_negative_perimeter(self):
        self.assertRaises(ValueError, square.perimeter, -1)
