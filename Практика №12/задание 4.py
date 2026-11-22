marks = [5, 4, 3, 5, 2, 5, 4, 3, 5, 5]

fives = 0

two = 0

for marks in marks:
    if marks == 5:
        fives += 1
    elif marks == 2:
        two += 1

print(fives, two)