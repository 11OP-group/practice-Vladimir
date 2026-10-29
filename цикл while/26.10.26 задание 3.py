num = int(input("Введите оценку -- > "))

count = 0

while 0<num<=5:
    if num == 5:
        count = count + 1
    num = int(input("Введите оценку -- > "))
print(count)