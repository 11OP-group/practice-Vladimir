income = float(input("введите размер вашего дохода"))

#размер налога в процентах
tax_rate = 0.13

tax_amount = income * tax_rate
net_income = income - tax_amount


print(f"Общая сумма дохода:  {income}")
print(f"Сумма рассчитанного налога: {tax_amount}")
print(f"Сумма «на руки» после вычета налога: {net_income}")