#Считаем площадь прямоугольника >

#Входные данные
def calculate_rectangle_area(width, height):
    """Площадь прямоугольника

    ertrance:
        height, width(float): вводим высоту и ширину

    return:
        (float): площадь прямоугольника
    """
    return width * height # площадь прямоугольника

width, height = map(float, input("введите сначала ширину, а потом высоту, через пробел:").split())

rectangle_area = calculate_rectangle_area(width, height)

print(f"площадь прямоугольника равна: {rectangle_area:.2f}")

#Считаем площадь круга >

import math #импортируем библиотеку

#входные данные
def calculate_circle_area(radius):
    """" Площадь круга
    ertrance:
        radius(float): вводим радиус

    return:
        (float): площадь круга
    """
    return math.pi * (radius**2) # Считаем площадь круга

radius = float(input("Введите радиус окружности: "))

circle_area = calculate_circle_area(radius)

print(f"Площадь круга равна -> {circle_area:.1f}")