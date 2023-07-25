# программа, проверяющая корректность дат из переданного ей списка
from datetime import date


def is_correct(day, month, year):
    try:
        if date(int(year), int(month), int(day)):
            return True
    except ValueError:
        return False


dates = []
while True:
    dates.append(input())
    if dates[-1] == 'end':
        break

dates = dates[:-1]
counter = 0

for elem in dates:
    d, m, y = elem.split('.')
    if is_correct(d, m, y):
        print('Корректная')
        counter += 1
    else:
        print('Некорректная')

print(counter)
