# функция, возвращающая список всех дат заданного года, выпадающих на ПН
from datetime import date


def get_all_mondays(year):
    result = []
    start_date = date(year=year, month=1, day=1).toordinal()
    end_date = date(year=year, month=12, day=31).toordinal()
    for i in range(start_date, end_date + 1):
        if date.fromordinal(i).weekday() == 0:
            result.append(date.fromordinal(i))

    return result


# TEST_1:
print(get_all_mondays(111))

# TEST_2:
print(get_all_mondays(994))

# TEST_3:
print(get_all_mondays(1353))

# TEST_4:
print(get_all_mondays(1864))

# TEST_5:
print(get_all_mondays(1945))

# TEST_6:
print(get_all_mondays(1976))

# TEST_7:
print(get_all_mondays(1989))

# TEST_8:
print(get_all_mondays(1999))

# TEST_9:
print(get_all_mondays(2001))

# TEST_10:
print(get_all_mondays(2007))

# TEST_11:
print(get_all_mondays(2011))

# TEST_12:
print(get_all_mondays(2021))

# TEST_13:
print(get_all_mondays(2077))
