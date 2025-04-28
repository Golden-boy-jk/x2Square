import math

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
        return abs(self.a**2 + self.b**2 - self.c**2) < 0.00001
