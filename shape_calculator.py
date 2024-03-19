NAME = "krug"
import math

class ShapeCalculator:
    
    @staticmethod
    def circle_area(radius):
        return math.pi * radius ** 2

    @staticmethod
    def triangle_area(side1, side2, side3):
        s = (side1 + side2 + side3) / 2
        return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

# Пример использования:
# radius = 5
# print("Площадь круга с радиусом", radius, ":", ShapeCalculator.circle_area(radius))

# side1 = 3
# side2 = 4
# side3 = 5
# print("Площадь треугольника с сторонами", side1, ",", side2, ",", side3, ":", ShapeCalculator.triangle_area(side1, side2, side3))