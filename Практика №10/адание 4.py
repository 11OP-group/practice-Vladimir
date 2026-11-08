prices = 0

while True:
    price = int(input("Введите цену товара:"))

    if price == 0:
        break

    if price < 0:
        print("Некорректная цена")
        continue

    if price > 0:
        prices = prices + price



if prices > 1000:
    prices = prices * 0.9

print("Сумма всех покупок составляет: ", prices)




