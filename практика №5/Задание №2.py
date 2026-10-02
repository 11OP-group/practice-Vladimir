
#Ввод данных
weight, height = map(float, input("Введите сначала вес, а потом рост, через пробел: ").split())

#расчет ИМТ
bmi = weight / (height ** 2)

print(f"Ваш Индекс Массы Тела (ИМТ): {bmi:.1f}")
