ballans = 1000

while True:

    print("1 - Информация о балансе")
    print("2 - Снять 100₽")
    print("3 - Пополнить баланс на 100₽")
    print("4 - Выйти")

    operation = input("Выберете операцию: ")

    if operation == "1":
        print("Ваш баланс составляет: ", ballans)

    if operation == "2":

        if ballans >= 100:
            ballans = ballans - 100
        else:
            print("Недостаточно средств")

    if operation == "3":
        ballans = ballans + 100

    if operation == "4":
        print("До свидания!")
        break

    else:
        print("Неверная команда")
