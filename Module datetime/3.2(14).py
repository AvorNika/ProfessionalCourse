# функция, возвращающая "интересные" даты, у которых год равен 1992, а сумма номеров месяца и дня равны 29
from datetime import date


def print_good_dates(dates):
    new_dates = list(filter(lambda y: y.year == 1992 and y.month + y.day == 29, dates))
    new_dates.sort()
    result = list(map(lambda x: x.strftime('%B %d, %Y'), new_dates))
    print(*result, sep='\n')


# TEST_1:
dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)

# TEST_2:
dates = [date(1993, 9, 15), date(2021, 11, 2), date(2000, 7, 7)]
print_good_dates(dates)

# TEST_3:
print_good_dates([])

# TEST_4:
dates = [date(1992, 5, 24), date(1000, 1, 1), date(2000, 2, 2), date(3000, 3, 3)]
print_good_dates(dates)

# TEST_5:
dates = [date(1257, 8, 22), date(1765, 8, 23), date(1999, 9, 9), date(1992, 6, 23)]
print_good_dates(dates)

# TEST_6:
dates = [date(1992, 9, 20), date(1992, 8, 21), date(1992, 7, 22), date(1992, 10, 19)]
print_good_dates(dates)

# TEST_7:
dates = [date(1257, 12, 12), date(1992, 6, 23), date(1284, 11, 2), date(1992, 1, 1)]
print_good_dates(dates)

# TEST_8:
print(print_good_dates([]))
