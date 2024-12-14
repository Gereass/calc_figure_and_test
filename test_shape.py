import unittest
from shape_calculator import *
import math

class TestShapeCalculator(unittest.TestCase):

    def test_circle_area(self):
        self.assertAlmostEqual(ShapeCalculator.circle_area(3), math.pi * 3 ** 2, places=5)
        self.assertAlmostEqual(ShapeCalculator.circle_area(0), 0, places=5)
    
    def test_triangle_area(self):
        self.assertAlmostEqual(ShapeCalculator.triangle_area(3, 4, 5), 6, places=5)
        self.assertAlmostEqual(ShapeCalculator.triangle_area(6, 8, 10), 24, places=5)
        self.assertAlmostEqual(ShapeCalculator.triangle_area(0, 0, 0), 0, places=5)
        self.assertAlmostEqual(ShapeCalculator.triangle_area(5, 5, 5), 10.8253, places=4)

if __name__ == '__main__':
    unittest.main()