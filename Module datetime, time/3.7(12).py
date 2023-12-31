# программа, выводящая список всех дат заданного месяца
from datetime import date
import calendar


def get_days_in_month(year, month):
    result = []
    user_month = list(calendar.month_name).index(month)
    days_range = calendar.monthrange(year, user_month)[1]
    for i in range(1, days_range + 1):
        result.append(date(year=year, month=user_month, day=i))
    
    return result


# TEST_1:
print(get_days_in_month(1982, 'January'))

# TEST_2:
print(get_days_in_month(2005, 'February'))

# TEST_3:
print(get_days_in_month(1971, 'March'))

# TEST_4:
print(get_days_in_month(2013, 'April'))

# TEST_5:
print(get_days_in_month(1981, 'May'))

# TEST_6:
print(get_days_in_month(1977, 'June'))

# TEST_7:
print(get_days_in_month(1957, 'July'))

# TEST_8:
print(get_days_in_month(1970, 'August'))

# TEST_9:
print(get_days_in_month(1957, 'September'))

# TEST_10:
print(get_days_in_month(1998, 'October'))

# TEST_11:
print(get_days_in_month(1970, 'November'))

# TEST_12:
print(get_days_in_month(2021, 'December'))
