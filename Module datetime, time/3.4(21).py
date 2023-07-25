# функция, в которой переданный список дат сортируется, добавляются недостающие последовательные даты и список возвращается
from datetime import datetime, timedelta


def fill_up_missing_dates(dates):
    new_dates = [datetime.strptime(i, '%d.%m.%Y') for i in dates]
    new_dates.sort()
    result = []
    for i in range(len(new_dates) - 1):
        result.append(new_dates[i].date())
        if new_dates[i + 1] - timedelta(days=1) == new_dates[i]:
            continue
        else:
            rang = (new_dates[i + 1] - new_dates[i]).days
            for j in range(1, rang):
                result.append((new_dates[i] + timedelta(days=j)).date())
    result.append(new_dates[-1].date())
    return list(map(lambda x: x.strftime('%d.%m.%Y'), result))


# TEST_1:
dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']

print(fill_up_missing_dates(dates))

# TEST_2:
dates = ['01.11.2021', '04.11.2021', '09.11.2021', '15.11.2021']

print(fill_up_missing_dates(dates))

# TEST_3:
dates = ['15.11.2021', '04.11.2021', '09.11.2021', '01.11.2021']

print(fill_up_missing_dates(dates))

# TEST_4:
dates = ['15.11.2021', '16.11.2021', '17.11.2021', '18.11.2021', '19.11.2021', '20.11.2021']
print(fill_up_missing_dates(dates))

# TEST_5:
dates = ['20.11.2021', '16.11.2021', '19.11.2021', '18.11.2021', '17.11.2021', '15.11.2021']
print(fill_up_missing_dates(dates))

# TEST_6:
dates = ['20.07.2021', '16.05.2021', '19.01.2021', '18.11.2021', '17.10.2021', '15.03.2021']
print(len(fill_up_missing_dates(dates)))

# TEST_7:
dates = ['20.07.2020', '16.05.2021', '19.01.2022', '18.11.2021', '17.10.2021', '15.03.2021']
print(len(fill_up_missing_dates(dates)))
