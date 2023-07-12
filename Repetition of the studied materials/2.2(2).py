# программа для определения алфавита, к которому относятся вводимые буквы
chars = [input() for _ in range(3)]
counter_en = 0
counter_ru = 0
for char in chars:
    if char in "AaBCcEeHKMOoPpTXxy":
        counter_en += 1
    elif char in "АаВСсЕеНКМОоРрТХху":
        counter_ru += 1

if counter_en == 3:
    print('en')
elif counter_ru == 3:
    print('ru')
else:
    print('mix')
