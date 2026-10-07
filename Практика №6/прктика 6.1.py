temperature = int(input("Введите вашу температуру тела: "))

pressure = int(input("Введите ваше давление (верхнее): "))

pulse = int(input("Введите ваш пульс (уд/мин): "))

if 36 <= temperature <= 37 or 110 <= pressure <= 130 or 60 <= pulse <= 100:
    print("ваше состояние в норме!")

elif (35 <= temperature <= 36) or (37 <= temperature <= 38) or ( 105 <= pressure <= 110 or 130 <= pressure <= 140 ) or ( 55 <= pulse <= 60 or  100 <= pulse <= 110):
    print(" Вы находитесь в состоянии легкого недомогания")

else:
    print("Вам нужно обратиться к врачу!")

