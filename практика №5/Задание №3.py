USD_TO_RUB = 95.50

def Convert_USD_TO_RUB(amount_usd):
    """ обмен долларов на рубли

    entrance:
        amount_usd(float): сумма в долларах

    return:
        Convert_USD_TO_RUB(float): сумма в рублях

    """
    # Умножаем кол-во долларов на курс к рублю
    return amount_usd * USD_TO_RUB

#Вводим сумму в долларах
quantity = input("Введите сумму в долларах -> ")

#присваиваем дробное значение
amount_usd = float(quantity)

amount_rub = Convert_USD_TO_RUB(amount_usd)

print(f"{amount_usd:.2F} = {amount_rub:.2F}")






