coffee = 1
tea = 2
juice = 3
water = 4
lemonade = 5

PRICE_COFFEE = 120
PRICE_TEA = 80
PRICE_JUICE = 100
PRICE_WATER = 50
PRICE_LEMONADE = 90

Drink = int(input("Введите носмер напитка от 1 до 5: "))
match Drink:
    case 1:
        print(f"1 - coffee ☕ = {PRICE_COFFEE} руб.")

    case 2:
        print(f"2 - tea ☕ = {PRICE_TEA} руб.")

    case 3:
        print(f"3 - juice ☕ = {PRICE_JUICE} руб.")

    case 4:
        print(f"4 - water ☕ = {PRICE_WATER} руб.")

    case 5:
        print(f"5 - lemonade ☕ = {PRICE_LEMONADE} руб.")
