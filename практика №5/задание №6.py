#расстояние между двумя точками

import math

def distance(x1, y1, x2, y2):
    """
    entrance:
        x1, y1, x2, y2(float)
    return:
    distance(float)
    """
    x = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
    return x

x1, y1 = map(float, input("введите координаты первой точки(x y):").split())

x2, y2 = map(float, input("введите координаты второй точки(x y):").split())

calculate_distance = distance(x1, y1, x2, y2)

print (f"Расстояние между точками: {calculate_distance:.2f}")

#площадь треугольника

def calculate_triangle_area(a, b, c):
    """
    entrance:
        a, b, c(float)
    return:
        triangle_area
    """
    semi_perimeter = (a + b + c)/2
    triangle_area = (semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c)) ** 0,5
    return triangle_area

a, b, c= map(float, input("введите длины сторон a-c, через пробел: ").split())
calculate_area = calculate_triangle_area(a, b, c)
print(f"площадь треугольника равна: {calculate_area:.2f}")
