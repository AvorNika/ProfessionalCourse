# программа, определяющая день недели по заданной дате
import calendar
from datetime import datetime
user_date = datetime.strptime(input(), '%Y-%m-%d')
print(list(calendar.day_name)[calendar.weekday(year=user_date.year, month=user_date.month, day=user_date.day)])