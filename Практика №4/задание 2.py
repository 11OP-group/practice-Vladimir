import math

def dist(x1, y1, x2, y2):
    x = math.sqrt(((x1 - x2)**2) + ((y1-y2)**2))
    return x

x1, y1 = map(float, input("введите координаты первой точки(x y):").split())

x2, y2 = map(float, input("введите координаты второй точки(x y):").split())

distance = dist(x1, y1, x2, y2)

print (f"Расстояние между точками: {distance:.2f}")
