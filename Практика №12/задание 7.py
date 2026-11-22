numbers = [10, 20, 30, 40, 50]

num = int(input("Введите число: "))

for i in range(len(numbers)):
    if numbers[i] == num:
        print(num)
        break
else:
    print("Такого числа нету ")


