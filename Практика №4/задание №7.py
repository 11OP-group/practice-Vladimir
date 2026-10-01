number_place = int(input("введите номер вашего места"))

NUMBER_OF_SEATS = 4

place = (number_place  - 1) // NUMBER_OF_SEATS + 1


print("Ваше место в купе №", place)