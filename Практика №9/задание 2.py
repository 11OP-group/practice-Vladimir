name = input("Введите имя: ")

found = False

count_name = 0

while name != "Левон":

    if found:
        count_name += 1

    if name == "Александра":
        found = True

    name = input("Введите имя: ")

print(f"людей между Александрой и Левоном: {count_name}")
