import unittest
from math import pi

import sys
sys.path.append("../")

import circle

class CircleTestCase(unittest.TestCase):
    def test_default_area(self):
        res = circle.area(3)
        self.assertEqual(res, pi * 9)
    def test_zero_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)
    def test_big_area(self):
        res = circle.area(1_000_000)
        self.assertEqual(res, 1_000_000_000_000 * pi)
    def test_string_area(self):
        self.assertRaises(TypeError, circle.area, "a")
    def test_negative_area(self):
        self.assertRaises(ValueError, circle.area, -1)
    def test_default_perimeter(self):
        res = circle.perimeter(3)
        self.assertEqual(res, 6 * pi)
    def test_zero_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)
    def test_big_perimeter(self):
        res = circle.perimeter(1_000_000)
        self.assertEqual(res, 2_000_000 * pi)
    def test_string_perimeter(self):
        self.assertRaises(TypeError, circle.perimeter, "a")
    def test_negative_perimeter(self):
        self.assertRaises(ValueError, circle.perimeter, -1)




