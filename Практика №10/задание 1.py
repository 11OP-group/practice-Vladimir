correct_password = 4590

while True:
    password = int(input("Введите пароль: "))

    if password == correct_password:
        print(" «Доступ разрешен» ")
        break

    print(" «Ошибка. Попробуйте еще раз» ")

