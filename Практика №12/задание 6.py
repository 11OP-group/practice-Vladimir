slovo = list(input("ввдите слово: "))
print(slovo)

perev = slovo[ ::-1]

print(perev)

if slovo[:] == perev[:]:
    print("Это палиндром!")
else:
    print("не палиндром")