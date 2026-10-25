from random import *

n = 0

number = randint(1,10)
for i in range(1,4):
    print(f"Итак, да начнётся угадайка🃏! Это попытка номер --> {i} 🎲")
    num = int(input("Введите число --> "))
    if num > number:
        print("а вот и нет, задуманное число меньше 🤡")
    elif num < number:
        print("не не не,задуманное число больше 🤡")
    elif num == number:
        print("🎰🎰🎰  ДА ЛАДНОООО ЧИСЛО РЕАЛЬНО ТАКОЕ ЖЕ, ЭТО ОКУП!  🎰🎰🎰")

        break
else:
    print(f"Какая досада, заданное число было равно --> {number} 🙉")