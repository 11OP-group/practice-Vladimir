found = False

for a in range(1, 150):
    a5 = a**5
    for b in range(a,150):
        b5 = b**5
        for c in range(b,150):
            c5 = c**5
            for d in range(c, 150):
                d5 = d**5

                summa = a5 + b5 + c5 + d5

                e = round(summa ** (1/5))

                if e**5 == summa:
                    print(f'Найдены числа: a={a}, b={b}, c={c}, d={d}, e={e}')
                    print('Сумма a+b+c+d+e:', a + b + c + d + e)
                    found = True
                    break
            if found:
                break
        if found:
            break
    if found:
        break