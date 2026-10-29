word = input("Введите слово --> ")

quantity = 0

while word != "хватит" and word != "достаточно" and word != "стоп":
    quantity = quantity + 1
    word = input("Введите слово --> ")

print("Кол-во введенных слов =", quantity)