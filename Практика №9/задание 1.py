n = int(input("Введите число --> "))

i = 1

while i <= n:
    if not (4 < i < 10)  and not( 16 < i < 38) and not (77 < i < 88):
        print(i)

    i = i+1
