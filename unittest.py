import unittest

class TestShapes(unittest.TestCase):

    def test_circle_area(self):
        circle = Circle(1)
        self.assertAlmostEqual(circle.area(), math.pi)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6)

    def test_triangle_right_angle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_angled())

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 3)

    def test_invalid_circle(self):
        with self.assertRaises(ValueError):
            Circle(-5)

if __name__ == '__main__':
    unittest.main()
