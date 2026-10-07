number = int(input("Введите номер кармана: "))

if number == 0:
    print("ZERO")

elif 1 <= number <= 10:
    print( "красный" if number % 2 == 1 else  "черный")

elif 11 <= number <= 18:
    print("черный" if number % 2 == 1 else "красный" )

elif 19 <= number <= 28:
    print("красный" if number % 2 == 1 else "черный")

elif 29 <= number <= 35:
    print ("черный" if number % 2 == 1 else "красный")

else:
    print("ошибка ввода данных")