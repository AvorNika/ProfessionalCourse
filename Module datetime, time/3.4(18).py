# функция, возвращающая количество воскресений вводимого года
from datetime import datetime, timedelta


def num_of_sundays(year):
    day_for_check = datetime(year=year, month=1, day=1)
    end_of_year = datetime(year=year, month=12, day=31)
    while day_for_check.weekday() != 6:
        day_for_check += timedelta(days=1)
    else:
        return ((end_of_year - day_for_check) // 7).days + 1


# TEST_1:
print(num_of_sundays(2021))

# TEST_2:
year = 2000
print(num_of_sundays(year))

# TEST_3:
print(num_of_sundays(768))

# TEST_4:
print(num_of_sundays(1944))

# TEST_5:
print(num_of_sundays(2022))

# TEST_6:
print(num_of_sundays(2050))
