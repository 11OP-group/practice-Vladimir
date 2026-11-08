#Начинаем с нуля
numbers = 0

while True:
    #Запрос ввода чисел
    num = int(input("Введите число: "))

    if num == 0:
        print("Ввод чисел окончен")
        break

    if num > numbers:
        numbers = num

print("Максимальное число последовательности --> ", numbers)