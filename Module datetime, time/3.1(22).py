# функция, возвращающая количество суббот между двумя датами
from datetime import date


def saturdays_between_two_dates(start, end):
    counter = 0
    for i in range(min(start, end).toordinal(), max(start, end).toordinal() + 1):
        if date.fromordinal(i).weekday() == 5:
            counter += 1
    return counter


# TEST_1:
date1 = date(2021, 11, 1)
date2 = date(2021, 11, 22)

print(saturdays_between_two_dates(date1, date2))

# TEST_2:
date1 = date(2020, 7, 26)
date2 = date(2020, 7, 2)

print(saturdays_between_two_dates(date1, date2))

# TEST_3:
date1 = date(2018, 7, 13)
date2 = date(2018, 7, 13)

print(saturdays_between_two_dates(date1, date2))

# TEST_4:
date1 = date(2010, 6, 13)
date2 = date(2011, 7, 14)
print(saturdays_between_two_dates(date1, date2))

# TEST_5:
date1 = date(2012, 7, 11)
date2 = date(2011, 8, 16)
print(saturdays_between_two_dates(date1, date2))

# TEST_6:
date1 = date(2021, 11, 1)
date2 = date(2021, 11, 5)
print(saturdays_between_two_dates(date1, date2))

# TEST_7:
date1 = date(2021, 11, 1)
date2 = date(2021, 11, 6)
print(saturdays_between_two_dates(date1, date2))

# TEST_8:
date1 = date(2018, 7, 14)
date2 = date(2018, 7, 14)
print(saturdays_between_two_dates(date1, date2))

