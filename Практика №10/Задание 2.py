number_1 = int(input("Введите первое число: "))

while True:

    number_2 = int(input("Введите второе число: "))

    if number_2 > number_1:
        break
    print("Второе число введено неверно, повторите попытку!")

while True:
    number_3 = int(input("Введите третье число: "))

    if number_3 > number_2:
        break
    print("Третье число введено неверно, повторите попыкту!")

print("Последовательность принята")


