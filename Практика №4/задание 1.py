import math

a = float(input("введите первое число:"))
b = float(input("введите второе число:"))

a = math.floor(a)
b = math.ceil(b)

print("округляя вниз до целого ==", a)
print("округляя вверх до целого ==", b)

print(a+b)