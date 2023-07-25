# функция, возвращающая True или False в зависимости от того, можно ли составить корректную дату из переданных ей дня, месяца и года
from datetime import date


def is_correct(day, month, year):
    try:
        if date(year, month, day):
            return True
    except ValueError:
        return False


# TEST_1:
print(is_correct(31, 12, 2021))

# TEST_2:
print(is_correct(31, 13, 2021))

# TEST_3:
print(is_correct(32, 10, 2021))

# TEST_4:
print(is_correct(99, 99, 2021))

# TEST_5:
print(is_correct(31, 2, 2021))
