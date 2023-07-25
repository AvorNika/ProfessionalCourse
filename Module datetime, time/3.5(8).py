# программа, определяющая время, оставшееся до выхода курса
from datetime import datetime, timedelta
current_date = datetime.strptime(input(), '%d.%m.%Y %H:%M')
finish_date = datetime(year=2022, month=11, day=8, hour=12)

diff = finish_date - current_date

def choose_plural(amount, declensions):
    info = {(1, ): declensions[0],
            (2, 3, 4): declensions[1],
            (5, 6, 7, 8, 9, 0): declensions[2]}
    if amount % 100 in range(11, 15):
        return f'{amount} {declensions[2]}'
    else:
        for i in info:
            if amount % 10 in i:
                return f'{amount} {info[i]}'

days_for_print = ['день', 'дня', 'дней']
hours_for_print = ['час', 'часа', 'часов']
minutes_for_print = ['минута', 'минуты', 'минут']

if diff <= timedelta(days=0, seconds=0):
    print('Курс уже вышел!')
elif diff.days == 0:
    if diff.seconds % 3600 == 0:
        print(f'До выхода курса осталось: {choose_plural(diff.seconds // 3600, hours_for_print)}')
    elif diff.seconds < 3600:
        print(f'До выхода курса осталось: {choose_plural((diff.seconds % 3600) //  60, minutes_for_print)}')
    else:
        print(f'До выхода курса осталось: {choose_plural(diff.seconds // 3600, hours_for_print)} и {choose_plural((diff.seconds % 3600) //  60, minutes_for_print)}')
elif diff.seconds == 0:
    print(f'До выхода курса осталось: {choose_plural(diff.days, days_for_print)}')
else:
    print(f'До выхода курса осталось: {choose_plural(diff.days, days_for_print)} и {choose_plural((diff.seconds - diff.seconds // (3600 * 24)) // 3600, hours_for_print)}')

