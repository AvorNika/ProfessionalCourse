# программа, определяющая даты бесплатных посещений Эрмитажа (третий четверг месяца)
from datetime import datetime


def get_all_thursdays(year):
    thursdays = {}
    result = []
    start_date = datetime(year=year, month=1, day=1).toordinal()
    end_date = datetime(year=year, month=12, day=31).toordinal()
    for i in range(start_date, end_date + 1):
        med_date = datetime.fromordinal(i)
        if med_date.weekday() == 3:
            if med_date.month not in thursdays:
                thursdays[med_date.month] = [datetime.fromordinal(i)]
            else:
                thursdays[med_date.month].append(datetime.fromordinal(i))
    
    for key in thursdays.keys():
        result_date = thursdays[key][2].strftime('%d.%m.%Y')
        result.append(result_date)

    return result


x = get_all_thursdays(int(input()))
print(*x, sep='\n')