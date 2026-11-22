import random

numbers = [random.randint(1, 20) for i in range (5)]

print(numbers)

min_num = min(numbers)

numbers[0], numbers [min_num] = numbers [min_num], numbers[0]

print(numbers)