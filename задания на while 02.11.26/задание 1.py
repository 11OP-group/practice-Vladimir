#тут короче ставим константы

passw = "admin"
pop = 3


while pop > 0:

    password = input("Введите пароль --> ")

    if password == passw:
        print("Доступ разрешен")
        break
    pop = pop - 1

#ну а тут типо попытки закончились
if pop == 0:
    print("Вход заблокирован ಠ_ಠ ")
