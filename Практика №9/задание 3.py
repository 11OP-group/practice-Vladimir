money = int(input("Введите кол-во монет --> "))

coins = 0

#расчетный блок для определения мин кол-ва монет
while money > 0:
        
    if money >= 25:
        money = money - 25

    elif money >= 10:
        money -= 10

    elif money >= 5:
        money -= 5

    elif money >= 1:
        money -= 1

    else:
        money -= 1

    coins = coins + 1
print(coins)