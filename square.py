import math
import unittest

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Радиус должен быть больше нуля")
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        # Сортируем стороны для удобства
        sides = sorted([self.a, self.b, self.c])

        if sides[0] <= 0 or sides[1] <= 0 or sides[2] <= 0:
            raise ValueError("Стороны должны быть положительными")

        if sides[0] + sides[1] <= sides[2]:
            raise ValueError("Невозможно построить треугольник с такими сторонами")

        # Переприсваиваем уже отсортированные значения
        self.a, self.b, self.c = sides

    def area(self):
        p = (self.a + self.b + self.c) / 2
        s = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return s

    def is_right_angled(self):
        return abs(self.a ** 2 + self.b ** 2 - self.c ** 2) < 0.00001


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
