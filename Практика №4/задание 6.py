import math

x = float(input("введите значение x"))

r = math.radians(x)

v = math.sin(r) + math.cos(r) + math.tan(r)**2

print(v)